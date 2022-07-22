#####FUNCTIONS USED IN THE PROGRAM#####

def string_to_seconds(string) :                 #convert a string looking like "hh:mm:ss"
 L=string.split(":")                            #  into the number of seconds represented
 hh, mm, ss = int(L[0]), int(L[1]), int(L[2])   #  by this amount of time
 hs, ms = hh*3600, mm*60
 ts = hs+ms+ss
 return ts

def seconds_to_string(integer) :                #convert a number of seconds into
 hh,ss = divmod(integer,3600)                    #  a string looking like "hh:mm:ss"
 mm,ss = divmod(ss,60)
 if hh<10 :
  hh="".join(["0",str(int(hh))])
 else :
  hh=str(int(hh))
 if mm<10 :
  mm="".join(["0",str(int(mm))])
 else :
  mm=str(int(mm))
 if ss<10 :
  ss="".join(["0",str(int(ss))])
 else :
  ss=str(int(ss))
 return ":".join([hh,mm,ss])

#####THE PROGRAM ITSELF#####

import os
from lxml import etree
path=input("path to folder : ")
os.chdir(path)

file=input("name of reference file : ")
et=etree.parse(file)
root=et.getroot()

t=input("reference time (hh:mm:ss) = ")
tref=string_to_seconds(t)

t=input("time wanted (hh:mm:ss) = ")
tw=string_to_seconds(t)

#iterate through all XML elements
for elem in root.getiterator():
 #skip comments and processing instructions,
 #  because they do not have names
 if not (
  isinstance(elem, etree._Comment)
  or isinstance(elem, etree._ProcessingInstruction)
 ):
  #remove a namespace URI in the element's name
  elem.tag = etree.QName(elem).localname

#remove unused namespace declarations
etree.cleanup_namespaces(root)

#changing metadata time
dstart=input("departure date (aaaa-mm-jj) = ")
tstart=input("time of departure (hh:mm:ss) = ")
root.find("metadata/time").text=dstart+"T"+tstart+"Z"

#changing time of first trkpt
tprev=string_to_seconds(root.find("trk/trkseg/trkpt/time").text[11:-1:])
root.find("trk/trkseg/trkpt").text=dstart+"T"+tstart+"Z"

#changing other times
tn=string_to_seconds(tstart)
for trkpt in root.findall("trk/trkseg/trkpt")[1::]:
 tnext=string_to_seconds(trkpt.find("time").text[11:-1:])
 diff=tnext-tprev
 diffpond=diff*(tw/tref)                  #so that is space between 2 points isn't linear
 tn=tn+diffpond
 trkpt.find("time").text=dstart+"T"+seconds_to_string(tn)+"Z"
 tprev=tnext

#saving
et.write("new-"+file)
