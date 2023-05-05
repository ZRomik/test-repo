import sys
import os
from helloprinter import print_hello
def say_hello(_from: str) -> None:
    print(f"Hello World from {_from}!")

if __name__  == "__main__":
    print_hello(os.path.basename(__file__))