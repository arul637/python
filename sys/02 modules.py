import sys

modules = sys.modules.keys()

print("system modules:-\n")
for i in modules:
    print(i)

modules = sys.modules

print("\nsystem modules:-")
for i in modules.items():
    print(i)

