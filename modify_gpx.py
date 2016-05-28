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
path=input("path to folder : ")
os.chdir(path)

file=input("name of reference file : ")
b=open(file,"r",encoding='utf8')
n=open("-".join(["new",file]),"w",encoding='utf8')

t=input("reference time (hh:mm:ss) = ")
tref=string_to_seconds(t)

t=input("time wanted (hh:mm:ss) = ")
tw=string_to_seconds(t)

base=b.readlines()                            #the 1st 3 lines don't change
for i in range(3) :
 n.write(base[i])

dstart=input("departure date (aaaa-mm-jj) = ")
dstart="".join([dstart,"T"])
tstart=input("time of departure (hh:mm:ss) = ")
n.write("".join(["  <time>",dstart,tstart,"Z</time>\n"]))  #to change the time of departure

for i in range(4,10) :                        #then again the time of departure
 n.write(base[i])                             #  with the appropriated structure
n.write("".join(["    <time>",dstart,tstart,"Z</time>\n"]))
n.write(base[11])

tn=string_to_seconds(tstart)
i=12                                          #we've written the previous lines already
while base[i] != '  </trkseg>\n' :            #that means the file is nearly ended
 n.write(base[i])                             #the 1st 2 lines are always the same
 n.write(base[i+1])
 i+=2
 
 t1=string_to_seconds(base[i][21:29:1])       #the interesting part is only between the 21st
 t2=string_to_seconds(base[i-4][21:29:1])     #  and 29th character
 diff=t1-t2
 diffpond=diff*(tw/tref)                  #so that is space between 2 points isn't linear
 tn=tn+diffpond                           #  it's proportional to the one made during the reference
 n.write("".join(["    <time>",dstart,seconds_to_string(tn),"Z</time>\n"]))
 n.write(base[i+1])                   #I hope you've not made your run between 2 days
 i+=2

for k in range(3) :
 n.write(base[i])
 i+=1

n.close()
b.close()

quit()
