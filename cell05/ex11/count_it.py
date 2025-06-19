import sys

args = sys.argv[1:]

if ien(args) == 0:
    print("none")
    else:
        print(F"parameters: {len(args)}")
        for arg in args:
            print(F"{arhs}: {len(arg)}")
