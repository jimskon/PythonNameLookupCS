import os 
from os import path 
import sys


from sortedcontainers import SortedDict
filePath="/home/class/SoftDev/namedata/"

class nameEntry:
  """
  Class to store data for a single name
  """
  def __init__(self, line : str):
    """
    Takes a single line and parses it into
    the fields
    """
    line=line.strip()
    data=line.split()
    self.name=data[0]
    self.percent=data[1]
    self.cumulative=data[2]
    self.rank=data[3]

class NameMap:
  """
  Class to store information about the 
  Statistics of names.
  For each name type, there is a dict
  for each name, there is a list of name %, cumulative %, rank
  """
  def __init__(self,nameFile : str):
    """
    create a new list of names with data
    given an index within range of 0..num-1
    """
    names = open(filePath+nameFile)
    self.namemap=SortedDict()
    for line in names:
      nameData=nameEntry(line)
      self.namemap[nameData.name]=nameData
    return
  def lookup(self,name):
    """
    lookup name in map
    return nameEntry
    else return none
    """
    return self.namemap.get(name)

  def lookup10(self,name):
    """
    lookup name in specified index
    return list of [%,%cum,rank] if in list
    else return none
    """
    i=self.namemap.bisect_right(name)
    print(i)
    low = max(0,i-5)
    high = min(len(self.namemap),i+5)
    result = []
    for j in range(low,high):
      result.append(self.namemap.peekitem(j))
    return result

def nameServer():
  fifoname="py" # unique name for fifos
  commandFifoFile = "/home/fifo/"+fifoname+"_commandFifo"
  resultFifoFile = "/home/fifo/"+fifoname+"_resultFifo"

  #Create Fifos is they don't exist
  if not path.exists(commandFifoFile):
    os.mkfifo(commandFifoFile)
    os.chmod(commandFifoFile, 0o777)
  if not path.exists(resultFifoFile):
    os.mkfifo(resultFifoFile)
    os.chmod(resultFifoFile, 0o777)

  print("Building namemaps ...",end="")
  femaleMap=NameMap('dist.female.first')
  maleMap=NameMap('dist.male.first')
  lastMap=NameMap('dist.all.last')
  print("done!");
  
  # Main loop.  Wait for message, process it, and return result.  Then loop.
  while True:
    print("Waiting for command");
    commandFifo=open(commandFifoFile, "r")
    resultFifo=open(resultFifoFile, "w")

    line = commandFifo.read()
    print("Command Recieved: ",line)

    fields=line.split(",")
    type = fields[0]
    name = fields[1]
    
    if (type=="Female"):
      data=femaleMap.lookup10(name)
    elif (type=="Male"):
      data=maleMap.lookup10(name)
    else:
      data=lastMap.lookup10(name)

    # Send results back to caller as JSON
    result='{"results":['
    for namedata in data:
      result+='{"name":"'+namedata[1].name+'","percent":'+namedata[1].percent+',"rank":'+namedata[1].rank+'},'
    # remove the extra comma at the end
    result = result[:-1]  
    result+=']}'

    # Print for debugging
    print("Sending:",result)

    resultFifo.write(result)
      
    resultFifo.close()
    commandFifo.close()


nameServer()
