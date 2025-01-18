#Imports
import time
import os
from Arkens import Slink, expi
import subprocess

#Expire the token
time.sleep(expi)
os.remove(Slink)

#Store the expired state of the token
subprocess.run(["git", "checkout", "main"])
subprocess.run(["git","add", Slink])
subprocess.run(["git", "commit", "main","-m", Slink])
subprocess.run(["git", "push", "main"])