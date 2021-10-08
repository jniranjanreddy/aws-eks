#!/usr/bin/env python3
import subprocess
cmd="uname -a"
sp=subprocess.Popen(cmd,shell=True/False,stdout=subprocess.PIPE,stderr=subprocess.PIPE,universal_newlines=True)
rc=sp.wait()
print(sp)