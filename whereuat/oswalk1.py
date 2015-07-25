import os, sys

projdir = sys.argv[1]
projdir = os.path.normpath(projdir)

#Build List of Files
scripts = [os.path.join(r,f) 
           for r,s,fs in os.walk(projdir) 
           for f in fs]

#Filter scripts
def filterfiles(x,**kwargs):
    if x[-4:] == ".txt":
        return True
    return False

scripts = filter(filterfiles, scripts)

def searchfor(x):
    if "=" in x:
        return True
    return False

def breakdata(f, ind, line):
    #might need to decide if to use i_iInt, or u_iInt
    return (f,ind)
    
#Search through files
for f in scripts:
    myf = file(f)
    for ind, line in enumerate(myf.readlines()):
        if searchfor(line):
            d.append( breakdata(f, ind, line) )


#Chose an algo:
    #1. Break on next suitable line + break-Conditional
    #2. Prints output on that line
    
#Build breaks.xml
import xml

#Load xml template
#Alter values
#Output xml to default location
