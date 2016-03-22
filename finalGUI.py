#####################################################################################################################################################################################################
############################################################# Program to generate .m script for connectivity ########################################################################################
############################################################# -- Helps to choose subjects from specific dir #########################################################################################
################################################################### -- Set flags as per requirements ################################################################################################
######## Developed by Pratik Gandhi
#############################################



### import necessary modules

import tkinter
import os
import sys
from tkinter import *
from tkinter import ttk
R1="1"
R2="1"
R3="1"
R4="1"
G1=""
G2=""
G3=""
G4=""

class Feedback:

    def __init__(self,master):

### Browse and Clear button to get path to the directory and to clear all the contents respectively. Path can be seen in the tab.
        self.frame_header=ttk.Frame(master)
        self.frame_header.pack()
        
        ttk.Label(self.frame_header, text="Choose your path").grid(row=0,column=1, padx=10)

        self.entry_name=ttk.Entry(self.frame_header, width=35)

        self.entry_name.grid(row=1, column =1, padx=10)

        ttk.Button(self.frame_header, text='Browse',command=lambda: browse(self)).grid(row=1, column =3, padx=5)
        ttk.Button(self.frame_header, text='Clear',command=lambda: clear(self)).grid(row=1, column=4, padx=5)

### Listbox section: Listing of subjects and choosing them:
        
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
        
### Ending Section: All the flags are called as well as the button to set them are here.
        
        self.frame_ending=ttk.Frame(master)
        self.frame_ending.pack()
        
        ### Defining the Flags ###
        
        global F1
        F1=False
        global F2
        F2=False
        global F3
        F3=False
        global F4
        F4=False
        global F5
        F5=False
        global F6
        F6=False
        
        global flag1,flag2,flag3,flag4,flag5,flag6
        global subflag11,subflag12,subflag13,subflag14,subflag15,subflag21,subflag22,subflag31,subflag32,subflag33,subflag34,subflag35,subflag36,subflag37,subflag41,subflag42,subflag43,subflag44,subflag45,subflag46,subflag47,subflag48,subflag49,subflag410,subflag411,subflag412,subflag51,subflag52,subflag53,subflag54,subflag61,subflag62,subflag63,subflag64,subflag65,subflag66,subflag67,subflag68,subflag69,subflag610,subflag611,subflag612

        flag1=BooleanVar()
        flag2=BooleanVar()
        flag3=BooleanVar()
        flag4=BooleanVar()
        flag5=BooleanVar()
        flag6=BooleanVar()
        subflag11=BooleanVar()
        subflag12=BooleanVar()
        subflag13=BooleanVar()
        subflag14=BooleanVar()
        subflag15=BooleanVar()
        subflag21=BooleanVar()
        subflag22=BooleanVar()
        subflag31=BooleanVar()
        subflag32=BooleanVar()
        subflag33=BooleanVar()
        subflag34=BooleanVar()
        subflag35=BooleanVar()
        subflag36=BooleanVar()
        subflag37=BooleanVar()
        subflag41=BooleanVar()
        subflag42=BooleanVar()
        subflag43=BooleanVar()
        subflag44=BooleanVar()
        subflag45=BooleanVar()
        subflag46=BooleanVar()
        subflag47=BooleanVar()
        subflag48=BooleanVar()
        subflag49=BooleanVar()
        subflag410=BooleanVar()
        subflag411=BooleanVar()
        subflag412=BooleanVar()
        subflag51=BooleanVar()
        subflag52=BooleanVar()
        subflag53=BooleanVar()
        subflag54=BooleanVar()
        subflag61=BooleanVar()
        subflag62=BooleanVar()
        subflag63=BooleanVar()
        subflag64=BooleanVar()
        subflag65=BooleanVar()
        subflag66=BooleanVar()
        subflag67=BooleanVar()
        subflag68=BooleanVar()
        subflag69=BooleanVar()
        subflag610=BooleanVar()
        subflag611=BooleanVar()
        subflag612=BooleanVar()
        

#### Main Flags Selection Checkbutton ####
        C1=ttk.Checkbutton(self.frame_ending, text='flag_T1_prepare_A',variable=flag1, command=lambda: printcheckbutton1(self)).grid(row=6, column=1, pady=5)
        C2=ttk.Checkbutton(self.frame_ending, text='flag_T1_prepare_B',variable=flag2, command=lambda: printcheckbutton1(self)).grid(row=6, column=2, pady=5)
        C3=ttk.Checkbutton(self.frame_ending, text='flag_PASL',variable=flag3, command=lambda: printcheckbutton1(self)).grid(row=6, column=3, pady=5)
        C4=ttk.Checkbutton(self.frame_ending, text='flag_fMRI_A', variable=flag4, command=lambda: printcheckbutton1(self)).grid(row=7, column=1, pady=5)
        C5=ttk.Checkbutton(self.frame_ending, text='flag_fMRI_B', variable=flag5, command=lambda: printcheckbutton1(self)).grid(row=7, column=2, pady=5)
        C6=ttk.Checkbutton(self.frame_ending, text='flag_DWI', variable=flag6, command=lambda: printcheckbutton1(self)).grid(row=7, column=3, pady=5)
      
        def reply(self):
            toplevel=Toplevel()

#### Making the subflag sections window ####
            
            sf1=Label(toplevel, text='flag_T1_prepare_A')
            sf1.grid(row=1,column=1,padx=5,pady=5)

            sf2=Label(toplevel, text='flag_T1_prepare_B')
            sf2.grid(row=1, column=2, padx=5, pady=5)
            
            sf3=Label(toplevel, text='flag_PASL')
            sf3.grid(row=1, column=3, padx=5, pady=5)

            sf4=Label(toplevel, text='flag_fMRI_A')
            sf4.grid(row=1, column=4, padx=5, pady=5)

            sf5=Label(toplevel, text='flag_fMRI_B')
            sf5.grid(row=1, column=5, padx=5, pady=5)

            sf6=Label(toplevel, text='flag_DWI')
            sf6.grid(row=1, column=6, padx=5, pady=5)

#### Subflags under flag_T1_prepare_A ####
            
            if flag1.get()==True:
                global subflag11
                subflag11=BooleanVar()
                c11=Checkbutton(toplevel, text='flags.T1.dcm2nii', variable=subflag11)
                c11.grid(row=3, column=1, padx=5, pady=5)

            if flag1.get()==True:
                global subflag12
                subflag12=BooleanVar()
                c12=Checkbutton(toplevel, text='flags.T1.anat', variable=subflag12)
                c12.grid(row=4, column=1, padx=5, pady=5)

            if flag1.get()==True:
                global subflag13
                subflag13=BooleanVar()
                c13=Checkbutton(toplevel, text='flags.T1.denoiser', variable=subflag13)
                c13.grid(row=5, column=1, padx=5, pady=5)

            if flag1.get()==True:
                global subflag14
                subflag14=BooleanVar()
                c14=Checkbutton(toplevel, text='flags.T1.bet', variable=subflag14)
                c14.grid(row=6, column=1, padx=5, pady=5)

            if flag1.get()==True:
                global subflag15
                subflag15=BooleanVar()
                c15=Checkbutton(toplevel, text='flags.T1.brain', variable=subflag15)
                c15.grid(row=7, column=1, padx=5, pady=5)

#### Subflags under flag_T1_prepare_B ####
            
            if flag2.get()==True:
                global subflag21
                subflag21=BooleanVar()
                c21=Checkbutton(toplevel, text='flags.T1.reg2MNI', variable=subflag21)
                c21.grid(row=3, column=2, padx=5, pady=5)

            if flag2.get()==True:
                global subflag22
                subflag22=BooleanVar()
                c22=Checkbutton(toplevel, text='flags.T1.seg', variable=subflag22)
                c22.grid(row=4, column=2, padx=5, pady=5)

#### Subflags under flag_PASL ####
            
            if flag3.get()==True:
                global subflag31
                subflag31=BooleanVar()
                c31=Checkbutton(toplevel, text='flags.RegT1', variable=subflag31)
                c31.grid(row=3, column=3, padx=5, pady=5)

            if flag3.get()==True:
                global subflag32
                subflag32=BooleanVar()
                c32=Checkbutton(toplevel, text='flags.RegOthers', variable=subflag32)
                c32.grid(row=4, column=3, padx=5, pady=5)

            if flag3.get()==True:
                global subflag33
                subflag33=BooleanVar()
                c33=Checkbutton(toplevel, text='flags.TissueMasks', variable=subflag33)
                c33.grid(row=5, column=3, padx=5, pady=5)

            if flag3.get()==True:
                global subflag34
                subflag34=BooleanVar()
                c34=Checkbutton(toplevel, text='flags.CBFrange', variable=subflag34)
                c34.grid(row=6, column=3, padx=5, pady=5)

            if flag3.get()==True:
                global subflag35
                subflag35=BooleanVar()
                c35=Checkbutton(toplevel, text='flags.SpatialSmooth', variable=subflag35)
                c35.grid(row=7, column=3, padx=5, pady=5)

            if flag3.get()==True:
                global subflag36
                subflag36=BooleanVar()
                c36=Checkbutton(toplevel, text='flags.ROIs', variable=subflag36)
                c36.grid(row=8, column=3, padx=5, pady=5)

            if flag3.get()==True:
                global subflag37
                subflag37=BooleanVar()
                c37=Checkbutton(toplevel, text='flags.CBF2MNI', variable=subflag37)
                c37.grid(row=9, column=3, padx=5, pady=5)

#### Subflags under flag_fMRI_A ####
            
            if flag4.get()==True:
                global subflag41
                subflag41=BooleanVar()
                c41=Checkbutton(toplevel, text='flags.dcm2nii', variable=subflag41)
                c41.grid(row=3, column=4, padx=5, pady=5)

            if flag4.get()==True:
                global subflag42
                subflag42=BooleanVar()
                c42=Checkbutton(toplevel, text='flags.SliceTimingCorr', variable=subflag42)
                c42.grid(row=4, column=4, padx=5, pady=5)

            if flag4.get()==True:
                global subflag43
                subflag43=BooleanVar()
                c43=Checkbutton(toplevel, text='flags.MotionCorr', variable=subflag43)
                c43.grid(row=5, column=4, padx=5, pady=5)

            if flag4.get()==True:
                global subflag44
                subflag44=BooleanVar()
                c44=Checkbutton(toplevel, text='flags.RegT1', variable=subflag44)
                c44.grid(row=6, column=4, padx=5, pady=5)

            if flag4.get()==True:
                global subflag45
                subflag35=BooleanVar()
                c35=Checkbutton(toplevel, text='flags.RegOthers', variable=subflag45)
                c35.grid(row=7, column=4, padx=5, pady=5)

            if flag4.get()==True:
                global subflag46
                subflag36=BooleanVar()
                c36=Checkbutton(toplevel, text='flags.Mode1000', variable=subflag46)
                c36.grid(row=8, column=4, padx=5, pady=5)

            if flag4.get()==True:
                global subflag47
                subflag37=BooleanVar()
                c37=Checkbutton(toplevel, text='flags.DemeanDetrend', variable=subflag47)
                c37.grid(row=9, column=4, padx=5, pady=5)

            if flag4.get()==True:
                global subflag48
                subflag48=BooleanVar()
                c48=Checkbutton(toplevel, text='flags.MotionRegressors', variable=subflag48)
                c48.grid(row=10, column=4, padx=5, pady=5)

            if flag4.get()==True:
                global subflag49
                subflag49=BooleanVar()
                c49=Checkbutton(toplevel, text='flags.BandPass', variable=subflag49)
                c49.grid(row=11, column=4, padx=5, pady=5)

            if flag4.get()==True:
                global subflag410
                subflag410=BooleanVar()
                c410=Checkbutton(toplevel, text='flags.TissueRegressors', variable=subflag410)
                c410.grid(row=12, column=4, padx=5, pady=5)

            if flag4.get()==True:
                global subflag411
                subflag411=BooleanVar()
                c411=Checkbutton(toplevel, text='flags.SpatialSmooth', variable=subflag411)
                c411.grid(row=13, column=4, padx=5, pady=5)

            if flag4.get()==True:
                global subflag412
                subflag412=BooleanVar()
                c412=Checkbutton(toplevel, text='flags.ROIs', variable=subflag412)
                c412.grid(row=14, column=4, padx=5, pady=5)

#### Subflags under flag_fMRI_B ####
            
            if flag5.get()==True:
                global subflag51
                subflag51=BooleanVar()
                c51=Checkbutton(toplevel, text='flags.FigsMotion', variable=subflag51)
                c51.grid(row=3, column=5, padx=5, pady=5)

            if flag5.get()==True:
                global subflag52
                subflag52=BooleanVar()
                c52=Checkbutton(toplevel, text='flags.FigsFC', variable=subflag52)
                c52.grid(row=4, column=5, padx=5, pady=5)

            if flag5.get()==True:
                global subflag53
                subflag53=BooleanVar()
                c53=Checkbutton(toplevel, text='flags.SaveFigs', variable=subflag53)
                c53.grid(row=5, column=5, padx=5, pady=5)

            if flag5.get()==True:
                global subflag54
                subflag54=BooleanVar()
                c54=Checkbutton(toplevel, text='flags.SaveMats', variable=subflag54)
                c54.grid(row=6, column=5, padx=5, pady=5)

#### Subflags under flag_DWI ####
            
            if flag6.get()==True:
                global subflag61
                subflag61=BooleanVar()
                c61=Checkbutton(toplevel, text='flags.dcm2nii', variable=subflag61)
                c61.grid(row=3, column=6, padx=5, pady=5)

            if flag6.get()==True:
                global subflag62
                subflag42=BooleanVar()
                c62=Checkbutton(toplevel, text='flags.order_filter', variable=subflag62)
                c62.grid(row=4, column=6, padx=5, pady=5)

            if flag6.get()==True:
                global subflag63
                subflag43=BooleanVar()
                c63=Checkbutton(toplevel, text='flags.denoiser', variable=subflag63)
                c63.grid(row=5, column=6, padx=5, pady=5)

            if flag6.get()==True:
                global subflag64
                subflag64=BooleanVar()
                c64=Checkbutton(toplevel, text='flags.b0_proc', variable=subflag64)
                c64.grid(row=6, column=6, padx=5, pady=5)

            if flag6.get()==True:
                global subflag65
                subflag65=BooleanVar()
                c65=Checkbutton(toplevel, text='flags.bet_b0', variable=subflag65)
                c65.grid(row=7, column=6, padx=5, pady=5)

            if flag6.get()==True:
                global subflag66
                subflag66=BooleanVar()
                c66=Checkbutton(toplevel, text='flags.bvec_corr', variable=subflag66)
                c66.grid(row=8, column=6, padx=5, pady=5)

            if flag6.get()==True:
                global subflag67
                subflag67=BooleanVar()
                c67=Checkbutton(toplevel, text='flags.run_ecc', variable=subflag67)
                c67.grid(row=9, column=6, padx=5, pady=5)

            if flag6.get()==True:
                global subflag68
                subflag68=BooleanVar()
                c68=Checkbutton(toplevel, text='flags.reg2T1', variable=subflag68)
                c68.grid(row=10, column=6, padx=5, pady=5)

            if flag6.get()==True:
                global subflag69
                subflag69=BooleanVar()
                c69=Checkbutton(toplevel, text='flags.tissueMasks', variable=subflag69)
                c69.grid(row=11, column=6, padx=5, pady=5)

            if flag6.get()==True:
                global subflag610
                subflag610=BooleanVar()
                c610=Checkbutton(toplevel, text='flags.runCamino', variable=subflag610)
                c610.grid(row=12, column=6, padx=5, pady=5)

            if flag6.get()==True:
                global subflag611
                subflag611=BooleanVar()
                c611=Checkbutton(toplevel, text='flags.createFiberFiles', variable=subflag611)
                c611.grid(row=13, column=6, padx=5, pady=5)

            if flag6.get()==True:
                global subflag612
                subflag612=BooleanVar()
                c612=Checkbutton(toplevel, text='flags.genMatrices', variable=subflag612)
                c612.grid(row=14, column=6, padx=5, pady=5)

                           
        ttk.Button(self.frame_ending, text='Choose sub-flags', command=lambda: reply(self)).grid(row=9, column=1, padx=5, pady=5)
        
        ttk.Button(self.frame_ending, text='Set flags', command=lambda: printcheckbutton1(self)).grid(row=9, column=2, padx=5, pady=5)
        ttk.Button(self.frame_ending, text='Generate Script', command=lambda: genscript(self)).grid(row=9, column=3, padx=5, pady=5)
        
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
        global value
        value=self.listbox_initlist.get(selected[0])
        self.listbox_finlist.insert(tkinter.END, value)

def printcheckbutton1(self):

#### Setting up the Main Flags ####
        global flag1
        F1=flag1.get()
        global flag1set
        if F1==True:
            flag1set='flag_T1_prepare_A=1;'
        elif F1==False:
            flag1set='flag_T1_prepare_A=0;'
      
        global flag2
        F2=flag2.get()
        global flag2set
        if F2==True:
            flag2set='flag_T1_prepare_B=1;'
        elif F2==False:
            flag2set='flag_T1_prepare_B=0;'
           
        global flag3
        F3=flag3.get()
        global flag3set
        if F3==True:
            flag3set='flag_PASL=1;'
        elif F3==False:
            flag3set='flag_PASL=0;'
            
        global flag4
        F4=flag4.get()
        global flag4set
        if F4==True:
            flag4set='flag_fMRI_A=1;'
        elif F4==False:
            flag4set='flag_fMRI_A=0;'
          
        global flag5
        F5=flag5.get()
        global flag5set
        if F5==True:
            flag5set='flag_fMRI_B=1;'
        elif F5==False:
            flag5set='flag_fMRI_B=0;'

        global flag6
        F6=flag6.get()
        global flag6set
        if F6==True:
            flag6set='flag_DWI=1;'
        elif F6==False:
            flag6set='flag_DWI=0;'

#### Setting up the Sub Flags ----> flag_T1_prepare_A==1 ####
        global subflag11
        SF11=subflag11.get()
        global subflag11set
        if SF11==True:
            subflag11set='flags.T1.dcm2nii=1;'
        elif SF11==False:
            subflag11set='flags.T1.dcm2nii=0;'

        global subflag12
        SF12=subflag12.get()
        global subflag12set
        if SF12==True:
            subflag12set='flags.T1.anat=1;'
        elif SF12==False:
            subflag12set='flags.T1.anat=0;'

        global subflag13
        SF13=subflag13.get()
        global subflag13set
        if SF13==True:
            subflag13set='flags.T1.denoiser=1;'
        elif SF13==False:
            subflag13set='flags.T1.denoiser=0;'

        global subflag14
        SF14=subflag14.get()
        global subflag14set
        if SF14==True:
            subflag14set='flags.T1.bet=1;'
        elif SF14==False:
            subflag14set='flags.T1.bet=0;'

        global subflag15
        SF15=subflag15.get()
        global subflag15set
        if SF15==True:
            subflag15set='flags.T1.brain=1;'
        elif SF15==False:
            subflag15set='flags.T1.brain=0;'

#### Setting up the Sub Flags ----> flag_T1_prepare_B==1 ####
        global subflag21
        SF21=subflag21.get()
        global subflag21set
        if SF21==True:
            subflag21set='flags.T1.reg2MNI=1;'
        elif SF21==False:
            subflag21set='flags.T1.reg2MNI=0;'

        global subflag22
        SF22=subflag22.get()
        global subflag22set
        if SF22==True:
            subflag22set='flags.T1.seg=1;'
        elif SF22==False:
            subflag22set='flags.T1.seg=0;'

#### Setting up the Sub Flags ----> flag_PASL==1 ####
        global subflag31
        SF31=subflag31.get()
        global subflag31set
        if SF31==True:
            subflag31set='flags.RegT1=1;'
        elif SF31==False:
            subflag31set='flags.RegT1=0;'

        global subflag32
        SF32=subflag32.get()
        global subflag32set
        if SF32==True:
            subflag32set='flags.RegOthers=1;'
        elif SF32==False:
            subflag32set='flags.RegOthers=0;'

        global subflag33
        SF33=subflag33.get()
        global subflag33set
        if SF33==True:
            subflag33set='flags.TissueMasks=1;'
        elif SF33==False:
            subflag33set='flags.TissueMasks=0;'

        global subflag34
        SF34=subflag34.get()
        global subflag34set
        if SF34==True:
            subflag34set='flags.CBFrange=1;'
        elif SF34==False:
            subflag34set='flags.CBFrange=0;'

        global subflag35
        SF35=subflag35.get()
        global subflag35set
        if SF35==True:
            subflag35set='flags.SpatialSmooth=1;'
        elif SF35==False:
            subflag35set='flags.SpatialSmooth=0;'

        global subflag36
        SF36=subflag36.get()
        global subflag36set
        if SF36==True:
            subflag36set='flags.ROIs=1;'
        elif SF36==False:
            subflag36set='flags.ROIs=0;'

        global subflag37
        SF37=subflag37.get()
        global subflag37set
        if SF37==True:
            subflag37set='flags.CBF2MNI=1;'
        elif SF37==False:
            subflag37set='flags.CBF2MNI=0;'

#### Setting up the Sub Flags ----> flag_fMRI_A===1 ####
        global subflag41
        SF41=subflag41.get()
        global subflag41set
        if SF41==True:
            subflag41set='flags.dcm2nii=1;'
        elif SF41==False:
            subflag41set='flags.dcm2nii=0;'

        global subflag42
        SF42=subflag42.get()
        global subflag42set
        if SF42==True:
            subflag42set='flags.SliceTimingCorr=1;'
        elif SF42==False:
            subflag42set='flags.SliceTimingCorr=0;'

        global subflag43
        SF43=subflag43.get()
        global subflag43set
        if SF43==True:
            subflag43set='flags.MotionCorr=1;'
        elif SF43==False:
            subflag43set='flags.MotionCorr=0;'

        global subflag44
        SF44=subflag44.get()
        global subflag44set
        if SF44==True:
            subflag44set='flags.RegT1=1;'
        elif SF44==False:
            subflag44set='flags.RegT1=0;'

        global subflag45
        SF45=subflag45.get()
        global subflag45set
        if SF45==True:
            subflag45set='flags.RegOthers=1;'
        elif SF45==False:
            subflag45set='flags.RegOthers=0;'

        global subflag46
        SF46=subflag46.get()
        global subflag46set
        if SF46==True:
            subflag46set='flags.Mode1000=1;'
        elif SF46==False:
            subflag46set='flags.Mode1000=0;'

        global subflag47
        SF47=subflag47.get()
        global subflag47set
        if SF47==True:
            subflag47set='flags.DemeanDetrend=1;'
        elif SF47==False:
            subflag47set='flags.DemeanDetrend=0;'

        global subflag48
        SF48=subflag48.get()
        global subflag48set
        if SF48==True:
            subflag48set='flags.MotionRegressors=1;'
        elif SF48==False:
            subflag48set='flags.MotionRegressors=0;'

        global subflag49
        SF49=subflag49.get()
        global subflag49set
        if SF49==True:
            subflag49set='flags.BandPass=1;'
        elif SF49==False:
            subflag49set='flags.BandPass=0;'

        global subflag410
        SF410=subflag410.get()
        global subflag410set
        if SF410==True:
            subflag410set='flags.TissueRegressors=1;'
        elif SF410==False:
            subflag410set='flags.TissueRegressors=0;'

        global subflag411
        SF411=subflag411.get()
        global subflag411set
        if SF411==True:
            subflag411set='flags.SpatialSmooth=1;'
        elif SF411==False:
            subflag411set='flags.SpatialSmooth=0;'

        global subflag412
        SF412=subflag412.get()
        global subflag412set
        if SF412==True:
            subflag412set='flags.ROIs=1;'
        elif SF412==False:
            subflag412set='flags.ROIs=0;'

#### Setting up the Sub Flags ----> flag_fMRI_B===1 ####
        global subflag51
        SF51=subflag51.get()
        global subflag51set
        if SF51==True:
            subflag51set='flags.FigsMotion=1;'
        elif SF51==False:
            subflag51set='flags.FigsMotion=0;'

        global subflag52
        SF52=subflag52.get()
        global subflag52set
        if SF52==True:
            subflag52set='flags.FigsFC=1;'
        elif SF52==False:
            subflag52set='flags.FigsFC=0;'

        global subflag53
        SF53=subflag53.get()
        global subflag53set
        if SF53==True:
            subflag53set='flags.SaveFigs=1;'
        elif SF53==False:
            subflag53set='flags.SaveFigs=0;'

        global subflag54
        SF54=subflag54.get()
        global subflag54set
        if SF54==True:
            subflag54set='flags.SaveMats=1;'
        elif SF54==False:
            subflag54set='flags.SaveMats=0;'

#### Setting up the Sub Flags ----> flag_DWI===1 ####
        global subflag61
        SF61=subflag61.get()
        global subflag61set
        if SF61==True:
            subflag61set='flags.dcm2nii=1;'
        elif SF61==False:
            subflag61set='flags.dcm2nii=0;'

        global subflag62
        SF62=subflag62.get()
        global subflag62set
        if SF62==True:
            subflag62set='flags.order_filter=1;'
        elif SF62==False:
            subflag62set='flags.order_filter=0;'

        global subflag63
        SF63=subflag63.get()
        global subflag63set
        if SF63==True:
            subflag63set='flags.denoiser=1;'
        elif SF63==False:
            subflag63set='flags.denoiser=0;'

        global subflag64
        SF64=subflag64.get()
        global subflag64set
        if SF64==True:
            subflag64set='flags.b0_proc=1;'
        elif SF64==False:
            subflag64set='flags.b0_proc=0;'

        global subflag65
        SF65=subflag65.get()
        global subflag65set
        if SF65==True:
            subflag65set='flags.bet_b0=1;'
        elif SF65==False:
            subflag65set='flags.bet_b0=0;'

        global subflag66
        SF66=subflag66.get()
        global subflag66set
        if SF66==True:
            subflag66set='flags.bvec_corr=1;'
        elif SF66==False:
            subflag66set='flags.bvec_corr=0;'

        global subflag67
        SF67=subflag67.get()
        global subflag67set
        if SF67==True:
            subflag67set='flags.run_ecc=1;'
        elif SF67==False:
            subflag67set='flags.run_ecc=0;'

        global subflag68
        SF68=subflag68.get()
        global subflag68set
        if SF68==True:
            subflag68set='flags.reg2T1=1;'
        elif SF68==False:
            subflag68set='flags.reg2T1=0;'

        global subflag69
        SF69=subflag69.get()
        global subflag69set
        if SF69==True:
            subflag69set='flags.tissueMaska=1;'
        elif SF69==False:
            subflag69set='flags.tissueMasks=0;'

        global subflag610
        SF610=subflag610.get()
        global subflag610set
        if SF610==True:
            subflag610set='flags.runCamino=1;'
        elif SF610==False:
            subflag610set='flags.runCamino=0;'

        global subflag611
        SF611=subflag611.get()
        global subflag611set
        if SF611==True:
            subflag611set='flags.createFiberFiles=1;'
        elif SF611==False:
            subflag611set='flags.createFiberFiles=0;'

        global subflag612
        SF612=subflag612.get()
        global subflag612set
        if SF612==True:
            subflag612set='flags.genMatrices=1;'
        elif SF612==False:
            subflag612set='flags.genMatrices=0;'
        
            return (flag1set,flag2set,flag3set,flag4set,flag5set,flag6set,subflag11set,subflag12set,subflag13set,subflag14set,subflag15set,subflag21set,subflag22set,subflag31set,subflag32set,subflag33set,subflag34set,subflag35set,subflag36set,subflag37set,subflag41set,subflag42set,subflag43set,subflag44set,subflag45set,subflag46set,subflag47set,subflag48set,subflag49set,subflag410set,subflag411set,subflag412set,subflag51set,subflag52set,subflag53set,subflag54set,subflag61set,subflag62set,subflag63set,subflag64set,subflag65set,subflag66set,subflag67set,subflag68set,subflag69set,subflag610set,subflag611set,subflag612set)
    
def genscript(self):
       global temp_list
       temp_list=list(self.listbox_finlist.get(0,END))
        
       file=open("/home/pkgandhi/GUI_testing/xml2struct.m","w")
       file.write("close all; \n")
       file.write("clear all; \n")
       file.write("clc; \n")
       file.write("%use system instead of bundled LD_LIBRARY_PATH; \n")
       file.write("setenv('LD_LIBRARY_PATH',''); \n\n")
       file.write("% general path to scripts; \n")
       file.write("path2scripts = '/usr/local/connectome_scripts/'; \n")
       file.write("addpath(path2scripts); \n")
       file.write("% path to use MRIread MRIwrite; \n")
       file.write("addpath('/usr/local/nifti_toolbox');; \n")
       file.write("% path to templates in MNI; \n")
       file.write("path2MNIparcs = '/usr/local/connectome_scripts/templates/MNIparcs'; \n")
       file.write("% path to FSL installation; \n")
       file.write("path2FSL = '/usr/local/fsl/bin'; \n")
       file.write("%FSL setup; \n")
       file.write("FSLsetup = 'FSLDIR=/usr/local/fsl; . ${FSLDIR}/etc/fslconf/fsl.sh; PATH=${FSLDIR}/bin:${PATH}; export FSLDIR PATH'; \n")
       file.write("% Path to AFNI \n")
       file.write("path2AFNI = '/usr/local/AFNI/bin/'; \n\n\n")
       file.write("path2data = fullfile(pwd,'..','subjects'); \n")
       file.write("%subjectList =dir(path2data); \n")
       file.write("%subjectList(1:2)=[]; %remove '.' and '..' \n\n")
       for idx,val in enumerate(temp_list):
           file.write("subjectList({})=struct('name','{}');".format(idx+1,val)+"\n")
       file.write(flag1set+"\n")
       file.write(flag2set+"\n")
       file.write(flag3set+'\n')
       file.write(flag4set+'\n')
       file.write(flag5set+'\n')
       file.write("\t configs.epiFolder='fMRI'; \n")
       file.write("\t configs.dcmFolder='DICOMS'; \n")
       file.write(flag6set+'\n\n')
       file.write("%% T1_prepare_A \n")
       file.write("if (flag_T1_prepare_A==1) \n")
       file.write("\t % path to T1 denoiser \n")
       file.write("\t addpath(genpath('/usr/local/connectome_scripts/MRIDenoisingPackage')); \n")
       file.write("\t"+subflag11set+'\n')
       file.write("\t"+subflag12set+'\n')
       file.write("\t"+subflag13set+'\n')
       file.write("\t"+subflag14set+'\n')
       file.write("\t"+subflag15set+'\n')
       
       file.write("\t %workers = parpool('local'); \n")
       file.write("\t for i=1:length(subjectList) \n")
       file.write("\t\t path2subject = fullfile(path2data,subjectList(i).name); \n")
       file.write("\t\t if exist(path2subject,'dir') & ~isempty(strfind(path2subject,'GPT')) \n")
       file.write("\t\t\t %% T1 preparations \n")
       file.write("\t\t\t path2T1 = fullfile(path2subject,'T1'); \n")
       file.write("\t\t\t\t disp('----------') \n")
       file.write("\t\t\t\t disp(subjectList(i).name) \n")
       file.write("\t\t\t\t disp('----------') \n")
       file.write("\t\t\t\t f_T1_prepare_A(path2T1,flags,path2FSL,FSLsetup,path2scripts,''); \n")
       file.write("\t\t\t end \n")
       file.write("\t\t end \n")
       file.write("\t end \n")
       file.write("\t %delete(workers); \n")
       file.write("end\n\n")

       file.write("%% T1 prepare B \n")
       file.write("if (flag_T1_prepare_B==1) \n")
       file.write("\t"+subflag21set+"\n")
       file.write("\t"+subflag22set+"\n")
       file.write("\t %workers = parpool('local'); \n")
       file.write("\t for i=1:length(subjectList) \n")
       file.write("\t\t sprintf('T1_prepare_B on %s',subjectList(i).name) \n")
       file.write("\t\t path2subject = fullfile(path2data,subjectList(i).name); \n")
       file.write("\t\t if exist(path2subject,'dir') & ~isempty(strfind(subjectList(i).name,'GPT')) \n")
       file.write("\t\t\t path2T1 = fullfile(path2subject,'T1'); \n")
       file.write("\t\t\t f_T1_prepare_B(path2T1,flags,path2FSL,FSLsetup,path2MNIparcs); \n")
       file.write("\t\t end\n")
       file.write("\t end\n")
       file.write("\t %delete(workers) \n")
       file.write("end\n")
       file.write("\n")

       file.write(" if flag_PASL==1\n")
       file.write("\t jscanmin=1;\n")
       file.write("\t jscanmax=1;\n")
       file.write("\t configs.epitype='CBF';\n")
       file.write("\t configs.dcmFolder='NONE';\n")
       file.write("% flags\n")
       file.write("\t"+subflag31set+"\n")
       file.write("\t"+subflag32set+"\n")
       file.write("\t\tconfigs.GMprobthr=0.15; % threshold the GMprobability image\n")
       file.write("\t"+subflag33set+"\n")
       file.write("\t"+subflag34set+"\n")
       file.write("\t\tconfigs.CBFmin = 5;     % lowest reasonable rCBF value\n")
       file.write("\t\tconfigs.CBFmax = 180;   % highest reasonable rCBF value\n")
       file.write("\t"+subflag35set+"\n")
       file.write("\t\tconfigs.fhwm = 0;% Full Width at Half Maximum of the Gaussian kernel\n")
       file.write("\t"+subflag36set+"\n")
       file.write("\t"+subflag37set+"\n")


       file.write("\t %workers=parpool('local');\n")
       file.write("\t for i=1:length(subjectlist)\n")
       file.write("\t\t path2subject=fillfile(path2data,subjectList(i).name);\n")
       file.write("\t\t for j=jscanmin:jscanmax\n")
       file.write("\t\t\t if exist(path2subject,'dir') & ~isempty(strfind(subjectList(i).name,'GPT')) & exist(fullfile(path2subject,'T1'),'dir')\n")
       file.write("\t\t\t\t configs.epiFolder = strcat(configs.epitype,num2str(j));\n")
       file.write("\t\t\t\t disp('------------------')\n")
       file.write("\t\t\t\t sentence = strcat(subjectList(i).name,',',configs.epiFolder);\n")
       file.write("\t\t\t\t disp(sentence)\n")
       file.write("\t\t\t\t disp('------------------')\n")
       file.write("\t\t\t\t fileIn = fullfile(path2data,subjectList(1).name,configs.epiFolder,'0_rCBF.nii.gz');\n")
       file.write("\t\t\t\t if exist(fileIn,'file')\n")
       file.write("\t\t\t\t\t path2rest = fullfile(path2data,subjectList(i).name,configs.epiFolder);\n")
       file.write("\t\t\t\t\t f_prepare_rCBF(path2subject,flags,configs,params,path2FSL,FSLsetup,path2AFNI,path2MNIparcs);\n")
       file.write("\t\t\t\t else\n")
       file.write("\t\t\t\t\t warning('File %s',fullfile(path2rest,'0_rCBF.nii.gz'),'does not exist. Skipping further analysis')\n")
       file.write("\t\t\t\t end\n")
       file.write("\t\t\t end\n")
       file.write("\t\t end\n")
       file.write("\t end\n")
       file.write("end\n")
#### ----flag_fMRI_A Part---- ####
       file.write("if flag_fMRI_A==1\n")
       file.write("%% fMRI processing\n\n")
       file.write("\t %%flags\n")
       file.write("%     first and last EPI to process\n")
       file.write("\tjscanmin=1;\n")
       file.write("\tjscanmax=1;\n")
       file.write("%     configs.epiFolder = 'REST1'; %now set within the scan loop\n")
       file.write("%     functional scan folder: generic (EPI), or specific (TASK, REST,...)\n")
       file.write("\tconfigs.epitype = 'EPI';\n")
       file.write("\tconfigs.dcmFolder = 'DICOMS';\n")
       file.write("\tconfigs.dilate_scrubbing = 1;\n")
       file.write("\t%% flags\n")
       file.write("\t"+subflag41set+"\n")
       file.write("\t"+subflag42set+"\n") 
       file.write("\t"+subflag43set+"\n")
       file.write("\t"+subflag44set+"\n")
       file.write("\t"+subflag45set+"\n")
       file.write("\t\tconfigs.GMprobthr = 0.25; % threshold the GM probability image\n")
       file.write("\t"+subflag46set+"\n")
       file.write("\t"+subflag47set+"\n") 
       file.write("\t"+subflag48set+"\n")
       file.write("\t\t%configs.FDthreshold = 0.4;\n")
       file.write("\t\tconfigs.DVARSth = 55; %30;\n")
       file.write("\t\tconfigs.SDth = [];\n")
       file.write("\t\tconfigs.FDth = 0.40; %0.26\n")
       file.write("\t"+subflag49set+"\n")
       file.write("\t\tconfigs.fMin = .009;\n")
       file.write("\t\tconfigs.fMax = .08;\n")
       file.write("\t"+subflag410set+"\n")
       file.write("\t\tconfigs.numCompsPCA = 5;\n")
       file.write("\t"+subflag411set+"\n")
       file.write("\t\tconfigs.fhwm = 0;\n")
       file.write("\t"+subflag412set+"\n")
       file.write("\t%% params(now inside the scan loop)\n")
       file.write("\tparams=[];\n")
       file.write("%     params.TR=2.25; %1.20; %2.10\n")
       file.write("%     params.nvols = 161;\n")
       file.write("%     params.nvols = 125;\n")
       file.write("\t%workers = parpool('local');\n")
       file.write("\tfor i=1:length(subjectList)\n")
       file.write("\t\t\tif exist(path2subject,'dir') & ~isempty(strfind(subjectList(i).name,'GPT')) & exist(fullfile(path2subject,'T1'),'dir')\n")
       file.write("\t\t\t\tconfigs.epiFolder = strcat(configs.epitype,num2str(j));\n")
       file.write("\t\t\t\tdisp('------------------')\n")
       file.write("\t\t\t\tsentence = strcat(subjectList(i).name,',',configs.epiFolder);\n")
       file.write("\t\t\t\tdisp(sentence)\n")
       file.write("\t\t\t\tdisp('------------------')\n")
       file.write("\t\t\t\tfileIn = fullfile(path2data,subjectList(1).name,configs.epiFolder,'0_rCBF.nii.gz');\n")
       file.write("\t\t\t\t%                 if exist(fileIn,'file')n")
       file.write("\t\t\t\t%                     sentence = sprintf('%s;%s/fslval %s pixdim4',FSLsetup,path2FSL,fileIn);\n")
       file.write("\t\t\t\t%                     [status,result] = system(sentence);\n")
       file.write("\t\t\t\t%                     params.TR = str2double(result);\n")
       file.write("\t\t\t\t%                     sentence = sprintf('%s;%s/fslval %s dim4',FSLsetup,path2FSL,fileIn);\n")
       file.write("\t\t\t\t%                     [status,result] = system(sentence);\n")
       file.write("\t\t\t\t%                     params.nvols = str2double(result);\n")
       file.write("\t\t\t\t%                 else\n")
       file.write("\t\t\t\t%                     params.TR = 0.000;\n")
       file.write("\t\t\t\t%                     params.nvols = 0;\n")
       file.write("\t\t\t\t%                 end\n")
       file.write("\t\t\t\tif exist(fileIn,'file')\n")
       file.write("\t\t\t\t\tpath2rest = fullfile(path2data,subjectList(i).name,configs.epiFolder);\n")
       file.write("\t\t\t\t\tf_functional_connectivity(path2subject,flags,configs,params,path2FSL,FSLsetup,path2AFNI);\n")
       file.write("\t\t\t\telse\n")
       file.write("\t\t\t\t\twarning('File %s',fullfile(path2rest,'0_rCBF.nii.gz'),'does not exist. Skipping further analysis')\n")
       file.write("\t\t\t\tend\n")
       file.write("\t\t\tend\n")
       file.write("\t\tend\n")
       file.write("\tend\n")
       file.write("%delete(workers);\n")
#### -------flag_fMRI_B Part----- #####
       file.write("%% FC matrices and figures\n")
       file.write("if flag_fMRI_B==1\n")
       file.write("%     first and last EPI to process\n")
       file.write("\tjscanmin = 1;\n")
       file.write("\tjscanmax = 6;end\n")
       file.write("\tconfigs.epitype='EPI';\n")
       file.write("%     params.TR=2.25 %&1.20 %2.10\n")
       file.write("%    params.nvols = 161;\n")
       file.write("%    params.nvols = 125;\n")
       file.write("%    params.dilate_scrubbing = 1;\n")
       file.write("\tnumBars=40;\n")
       file.write("%     dropTRs = ceil(15/params.TR);\n")
       file.write("%     fileIn = fullfile(path2data,subjectList(1).name,configs.epiFolder,'0_rest.nii.gz');\n")
       file.write("%     sentence = sprintf('%s;%s/fslval %s dim4',FSLsetup,path2FSL,fileIn);\n")
       file.write("%     [status,result] = system(sentence);\n")
       file.write("%     params.nvols = str2double(result);\n")
       file.write("%     TR.init = dropTRs+1;\n")
       file.write("% %    if strcmp(configs.epiFolder,'REST1') || strcmp(configs.epiFolder,'REST2')\n")
       file.write("%         TR.end = params.nvols -dropTRs;\n")
       file.write("% %    elseif strcmp(configs.epiFolder,'REST3')\n")
       file.write("% %        TR.end = floor(params.nvols*1/3);\n")
       file.write("% %    end\n\n")
       file.write("\tstep = 1;\n")
       file.write("\t%%flags\n")
       file.write("\t"+subflag51set+"\n")
       file.write("\t"+subflag52set+"\n")
       file.write("\t"+subflag53set+"\n")
       file.write("\t"+subflag54set+"\n")
       file.write("\t%%params\n")
       file.write("\tparams.minVoxelsROI = 8;\n")
       file.write("\tparams.dilate_scrubbing = 1;\n\n")
       file.write("\tfor i=1:length(subjectList)\n")
       file.write("\t\tpath2subject = fullfile(path2data,subjectList(i).name);\n")
       file.write("\t\tfor j=jscanmin:jscanmax\n")
       file.write("\t\t\tif exist(fullfile(path2subject),'dir') && ~isempty(strfind(path2subject,'GPT'))\n")
       file.write("\t\t\t\tconfigs.epiFolder = strcat(configs.epitype,num2str(j));\n")
       file.write("\t\t\t\tfileIn = fullfile(path2data,subjectList(1).name,configs.epiFolder,'0_epi.nii.gz');\n")
       file.write("\t\t\t\tsentence = sprintf('%s;%s/fslval %s pixdim4',FSLsetup,path2FSL,fileIn);\n")
       file.write("\t\t\t\t[status,result] = system(sentence);\n")
       file.write("\t\t\t\tparams.TR = str2double(result);\n")
       file.write("\t\t\t\tdropTRs = ceil(15/params.TR);\n")
       file.write("\t\t\t\tsentence = sprintf('%s;%s/fslval %s dim4',FSLsetup,path2FSL,fileIn);\n")
       file.write("\t\t\t\t[status,result] = system(sentence);\n")
       file.write("\t\t\t\tparams.nvols = str2double(result);\n")
       file.write("\t\t\t\tTR.init = dropTRs+1;\n")
       file.write("\t\t\t\t%    if strcmp(configs.epiFolder,'REST1') || strcmp(configs.epiFolder,'REST2')\n")
       file.write("\t\t\t\tTR.end = params.nvols -dropTRs;\n")
       file.write("\t\t\t\tpath2rest = fullfile(path2data,subjectList(i).name,configs.epiFolder);\n")
       file.write("\t\t\t\tpath2T1 = fullfile(path2data,subjectList(i).name,'T1');\n")
       file.write("\t\t\t\tsubjectList(i).name\n")
       file.write("\t\t\t\t[PCA0,PCA1,PCA3,PCA5] = f_evaluateFC(path2rest,numBars,TR,step,flags,params,configs,subjectList(i).name);\n")
       file.write("\t\t\t\tclose all;\n")
       file.write("\t\t\tend\n")
       file.write("\t\tend\n")
       file.write("\tend\n")
       file.write("\t%delete(workers);")
       file.write("end\n\n\n")
       file.write("%% DWI Processing\n")
       file.write("if(flag_DWI==1)\n")
       file.write("\t% environment paths\n")
       file.write("%    addCaminoPath = sprintf('PATH=%s:${PATH}',fullfile(path2scripts,'camino-code-d64fe361776a8ee02a41f13e6b180ddd574f8882','bin')); %add Camino path to the system\n")
       file.write("\taddCaminoPath = sprintf('PATH=%s:${PATH}',fullfile('/usr/local/camino','bin')); %add Camino path to the system\n")
       file.write("%    addCaminoTrackVisPath = sprintf('PATH=%s:${PATH}',fullfile(pwd,'camino-trackvis-0.2.8.1','bin')); %add Camino path to the system\n")
       file.write("\taddCaminoTrackVisPath = sprintf('PATH=%s:${PATH}',fullfile('/usr/local/camino-trackvis','bin')); %add Camino path to the system\n")
       file.write("\t% path to DWI denoiser\n")
       file.write("\taddpath(genpath('/usr/local/DWIDenoisingPackage_r01_pcode'));\n\n")
       file.write("\t% tractography parameters\n")
       file.write("\tparams.bMax=1500;\n")
       file.write("\tparams.file_bvec = '0_DWI.bvec';\n")
       file.write("\tparams.file_bval = '0_DWI.bval';\n")
       file.write("\tparams.rician = 0; %should not be changed\n")
       file.write("\tparams.schemeOrientation = [1,1,-1]; %diffusion gradient coordinate sign. This is dataset dependent and should be evaluated. Check at http://cmic.cs.ucl.ac.uk/camino/index.php?n=Tutorials.DTI\n")
       file.write("\tparams.FAthreshold = 0.10; %FA minimum value for fiber-tracking\n")
       file.write("\tparams.order0Threshold = 12;\n")
       file.write("\tparams.order2Threshold = 6;\n")
       file.write("\tparams.order4Threshold = 6;\n")
       file.write("\tparams.CURVthreshold = 70; %degrees limit on curvature for fibers (very sensitive for short-fibers) [65-90]\n")
       file.write("\tparams.clusterMinSizeMultiTensor = 8; %minimum cluster size so that voxels are modeled with multi-tensor. They go back to single-tensor otherwis\n")
       file.write("\tparams.seedsWMborder = 1;\n")
       file.write("\tparams.clusterMinSizeTissue = 27; %WM minimum cluster size (voxels), otherwise removed.\n")
       file.write("\tparams.stepSize = 1.00; % resolution with respect to voxelsize for fiber-tracking. It is suggested that this is half of voxel-size\n")
       file.write("\tparams.iterations = 1; % seeds per voxel. Do not increase unless doing probabilistic tractography\n")
       file.write("\tparams.LengthMin = 8; %[4-12]\n")
       file.write("\tparams.LengthMax = 180; %[150-200]\n\n")
       file.write("\t%% flags\n")


       file.write("\t%matlabpool open 4;\n")
       file.write("\t%parfor i=1:length(subjectList)\n")
       file.write("\tfor i=1:length(subjectList)\n")
       file.write("\t\tpath2subject = fullfile(path2data,subjectList(i).name);\n")
       file.write("\t\tpaths.T1 = fullfile(path2subject,'T1');\n")
       file.write("\t\tpaths.DWI = fullfile(path2subject,'DTI');\n")
       file.write("\t\tparams.subjName = subjectList(i).name;\n")
       file.write("\t\tsentence = sprintf('cp %s %s',fullfile(paths.DWI,'DTI.bval'),fullfile(paths.DWI,'0_DWI.bval'));\n")
       file.write("\t\t[status,result] = system(sentence);\n")
       file.write("\t\tsentence = sprintf('cp %s %s',fullfile(paths.DWI,'DTI.bvec'),fullfile(paths.DWI,'0_DWI.bvec'));\n")
       file.write("\t\t[status,result] = system(sentence);\n")
       file.write("\t\tsentence = sprintf('cp %s %s',fullfile(paths.DWI,'DTI.nii.gz'),fullfile(paths.DWI,'0_DWI.nii.gz'));\n")
       file.write("\t\t[status,result] = system(sentence);\n")
       file.write("\t\tf_structural_connectivity(paths,flags,params,FSLsetup,path2FSL,addCaminoPath,addCaminoTrackVisPath);\n")
       file.write("\tend\n")
       file.write("\t%matlabpool close;\n")
       file.write("end\n")
       
       file.close()

def main():
        root=Tk()
        feedback=Feedback(root)
        root.mainloop()

if __name__ == "__main__": main()
