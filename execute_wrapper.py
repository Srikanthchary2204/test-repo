import subprocess
import sys
if __name__== "__main__":
    argl=sys.argv[1]
    print("calling script")
    status=subprocess.run("python3 codes.py",shell=True)
    