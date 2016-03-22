import tkinter
import os
from tkinter import *
from tkinter import ttk
R1="1"
R2="1"
R3="1"
R4="1"
X1=""
G1=""
G2=""
G3=""
G4=""

class Feedback:

    def __init__(self,master):

        ### Header Section
        self.frame_header=ttk.Frame(master)
        self.frame_header.pack()
        
        ttk.Label(self.frame_header, text="Choose your path").grid(row=0,column=1, padx=10)

        self.entry_name=ttk.Entry(self.frame_header, width=35)

        self.entry_name.grid(row=1, column =1, padx=10)

        ttk.Button(self.frame_header, text='Browse',command=lambda: browse(self)).grid(row=1, column =3, padx=5)
        ttk.Button(self.frame_header, text='Clear',command=lambda: clear(self)).grid(row=1, column=4, padx=5)

        ### Content Section
        self.frame_content=ttk.Frame(master)
        self.frame_content.pack()

        self.listbox_initlist=Listbox(self.frame_content)
        self.listbox_initlist.grid(row=3, column=1, rowspan=2, columnspan=2, padx=5, pady=5, sticky=N+E)
        self.scrollbar=Scrollbar(self.frame_content, orient="vertical", command=self.listbox_initlist)
        self.listbox_initlist.configure(yscrollcommand=self.scrollbar.set)
        self.scrollbar.grid(row=3, column=3, rowspan=2, pady=5, sticky=N+S)
        
        
        ttk.Button(self.frame_content, text='>>', command=lambda: addselected(self)).grid(row=3, column=4, rowspan=2, padx=5, pady=5)
        
        self.listbox_finlist=Listbox(self.frame_content, selectmode=EXTENDED)
        self.listbox_finlist.grid(row=3, column=6, rowspan=2, columnspan=2, padx=5, pady=5)
        self.scrollbar_finlist=Scrollbar(self.frame_content, orient="vertical", command=self.listbox_finlist)
        self.listbox_finlist.configure(yscrollcommand=self.scrollbar_finlist.set)
        self.scrollbar_finlist.grid(row=3, column=8, rowspan=2, pady=5, sticky=N+S)
        
        ### Ending Section
        self.frame_ending=ttk.Frame(master)
        self.frame_ending.pack()
        
            ### Defining the Flags ###
        #ttk.Radiobutton(self.frame_ending, text='flags.T1.dcm2nii',variable="R1").grid(row=5, column=1, padx=5, pady=5)
        
        global X1
        X1=False
        global X2
        X2=False
        global X3
        X3=False
        global X4
        X4=False
        global var1
        global var2
        global var3
        global var4
        var1=BooleanVar()
        var2=BooleanVar()
        var3=BooleanVar()
        var4=BooleanVar()
        C1=ttk.Checkbutton(self.frame_ending, text='flags.T1.dcm2nii',variable=var1, command=lambda: printcheckbutton1(self)).grid(row=6, column=1, pady=5)
        C2=ttk.Checkbutton(self.frame_ending, text='flags.T1.anat',variable=var2, command=lambda: printcheckbutton2(self)).grid(row=6, column=2, pady=5)
        C3=ttk.Checkbutton(self.frame_ending, text='flags.T1.denoiser',variable=var3, command=lambda: printcheckbutton3(self)).grid(row=6, column=3, pady=5)
        C4=ttk.Checkbutton(self.frame_ending, text='flags.T1.bet', variable=var4, command=lambda: printcheckbutton4(self)).grid(row=6, column=4, pady=5)

        ttk.Button(self.frame_ending, text='Set flags', command=lambda: printcheckbutton1(self)).grid(row=7, column=2, rowspan=2, padx=5, pady=5)
        ttk.Button(self.frame_ending, text='Generate Script', command=lambda: genscript(self)).grid(row=7, column=4, rowspan=2, padx=5, pady=5)
        
def browse(self):
        global contents
        filedir=filedialog.askdirectory()
        self.entry_name.insert(tkinter.END,filedir)
        contents=os.listdir(filedir)
        for i in contents:
            self.listbox_initlist.insert(tkinter.END, str(i))
        
def clear(self):
        self.entry_name.delete(0,'end')
        self.listbox_initlist.delete(0,'end')
        self.listbox_finlist.delete(0,'end')
                 
def addselected(self):
        selected=self.listbox_initlist.curselection()
    #selected=map(int,selected)
    #selected=[self.selected[int(item)] for item in selected]
        global value
        value=self.listbox_initlist.get(selected[0])
        self.listbox_finlist.insert(tkinter.END, value)

def printcheckbutton1(self):
        global var1
        X1=var1.get()
        global G1
        if X1==True:
            G1='flags.T1.dcm2nii=1;'
            return G1
        elif X1==False:
            G1='flags.T1.dcm2nii=0;'
        else:
            G1='flags.T1.dcm2nii=0;'

def printcheckbutton2(self):
        global var2
        X2=var2.get()
        global G2
        if X2==True:
            G2='flags.T1.anat=1;'
            return G2
        elif X2==False:
            G2='flags.T1.anat=0;'
            return G2
        else:
            G2='flags.T1.anat=0;'

def printcheckbutton3(self):
        global var3
        X3=var3.get()
        global G3
        if X3==True:
            G3='flags.T1.denoiser=1;'
            return G3
        elif X3==False:
            G3='flags.T1.denoiser=0;'

def printcheckbutton4(self):
        global var4
        X4=var4.get()
        global G4
        if X4==True:
            G4='flags.T1.bet=1;'
            return G4
        elif X4==False:
            G4='flags.T1.bet=0;'
    
def genscript(self):
       file=open("/home/pkgandhi/GUI_testing/xml2struct.m","w")
       file.write("test \n")
       file.write(G1+"\n")
       file.write(G2+"\n")
       file.write(G3+'\n')
       file.write(G4+'\n')
       file.close()

def main():
        root=Tk()
        feedback=Feedback(root)
        root.mainloop()

if __name__ == "__main__": main()
