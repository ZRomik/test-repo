import sys
import os
def say_hello(_from: str) -> None:
    print(f"Hello World from {_from}!")

if __name__  == "__main__":
    say_hello(os.path.basename(__file__))