#!/usr/bin/python

# Python Dependencies
import sys, getopt
import shutil

# User Dependencies
# -- None


# TODO:
# Program can be further updated:
# See: https://www.devdungeon.com/content/working-binary-data-pythonpython%20convert%20hexadecimal%20to
# Not sure if this article's methods are faster


# Convert a block of bytes(?) to hexidecimal(?)
def tohex(block):
    # convert the byte string block to a regular string
    str = ""
    for ch in block:
        str += hex(ch) + " "
    return str

# With our first command line argument (the picture, open)
with open(sys.argv[1], "rb") as f:

    # Read the first 7 bytes
    str = tohex(f.read(7))                                              # Read 7 bytes
    print_chars_from_hex(str)
    if str == '0xff 0xd8 0xff 0xdb 0x0 0x84 0x0 ':                      # Check the bytes against our header
        split = False                                                   # -- do not need to split
        str = tohex(f.read(64))                                         # -- read 64 more bytes
    elif str == '0xff 0xd8 0xff 0xe0 0x0 0x10 0x4a ':                   # Check the bytes against a different header
        split = True                                                    # -- will need to split
        str = tohex(f.read(18))                                         # -- read 18 bytes
        if str != '0x46 0x49 0x46 0x0 0x1 0x1 0x0 0x0 0x1 0x0 0x1 0x0 0x0 0xff 0xdb 0x0 0x43 0x0 ':     # check those next 18 bytes
            exit(0)                                                                                     # -- exit the program
        str = tohex(f.read(64))                                                                         # Convert 64 bytes to hex
    else:                                                                                               # else
        exit(0)                                                                                         # -- exit the program

    # Read the next section of the file
    if str != '0x3 0x2 0x2 0x3 0x2 0x2 0x3 0x3 0x3 0x3 0x4 0x3 0x3 0x4 0x5 0x8 0x5 0x5 0x4 0x4 0x5 0xa 0x7 0x7 0x6 0x8 0xc 0xa 0xc 0xc 0xb 0xa 0xb 0xb 0xd 0xe 0x12 0x10 0xd 0xe 0x11 0xe 0xb 0xb 0x10 0x16 0x10 0x11 0x13 0x14 0x15 0x15 0x15 0xc 0xf 0x17 0x18 0x16 0x14 0x18 0x12 0x14 0x15 0x14 ':          # check the bytes
        exit(0)                                                                                                                                                                                                                                                                                                 # -- exit the program

    # If split is true, read the next part
    if split:
        str = tohex(f.read(4))
        if str != '0xff 0xdb 0x0 0x43 ':
            exit(0)

    # Get the next 65 bytes
    str = tohex(f.read(65))
    if str != '0x1 0x3 0x4 0x4 0x5 0x4 0x5 0x9 0x5 0x5 0x9 0x14 0xd 0xb 0xd 0x14 0x14 0x14 0x14 0x14 0x14 0x14 0x14 0x14 0x14 0x14 0x14 0x14 0x14 0x14 0x14 0x14 0x14 0x14 0x14 0x14 0x14 0x14 0x14 0x14 0x14 0x14 0x14 0x14 0x14 0x14 0x14 0x14 0x14 0x14 0x14 0x14 0x14 0x14 0x14 0x14 0x14 0x14 0x14 0x14 0x14 0x14 0x14 0x14 0x14 ':
        exit(0)

    # Read the next 5 bytes
    str = tohex(f.read(5))
    if str != '0xff 0xc0 0x0 0x11 0x8 ':
        exit(0)

    # Disregard the next 4 bytes
    f.read(4)

    # Read the next 10 bytes
    str = tohex(f.read(10))
    if str != '0x3 0x1 0x22 0x0 0x2 0x11 0x1 0x3 0x11 0x1 ':
        exit(0)

    # If split if true, skip a slightly different amount of bytes
    if split:
        f.read(432)
    else:
        f.read(420)

    # Read the next 5 bytes and check them
    str = tohex(f.read(5))
    if str != '0xff 0xda 0x0 0xc 0x3 ':
        exit(0)

    # Print out PixelKnot detected message
    if split:
        print(sys.argv[1] + " ==============================>>>>>>>>>>rewritten pixel knot header detected!!!")
    else:
        print(sys.argv[1] + " ==============================>>>>>>>>>>original pixel knot header detected!!!")

    # Copy our picture with its metadata (ie copy2) to the matches folder for further review
    shutil.copy2(sys.argv[1], "./matches/")
