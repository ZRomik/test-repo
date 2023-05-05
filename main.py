import sys
import os
from helloprinter import print_hello

if __name__  == "__main__":
    print_hello(os.path.basename(__file__))