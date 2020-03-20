#!/usr/bin/env python3
import sys
from builtins import input


"""""""""""""""""""""""""""
        does this:

          SATOR
          RSATO
          ROSAT
          ROTSA
          ROTAS

"""""""""""""""""""""""""""

def sator(iput=None):
    if iput != None:
        x = iput
        new_string = ""

        print(str(x))
        while len(x) > 1:
            new_string += x[-1]
            x = x[:-1]
            print(new_string + x)
    else:
        x = str(input("enter a word: "))
        new_string = ""
        print(str(x))
        while len(x) > 1:
            new_string += x[-1]
            x = x[:-1]
            print(new_string + x)

if __name__ == '__main__':
    if len(sys.argv) > 1:
        sator(sys.argv[1])
    else:
        sator()
