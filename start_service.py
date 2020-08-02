""" """
import os
from gooey import Gooey, GooeyParser

@Gooey
def start():
    
    parser = GooeyParser(description="My Cool GUI Program!") 
    parser.add_argument('Filename', widget="FileChooser")
    parser.add_argument('Date', widget="DateChooser")

    os.chdir('./sanitara')
    os.system('uvicorn main:app --reload')
    

if __name__ == "__main__":
    start()