import os
import argparse
import sys


parser = argparse.ArgumentParser(description="To load \".env\" file.")

parser.add_argument("--file", help="user defined file", default=".env")

args = parser.parse_args()

# print(args.file)
fname = args.file

envdict = {}

with open(fname, "r") as f:
    l = f.read()
    
lines = l.strip("\n").split("\n")
# print(lines)

for line in lines:
    try:
        k, v = line.split("=")
    except:
        print(fname + " document format invalid.")
        print("Please change to string like this \"key\"=\"value\"")
        print(line)
        sys.exit()
    
    envdict[k] = v

print(envdict)

for k, v in envdict.items():
    try:
        os.environ[k]=str(v)
    except:
        print("Enviroment variable set faild")
        print(k + " : " + v + "cannot set.")
        sys.exit()
    else:
        print("Correcty seted value \"" + k + "\"" + " is \"" + os.environ.get(k) + "\"")