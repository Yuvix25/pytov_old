import os
if __name__ == "__main__":
    print(os.path.dirname(os.path.abspath(__file__)))
    if (input("Add this directory to path? (y/n) ").lower() == "y"):
        os.environ["PATH"] += ";" + os.path.dirname(os.path.abspath(__file__))
    else:
        print("Operation canceled by user.")