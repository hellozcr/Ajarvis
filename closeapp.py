import subprocess
from difflib import get_close_matches as find
from test import speak
from os import system


program=[]
progid=[]
progdict={}


cmd='powershell "gps |where mainwindowtitle |select Description'
cmd1='powershell "gps |where mainwindowtitle |select id'


proc=subprocess.Popen(cmd,shell=True,stdout=subprocess.PIPE)
proc1=subprocess.Popen(cmd1,shell=True,stdout=subprocess.PIPE)



for line in proc.stdout:
    st=(line.decode().rstrip())
    program.append(st)

for line in proc1.stdout:
    st=(line.decode().rstrip())
    progid.append(st)

for i in range(0,len(progid)):
    progdict[program[i]]=progid[i]


def close(c):
    global program,progid
    q=find(c,program)
    if q==[]:
        speak("no app found to close")
    
    else:
        for key,value in progdict.items():
            if key==q[0]:
                speak(f"{key} is closing")
                system("taskkill /im  "+ str(value))




    

