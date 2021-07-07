import webbrowser,subprocess,os,shutil
from pathlib import Path
import tkinter as tk
from tkinter.filedialog import askopenfilename
global root,username
selection = 0
num = 2
colorv = True
num2 = 2
colorv2 = True
filename = ""
root = tk.Tk()
root.title("8088 assembler")
root.configure(background='black')
root.geometry("204x220")
root.resizable(False,False) 
txt1=""
txt2="assemble 88"
txt3="Chose file"
username = str(os.getlogin())

if os.path.isfile('C:/Users/'+ username +'/AppData/Local/DOSBox/dosbox-0.74-3_buckup.conf') == True:
    os.remove("C:/Users/"+ username +"/AppData/Local/DOSBox/dosbox-0.74-3.conf")
    os.rename("C:/Users/"+ username +"/AppData/Local/DOSBox/dosbox-0.74-3_buckup.conf","C:/Users/"+ username +"/AppData/Local/DOSBox/dosbox-0.74-3.conf")
            

def openwebpage():
    webbrowser.open('https://github.com/LoreBadTime/8088-easy-builder', new=2)
    
def openwebpage2():
    webbrowser.open('https://github.com/LoreBadTime/C-easy-builder/blob/master/README.md', new=2)


def callback(num):
    global selection,build,filename,T,b,k,c,colorv,colorv2,directory,file,f_w_ext,configfile
    selection = num
    if selection == 3:
            if os.path.isfile('C:/Users/'+ username +'/AppData/Local/DOSBox/dosbox-0.74-3_buckup.conf') == True:
                os.remove("C:/Users/"+ username +"/AppData/Local/DOSBox/dosbox-0.74-3.conf")
                os.rename("C:/Users/"+ username +"/AppData/Local/DOSBox/dosbox-0.74-3_buckup.conf","C:/Users/"+ username +"/AppData/Local/DOSBox/dosbox-0.74-3.conf")
            filename = askopenfilename()
            directory = os.path.dirname(filename)
            file = os.path.basename(filename)
            f_w_ext = Path(filename).stem
            
            if filename == "":
                T.delete('1.0', tk.END)
                T.insert(tk.END, "Warning no input file")
                b.configure(foreground='red',activeforeground='red')
                e.configure(foreground='red',activeforeground='red')
                c.configure(foreground='yellow',activeforeground='yellow')
                k.configure(foreground='red',activeforeground='red')
                
            else:
                b.configure(foreground='green',activeforeground='yellow')
                build = True
            
    elif selection == 2:

            if filename == "" or filename == None or file.endswith('.s') != True :
                T.delete('1.0', tk.END)
                T.insert(tk.END, "Warning no input file")
                b.configure(foreground='red',activeforeground='red')
                e.configure(foreground='red',activeforeground='red')
                k.configure(foreground='red',activeforeground='red')
                c.configure(foreground='yellow',activeforeground='yellow')
            else:
                if os.path.isfile(str("C:/8088/" + f_w_ext + ".s")) == True:
                    os.remove(str("C:/8088/" + f_w_ext + ".s"))
                shutil.copy2(str(directory + "/" + f_w_ext + ".s"), str("C:/8088/"))
                if os.path.isfile(str("C:/8088/" + f_w_ext + ".#")) == True:
                    os.remove(str("C:/8088/" + f_w_ext + ".#"))
                if os.path.isfile(str("C:/8088/" + f_w_ext + ".88")) == True:
                    os.remove(str("C:/8088/" + f_w_ext + ".88"))
                if os.path.isfile(str("C:/8088/" + f_w_ext + ".$")) == True:
                    os.remove(str("C:/8088/" + f_w_ext + ".$"))
                if os.path.isfile(str("C:/8088/ASCIIFIL.$$$")) == True:
                    os.remove(str("C:/8088/ASCIIFIL.$$$"))
                if os.path.isfile('C:/Users/'+ username +'/AppData/Local/DOSBox/dosbox-0.74-3_buckup.conf') == True and colorv != True:
                    os.remove("C:/Users/"+ username +"/AppData/Local/DOSBox/dosbox-0.74-3.conf")
                    T.delete('1.0', tk.END)
                    os.rename("C:/Users/"+ username +"/AppData/Local/DOSBox/dosbox-0.74-3_buckup.conf","C:/Users/"+ username +"/AppData/Local/DOSBox/dosbox-0.74-3.conf")

                try:
                    if filename != "":
                        T.delete('1.0', tk.END)
                        T.insert(tk.END, file)
                        root.update()
                        if file.endswith('.s') != True :
                            T.delete('1.0', tk.END)
                            T.insert(tk.END, "not a source file")
                            b.configure(foreground='red',activeforeground='red')
                            c.configure(foreground='yellow',activeforeground='yellow')
                        else:
                            T.delete('1.0', tk.END)
                            T.insert(tk.END, file)
                            f = open('C:/Users/'+ username +'/AppData/Local/DOSBox/dosbox-0.74-3.conf','r+')
                            g = open('C:/Users/'+ username +'/AppData/Local/DOSBox/test_rep.conf','w')
                            lines = f.readlines()
                            for line in lines:
                                if line == "#config\n":                             #comment this to debug assembly errors
                                    lineg = line + str("as88 " + str(f_w_ext) +"\n")# + str("EXIT\n")
                                    g.write(lineg)
                                    
                                else:
                                    g.write(line)
                            f.close()
                            g.close()

                            os.rename("C:/Users/"+ username +"/AppData/Local/DOSBox/dosbox-0.74-3.conf","C:/Users/"+ username +"/AppData/Local/DOSBox/dosbox-0.74-3_buckup.conf")
                            os.rename("C:/Users/"+ username +"/AppData/Local/DOSBox/test_rep.conf","C:/Users/"+ username +"/AppData/Local/DOSBox/dosbox-0.74-3.conf")
                            e.configure(foreground='green',activeforeground='green')
                            k.configure(foreground='green',activeforeground='green')
                            p = subprocess.Popen(str('C://Program Files (x86)//DOSBox-0.74-3//DOSBox.exe'))
                            p.wait()
                            os.remove("C:/Users/"+ username +"/AppData/Local/DOSBox/dosbox-0.74-3.conf")
                            T.delete('1.0', tk.END)
                            os.rename("C:/Users/"+ username +"/AppData/Local/DOSBox/dosbox-0.74-3_buckup.conf","C:/Users/"+ username +"/AppData/Local/DOSBox/dosbox-0.74-3.conf")
                except:
                    pass
                
                
                try:
                    if os.path.isfile(str("C:/8088/ASCIIFIL.$$$")) == True:
                        os.rename(str("C:/8088/ASCIIFIL.$$$"),str("C:/8088/" + f_w_ext + ".$"))
                except:
                    pass
    elif selection == 4:
        if filename == "" or filename == None or file.endswith('.s') != True :
                T.delete('1.0', tk.END)
                T.insert(tk.END, "Warning no input file")
                b.configure(foreground='red',activeforeground='red')
                e.configure(foreground='red',activeforeground='red')
                k.configure(foreground='red',activeforeground='red')
                c.configure(foreground='yellow',activeforeground='yellow')
                
        else:
                if build == True:
                    try:
                        if filename != "":
                            T.delete('1.0', tk.END)
                            T.insert(tk.END, file)
                            root.update()
                            if file.endswith('.s') != True :
                                T.delete('1.0', tk.END)
                                T.insert(tk.END, "not a source file")
                                b.configure(foreground='red',activeforeground='red')
                                c.configure(foreground='yellow',activeforeground='yellow')
                            else:
                                T.delete('1.0', tk.END)
                                T.insert(tk.END, file)
                                f = open('C:/Users/'+ username +'/AppData/Local/DOSBox/dosbox-0.74-3.conf','r+')
                                g = open('C:/Users/'+ username +'/AppData/Local/DOSBox/test_rep.conf','w')
                                lines = f.readlines()
                                for line in lines:
                                    if line == "#config\n":                             #comment this to debug assembly errors
                                        lineg = line + str("t88 " + str(f_w_ext) +"\n")# + str("EXIT\n")
                                        g.write(lineg)
                                        
                                    else:
                                        g.write(line)
                                f.close()
                                g.close()

                                os.rename("C:/Users/"+ username +"/AppData/Local/DOSBox/dosbox-0.74-3.conf","C:/Users/"+ username +"/AppData/Local/DOSBox/dosbox-0.74-3_buckup.conf")
                                os.rename("C:/Users/"+ username +"/AppData/Local/DOSBox/test_rep.conf","C:/Users/"+ username +"/AppData/Local/DOSBox/dosbox-0.74-3.conf")

                                p = subprocess.Popen(str('C://Program Files (x86)//DOSBox-0.74-3//DOSBox.exe'))
                                p.wait()
                                os.remove("C:/Users/"+ username +"/AppData/Local/DOSBox/dosbox-0.74-3.conf")
                                T.delete('1.0', tk.END)
                                os.rename("C:/Users/"+ username +"/AppData/Local/DOSBox/dosbox-0.74-3_buckup.conf","C:/Users/"+ username +"/AppData/Local/DOSBox/dosbox-0.74-3.conf")
                    except:
                              pass
                
    elif selection == 5:
        
            if filename == "" or filename == None or file.endswith('.s') != True :
                T.delete('1.0', tk.END)
                T.insert(tk.END, "Warning no input file")
                b.configure(foreground='red',activeforeground='red')
                e.configure(foreground='red',activeforeground='red')
                k.configure(foreground='red',activeforeground='red')
                c.configure(foreground='yellow',activeforeground='yellow')
                
            else:
                if build == True:
                    try:
                        if filename != "":
                            T.delete('1.0', tk.END)
                            T.insert(tk.END, file)
                            root.update()
                            if file.endswith('.s') != True :
                                T.delete('1.0', tk.END)
                                T.insert(tk.END, "not a source file")
                                b.configure(foreground='red',activeforeground='red')
                                c.configure(foreground='yellow',activeforeground='yellow')
                            else:
                                T.delete('1.0', tk.END)
                                T.insert(tk.END, file)
                                f = open('C:/Users/'+ username +'/AppData/Local/DOSBox/dosbox-0.74-3.conf','r+')
                                g = open('C:/Users/'+ username +'/AppData/Local/DOSBox/test_rep.conf','w')
                                lines = f.readlines()
                                for line in lines:
                                    if line == "#config\n":                             #comment this to debug assembly errors
                                        lineg = line + str("s88 " + str(f_w_ext) +"\n")# + str("EXIT\n")
                                        g.write(lineg)
                                        
                                    else:
                                        g.write(line)
                                f.close()
                                g.close()

                                os.rename("C:/Users/"+ username +"/AppData/Local/DOSBox/dosbox-0.74-3.conf","C:/Users/"+ username +"/AppData/Local/DOSBox/dosbox-0.74-3_buckup.conf")
                                os.rename("C:/Users/"+ username +"/AppData/Local/DOSBox/test_rep.conf","C:/Users/"+ username +"/AppData/Local/DOSBox/dosbox-0.74-3.conf")
                                
                                p = subprocess.Popen(str('C://Program Files (x86)//DOSBox-0.74-3//DOSBox.exe'))
                                p.wait()
                                os.remove("C:/Users/"+ username +"/AppData/Local/DOSBox/dosbox-0.74-3.conf")
                                T.delete('1.0', tk.END)
                                os.rename("C:/Users/"+ username +"/AppData/Local/DOSBox/dosbox-0.74-3_buckup.conf","C:/Users/"+ username +"/AppData/Local/DOSBox/dosbox-0.74-3.conf")
                    except:
                              pass
                
    try: 
        return filename,directory,file,f_w_ext
    except:
        pass
def clearjunk():
    
    e.configure(foreground='red',activeforeground='red')
    k.configure(foreground='red',activeforeground='red')
    
    for file in os.listdir("C:/8088/"):
        if file.endswith('.s') or file.endswith('.#') or file.endswith('.$') or file.endswith('.88') or file.endswith('.$$$'):
            os.remove("C:/8088/"+ file)
if os.path.isfile('C:/8088/as88.exe') != True or os.path.isfile('C:/Program Files (x86)/DOSBox-0.74-3/DOSBox.exe') != True:
    d = tk.Button(root, text="Download 8088 and Dosbox", height = 1,width = 25,activebackground='black',background='black',foreground='cyan')
    d.configure(command=lambda :openwebpage())
    d.place(x=10 ,y=50)
    
    T = tk.Text(root, height = 3, width = 22,)
    T.place(x=10 ,y=120)
    T.insert(tk.END, "Follow install \ninstructions ")
    
else:
    b = tk.Button(root, text=txt2, height = 1,width = 25,activebackground='black',background='black',foreground='yellow',activeforeground='red')
    b.configure(command=lambda :callback(2))
    b.place(x=10 ,y=20)                
    c = tk.Button(root, text=txt3, height = 1,width = 25,activebackground='black',background='black',foreground='white',activeforeground='yellow')
    c.configure(command=lambda :callback(3))
    c.place(x=10 ,y=50)
    e = tk.Button(root, text="tracer 88", height = 1,width = 25,activebackground='black',background='black',foreground='yellow',activeforeground='red')
    e.configure(command=lambda :callback(4))
    e.place(x=10 ,y=80)
    k = tk.Button(root, text="interprete 88", height = 1,width = 25,activebackground='black',background='black',foreground='yellow',activeforeground='red')
    k.configure(command=lambda :callback(5))
    k.place(x=10 ,y=110)
    T = tk.Text(root, height = 2, width = 22,)
    T.place(x=10 ,y=170)
    T.insert(tk.END, "chose a file")
    h = tk.Button(root, text="clear junk", height = 1,width = 25,activebackground='black',background='black',foreground='yellow',activeforeground='red')
    h.configure(command=lambda :clearjunk())
    h.place(x=10 ,y=140)
    

root.mainloop()

