import subprocess
if __name__== "__main__":
    print("calling script")
    status=subprocess.run("python3 codes.py",shell=True)
    