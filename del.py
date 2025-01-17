import subprocess
import time
import os
from Arkens import Slink, expi
time.sleep(expi)
os.remove(Slink)
subprocess.call(["git", "commit"])
subprocess.call(["git", "push"])