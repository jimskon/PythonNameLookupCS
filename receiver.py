import os
from os import path
import sys

fifoName = "/home/fifo/scmp318example.fifo"
if not path.exists(fifoName):
        os.mkfifo(fifoName)

fifo = open(fifoName, "r")
for line in fifo:
        print("Received: " + line)
fifo.close()
