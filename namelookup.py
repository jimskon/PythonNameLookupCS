#!/usr/bin/env python3
# namelookup.py - Program to display name statistics
# James Skon, 2019
#!/usr/bin/env python

import cgi;
import cgitb
cgitb.enable()


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
    return list of <name,[%,%cum,rank]> if in list
    else return none
    """
    i=self.namemap.bisect_right(name)
    low = max(0,i-5)
    high = min(len(self.namemap),i+5)
    result = []
    for j in range(low,high):
      result.append(self.namemap.peekitem(j))
    return result


def lookup(name,data):
  print(data[name])

def print_header():
    print ("""Content-type: text/html\n""")

def main():
  femaleMap=NameMap('dist.female.first')
  maleMap=NameMap('dist.male.first')
  lastMap=NameMap('dist.all.last')

  form = cgi.FieldStorage()
  if (form.getvalue("name") and form.getvalue("type_select")):
      print_header()
      name=form.getvalue("name").upper()
      ltype=form.getvalue("type_select")
      if ltype=="Female":
        data=femaleMap.lookup10(name)
      elif ltype=="Male":
        data=maleMap.lookup10(name)
      else:
        data=lastMap.lookup10(name)
      result=""
      for namedata in data:
         if len(result) > 0:
           result+=","
         result+=namedata[1].name+","+namedata[1].percent+","+namedata[1].rank
      print(result)
  else:
      print("Error in submission")
        
main()
