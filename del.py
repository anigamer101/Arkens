import time
import git
import os
from Arkens import Slink, expi, repo
print(expi)
print(expi)
time.sleep(expi)
os.remove(Slink)
print(Slink)
repo.index.add([Slink]) 
repo.index.commit(Slink) 
origin = repo.remote(name='origin')
origin.push()