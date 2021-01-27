""" """
import os
import sys
from corree import corree
import arguments


def main():

    os.chdir('./sanitara')
    os.system('uvicorn main:app --reload')

if __name__ == "__main__":
    
    main(args)

