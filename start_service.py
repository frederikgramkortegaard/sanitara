""" """
import os

def main():

    os.chdir('./sanitara')
    os.system('uvicorn main:app --reload')

if __name__ == "__main__":
    main()
