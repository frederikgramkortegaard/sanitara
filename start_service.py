""" """
import os
from gooey import Gooey, GooeyParser

def start():
    os.chdir('./sanitara')
    os.system('uvicorn main:app --reload')
    

if __name__ == "__main__":
    start()