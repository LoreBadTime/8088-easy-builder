# 8088-easy-builder
GUI for the 8088 tracer toolkit

# Features:
<ul>
<li>easy file pickup</li>
<li>fast and automatized building process</li>
<li>implemented a fix/workaround for the filename bug</li>
<li>automatic cleanup after execution</li>
</ul>

# Prerequisites:
You need to get few files
```
as88.exe
t88.exe
s88.exe
CWSDPMI.EXE
```

and you need to pack them in a folder called 8088 like this
```
/8088/as88.exe
/8088/t88.exe
/8088/s88.exe
/8088/CWSDPMI.EXE
```

# Windows install Instructons:(working on windows 11)
<ol>
<li>Install <a href="https://www.dosbox.com/download.php?main=1">DOSBOX</a> and <a href="https://www.python.org/downloads/">python3(>3.8)</a></li>
<li>Download the source zip and unzip the file</li>
<li><p>Move the /8088 folder in windows builder directory in the unzipped file 

```
(folder tree)
-/windows builder/8088/
-/windows builder/dosbox-0.74-3.conf
-/windows builder/8088GUIassembler.pyw
```

</p></li>
<li>Start dosbox manually and close it once</li>
</ol>
Now just start 8088GUIassembler.pyw in "Windows builder" folder(you can change this file location)

# Linux install Instructons(Ubuntu based):
<ol>
<li><p>Install DOSBOX and python3(>3.8)
Terminal commands:

```
sudo apt-get install dosbox
sudo apt-get install python3 
```

PS:python could be already installed in the system,missing modules errors should be fixed manually by installing those modules
</p></li>
<li>Download the source zip and unzip the file</li>
<li><p>Move the /8088 folder in linux builder directory in the unzipped file

```
(folder tree)
-/linux builder/8088/
-/linux builder/dosbox-0.74-3.conf
-/linux builder/8088GUIassembler.pyw
```

</p></li>
<li><p>start dosbox once and close it

```
dosbox
```

</p></li>
Now just start 8088GUIassembler.py in "linux builder" folder(you can change this file location)
</ol>
PS:
If you get the error "non module named tkinter" run the command 

```
sudo apt-get install python3-tk
```
This error could happen on fresh Ubuntu installs

# MacOS install Instructons(UNTESTED VERSION,WILL PROBABLY NOT WORK):
```
1)Install DOSBOX and python3(>3.8)
2)Download the source zip and unzip the file
3)move the /8088 folder in MacOS builder directory in the unzipped file 

(folder tree)
-/MacOS builder/8088/
-/MacOS builder/dosbox-0.74-3.conf
-/MacOS builder/8088GUIassembler.pyw

4)start dosbox once and close it

```
Now just start 8088GUIassembler.py in "MacOS builder" folder(you can change this file location)

# FAQ
<ol>
<li><p>The builder is stuck in follow install instructions

```
This means that some files are badly placed,this problem depends by case so it sould be fixed manually(contact me or fill a issue)
```
</p></li>
<li><p>
Buttons do nothing

```
Try to replace manually the dosbox.conf provided in source folder into the default location following this link https://www.dosbox.com/wiki/Dosbox.conf
```
</p></li>
<li><p>
MacOS version does not work

```
its based on few feedbacks,but this is the best i can do since i don't own a MacOS
fill an issue so i can try to port it
```
</p></li>
<li><p>
How to remove the python shell?

```
Rename the .py extension into .pyw
```
</p></li>
</ol>
