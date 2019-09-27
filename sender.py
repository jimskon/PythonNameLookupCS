import os

fifoName = "/tmp/scmp318example.fifo"

fifo = open(fifoName, "w")
fifo.write("Message from the sender!\n")
fifo.close()
