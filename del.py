import subprocess
import time
import os
from Arkens import Slink, expi
time.sleep(expi)
os.remove(Slink)
f = subprocess.call(["git", "add", Slink])
subprocess.call(["git", "commit"])
subprocess.call(["git", "push", f])