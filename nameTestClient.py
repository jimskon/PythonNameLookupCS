# A rogram to test the nameserver program
import os 
from os import path 
import sys
fifoname="skon"  # Unique name for fifos

commandFifoFile = "/tmp/"+fifoname+"_commandFifo"
resultFifoFile = "/tmp/"+fifoname+"_resultFifo"

#Create Fifos if they don't exist
if not path.exists(commandFifoFile):
        os.mkfifo(commandFifoFile)
        os.chmod(commandFifoFile, 0o777)
if not path.exists(resultFifoFile):
        os.mkfifo(resultFifoFile)
        os.chmod(resultFifoFile, 0o777)

type=int(input("1=female,2=male,3=last: "))
name=input("Name:").upper()

if (type==1):
  ltype="Female"
elif (type==2):
  ltype="Male"
else:
  ltype="Last"

commandFifo=open(commandFifoFile, "w")
resultFifo=open(resultFifoFile, "r")

commandFifo.write(ltype+","+name)
commandFifo.close()
for line in resultFifo:
        print(line)

resultFifo.close()

print("Done!")
