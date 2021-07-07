# 8088-easy-builder
GUI 8088 builder(made for ARE course),(NEEDS DOSBOX,Windows-Linux)

Prerequisites:
before using it you need to get few files
```
as88.exe
t88.exe
s88.exe
CWSDPMI.EXE
```

you need to pack them in a folder called 8088 like this
```
/8088/as88.exe
/8088/t88.exe
/8088/s88.exe
/8088/CWSDPMI.EXE
```

Windows install Instructons:
```
1)Install DOSBOX and python3(>3.8)
2)Download the source zip and unzip the file
3)move the /8088 folder in C:/ directory (result C:/8088)
3)go to C:/Users/YOURUSERNAME/AppData/Local/DOSBox/ folder 
4)replace dosbox-0.74-3.conf with the one provided in the "Windows builder" folder in the zip file
```
Now just start 8088GUIassembler.py in "Windows builder" folder(you can change this file location)

Linux install Instructons(Ubuntu based;TEST VERSION COULD NOT WORK):
```
1)Install DOSBOX and python3(>3.8)
Terminal commands:
sudo apt-get install dosbox
sudo apt-get install python3 
python could be already installed in the system

2)run in terminal one time the command:
dosbox
and close the opened dosbox window
3)Download the source zip and unzip the file
4)move the /8088 folder in "/home/YOURUSERNAME/" directory (result "/home/YOURUSERNAME/8088/)
5)go to "/home/YOURUSERNAME/.dosbox/" folder 
6)replace dosbox-0.74-3.conf with the one provided in the "Linux builder" folder in the zip file
```
Now just start 8088GUIassembler.py in "linux builder" folder(you can change this file location)


