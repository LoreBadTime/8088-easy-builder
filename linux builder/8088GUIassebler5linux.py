import webbrowser,subprocess,os,shutil
from pathlib import Path
import tkinter as tk
from tkinter.filedialog import askopenfilename
global root,username,linuxfolder
import re
linuxfolder = str(os.path.expanduser("~"))
linuxdos = str(os.path.expanduser("~")) + str('/.dosbox/')
selection = 0
num = 2
colorv = True
num2 = 2
colorv2 = True
filename = ""
root = tk.Tk()
root.title("8088 assembler")
root.configure(background='black')
root.geometry("254x190")
root.resizable(False,False) 
txt1=""
txt2="assemble 88"
txt3="Chose file"


if os.path.isfile('./dosbox-0.74-3.conf') == True:
    shutil.copy2('./dosbox-0.74-3.conf', linuxdos)
    os.remove('./dosbox-0.74-3.conf')
if os.path.isfile('./8088/as88.exe') == True:
    shutil.copytree('./8088', str(linuxfolder + str("/8088/")))
    shutil.rmtree('./8088')



if os.path.isfile(linuxdos + '/dosbox-0.74-3_buckup.conf') == True:
    os.remove(linuxdos + "/dosbox-0.74-3.conf")
    os.rename(linuxdos + "/dosbox-0.74-3_buckup.conf",linuxdos + "/dosbox-0.74-3.conf")
def clearjunk():
    global linuxfolder
    for file in os.listdir(linuxfolder + "/8088/"):
        if file.endswith('.s') or file.endswith('.#') or file.endswith('.$') or file.endswith('.88') or file.endswith('.$$$'):
            os.remove(linuxfolder + "/8088/" + file)            

def openwebpage():
    webbrowser.open('https://github.com/LoreBadTime/8088-easy-builder', new=2)
    webbrowser.open('https://www.dosbox.com/download.php?main=1', new=2)

def callback(num):
    global selection,build,filename,T,b,k,c,colorv,colorv2,directory,file,f_w_ext,configfile,s,linuxfolder
    selection = num
    if selection == 3:
            if os.path.isfile(linuxdos + '/dosbox-0.74-3_buckup.conf') == True:
                os.remove(linuxdos + "/dosbox-0.74-3.conf")
                os.rename(linuxdos + "/dosbox-0.74-3_buckup.conf",linuxdos + "/dosbox-0.74-3.conf")
            filename = askopenfilename()
            directory = os.path.dirname(filename)
            file = os.path.basename(filename)
            f_w_ext = Path(filename).stem
            
            if filename == "" or file.endswith('.s') != True:
                T.delete('1.0', tk.END)
                T.insert(tk.END, "Warning no input file")
                e.configure(foreground='red',activeforeground='red')
                c.configure(foreground='yellow',activeforeground='yellow')
                k.configure(foreground='red',activeforeground='red')
                s.configure(foreground='red',activeforeground='red')
            else:
                T.delete('1.0', tk.END)
                T.insert(tk.END, file)
                e.configure(foreground='green',activeforeground='yellow')
                k.configure(foreground='green',activeforeground='yellow')
                s.configure(foreground='green',activeforeground='yellow')
                build = True
            
    elif selection == 4 or selection == 5 or selection == 6:
            clearjunk()

            if filename == "" or filename == None or file.endswith('.s') != True :
                T.delete('1.0', tk.END)
                T.insert(tk.END, "Warning no input file")
                e.configure(foreground='red',activeforeground='red')
                k.configure(foreground='red',activeforeground='red')
                s.configure(foreground='red',activeforeground='red')
                c.configure(foreground='yellow',activeforeground='yellow')
            else:
                fold88= linuxfolder + str("/8088/")
                copystring = f_w_ext
                f_w_ext = "tmp"
                if os.path.isfile(str(fold88 + f_w_ext + ".s")) == True:
                    os.remove(str(fold88 + f_w_ext + ".s"))
                shutil.copy2(str(directory + "/" + copystring + ".s"), str(fold88))
                os.rename(str(fold88 + copystring + ".s"),str(fold88 + f_w_ext + ".s"))
                if os.path.isfile(str(fold88 + f_w_ext + ".#")) == True:
                    os.remove(str(fold88 + f_w_ext + ".#"))
                if os.path.isfile(str(fold88 + f_w_ext + ".88")) == True:
                    os.remove(str(fold88 + f_w_ext + ".88"))
                if os.path.isfile(str(fold88 + f_w_ext + ".$")) == True:
                    os.remove(str(fold88 + f_w_ext + ".$"))
                if os.path.isfile(str(fold88 + "ASCIIFIL.$$$")) == True:
                    os.remove(str(fold88 + "ASCIIFIL.$$$"))
                if os.path.isfile(linuxdos + '/dosbox-0.74-3_buckup.conf') == True and colorv != True:
                    os.remove(linuxdos + "/dosbox-0.74-3.conf")
                    T.delete('1.0', tk.END)
                    os.rename(linuxdos + "/dosbox-0.74-3_buckup.conf",linuxdos + "/dosbox-0.74-3.conf")

                try:
                    if filename != "":
                        T.delete('1.0', tk.END)
                        T.insert(tk.END, file)
                        root.update()
                        if file.endswith('.s') != True :
                            T.delete('1.0', tk.END)
                            T.insert(tk.END, "not a source file")
                            e.configure(foreground='red',activeforeground='red')
                            k.configure(foreground='red',activeforeground='red')
                            s.configure(foreground='red',activeforeground='red')
                            c.configure(foreground='yellow',activeforeground='yellow')
                        else:
                            T.delete('1.0', tk.END)
                            T.insert(tk.END, file)
                            f = open(linuxdos + '/dosbox-0.74-3.conf','r+')
                            g = open(linuxdos + '/test_rep.conf','w')
                            lines = f.readlines()
                            for line in lines:
                                if line == "#config\n":
                                    if selection == 4:
                                        lineg = line + str("@ECHO file caricato:" + str(copystring) +".s\n") + str("as88 " + str(f_w_ext) +"\n") + str("REN ASCIIFIL.$$$ " + str(f_w_ext) +".$\n") + str("t88 " + str(f_w_ext) +"\n") #+ str("EXIT\n")
                                    elif selection == 6:
                                        lineg = line + str("@ECHO file caricato:" + str(copystring) +".s\n") + str("as88 " + str(f_w_ext) +"\n")
                                    else:
                                        lineg = line + str("@ECHO file caricato:" + str(copystring) +".s\n") + str("as88 " + str(f_w_ext) +"\n") + str("REN ASCIIFIL.$$$ " + str(f_w_ext) +".$\n") + str("s88 " + str(f_w_ext) +"\n")
                                    
                                    g.write(lineg)
                                    
                                else:
                                    g.write(line)
                            f.close()
                            g.close()

                            os.rename(linuxdos + "/dosbox-0.74-3.conf",linuxdos + "/dosbox-0.74-3_buckup.conf")
                            os.rename(linuxdos + "/test_rep.conf",linuxdos + "/dosbox-0.74-3.conf")
                            p = subprocess.Popen(str('dosbox'))
                            p.wait()
                            clearjunk()
                            if os.path.isfile(linuxdos + '/dosbox-0.74-3_buckup.conf') == True:
                                os.remove(linuxdos + "/dosbox-0.74-3.conf")
                                os.rename(linuxdos + "/dosbox-0.74-3_buckup.conf",linuxdos + "/dosbox-0.74-3.conf")
                            
                except:
                    pass
                f_w_ext = copystring
    try: 
        return filename,directory,file,f_w_ext
    except:
        pass

if os.path.isfile(str(linuxfolder + '/8088/as88.exe')) != True :
    d = tk.Button(root, text="Download 8088 and Dosbox", height = 1,width = 25,activebackground='black',background='black',foreground='cyan')
    d.configure(command=lambda :openwebpage())
    d.place(x=10 ,y=50)
    T = tk.Text(root, height = 3, width = 22,)
    T.place(x=10 ,y=120)
    T.insert(tk.END, "Follow install \ninstructions ")
    
else:              
    c = tk.Button(root, text=txt3, height = 1,width = 25,activebackground='black',background='black',foreground='white',activeforeground='yellow')
    c.configure(command=lambda :callback(3))
    c.place(x=10 ,y=20)
    e = tk.Button(root, text="tracer", height = 1,width = 25,activebackground='black',background='black',foreground='yellow',activeforeground='red')
    e.configure(command=lambda :callback(4))
    e.place(x=10 ,y=50)
    k = tk.Button(root, text="run", height = 1,width = 25,activebackground='black',background='black',foreground='yellow',activeforeground='red')
    k.configure(command=lambda :callback(5))
    k.place(x=10 ,y=80)
    s = tk.Button(root, text="syntax check", height = 1,width = 25,activebackground='black',background='black',foreground='yellow',activeforeground='red')
    s.configure(command=lambda :callback(6))
    s.place(x=10 ,y=110)
    T = tk.Text(root, height = 2, width = 28,)
    T.place(x=10 ,y=140)
    T.insert(tk.END, "chose a file")
    

root.mainloop()

