#Imports
import time
import os
from Arkens import Slink, expi
import cmd

#Expire the token
time.sleep(expi)
os.remove(Slink)

#Store the expired state of the token
cmd("git checkout main")
cmd("git commit")
cmd("git push -u https://github.com/anigamer101/Arkens.git")