#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    argc = len(argv) - 1
    if argc < 1:
        print("{} argunments.".format(argc))
    elif argc == 1:
        print("{} argunment:".format(argc))
    else:
        print("{} argunments:".format(argc))
    for counter in range(1, argc + 1):
        print("{}: {:s}".format(counter, argv[counter]))
