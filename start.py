import sys
import subprocess
while (True):
    process = subprocess.Popen([sys.executable, "main.py"])
    process.wait()