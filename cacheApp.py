import tkinter as tk
from tkinter import ttk
import tkinter.font as tkFont
from PIL import ImageTk, Image
import os, shutil, sys
import math

class Viewport(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('Clean Drive')
        self.geometry('410x500')
#         self.resizable(False, False)
        self.themainframe = ttk.Frame(self)
        self.themainframe.grid(row=0,column=0)
        thefirstFrame = Firstframe(self.themainframe)
        thefirstFrame.grid(column=0, row=0, padx=20, pady=10)
        thefirstFrame.columnconfigure(0, weight=1)
        thefirstFrame.rowconfigure(0,weight=1)
        
class Firstframe(ttk.Frame):
    def __init__(self, parent):
        super().__init__()
        
#       stringvar sections  
        self.cacheVariable = tk.StringVar()
        self.cachefilessizeVariable = tk.StringVar()
        self.cachefilessizeVariable.set('0 GB')
        self.logfilesVariable = tk.StringVar()
        self.trashVariable = tk.StringVar()
        self.mailcacheVariable = tk.StringVar()
        self.browserVariable = tk.StringVar() 
        self.mobileappsVariable = tk.StringVar() 
        self.itunestempVariable = tk.StringVar()
        self.oldupdatesVariable = tk.StringVar()
        self.calculatedSizeVariable = tk.StringVar()
        self.calculatedSizeVariable.set('0 GB')
        self.popUpwindowFileSize = tk.StringVar()
        self.popUpwindowFileSize.set('up 0 GB of disk space on your Mac.')
#       ----------------------------------------------------------------------------------- 
        
        
#       calling methods
        self.__getcachefoldersize()
#         self.displayCacheFileSize()
#         self.convertfoldersize(self.getcachefoldersize())
#       ----------------------------------------------------------------------------------- 
        
        
#       tkinter widgets section
        self.style = ttk.Style()
        self.style.configure('Blue.TLabel',foreground='blue')
        
        self.myFont = tkFont.Font(family="TkDefaultFont", size=30, weight="bold")
        self.myFont2 = tkFont.Font(family="TkDefaultFont", size=6)
        
        self.closeAppButton = ttk.Button(self, text='close')
        self.closeAppButton.grid(row=0, column=0, sticky='NW', padx=(0,5))
        
        self.cleanDrive = ttk.Label(self, text='Clean Drive')
        self.cleanDrive.grid(row=0, column=1, padx=10)
        
        self.appSettingsButton = ttk.Button(self, text='settings')
        self.appSettingsButton.grid(row=0, column=2, sticky='NE', padx=(5,0))
        
        self.calculatedSize = ttk.Label(self, text='0.69 GB', font=self.myFont, textvariable=self.calculatedSizeVariable)
        self.calculatedSize.grid(row=1,column=1,pady=(20,5))
        
        self.ready = ttk.Label(self, text='Ready for Cleanup')
        self.ready.grid(row=2, column=1, pady=(0, 10))
        
        self.logfilesV = ttk.Checkbutton(self, text='Log files', onvalue='On', offvalue='Off',variable=self.logfilesVariable)
        self.logfilesV.grid(row=3, column=0, sticky='W', pady=(0,5))
        
        self.logfilesSize = ttk.Label(self, text='0 GB')
        self.logfilesSize.grid(row=3, column=2, sticky='E')
        
        self.cachefilesV = ttk.Checkbutton(self, text='Cache files', onvalue='On', offvalue='Off', variable=self.cacheVariable, command=self.__displayCacheFileSize)
        self.cachefilesV.grid(row=4, column=0, sticky='W',pady=(0,5))
        
        self.cachefilesSize = ttk.Label(self, text='0 GB', textvariable=self.cachefilessizeVariable)
        self.cachefilesSize.grid(row=4, column=2, sticky='E')
        
        self.trashfilesV = ttk.Checkbutton(self, text='Trash files', onvalue='On', offvalue='Off', variable=self.trashVariable)
        self.trashfilesV.grid(row=5, column=0, sticky='W',pady=(0,5))
        
        self.trashfilesSize = ttk.Label(self, text='0 GB')
        self.trashfilesSize.grid(row=5, column=2, sticky='E')
        
        self.mailcacheV = ttk.Checkbutton(self, text='Mail cache', onvalue='On', offvalue='Off', variable=self.mailcacheVariable)
        self.mailcacheV.grid(row=5, column=0, sticky='W',pady=(0,5))
        
        self.mailcacheSize = ttk.Label(self, text='0 GB')
        self.mailcacheSize.grid(row=5, column=2, sticky='E')
        
        self.browserDataV = ttk.Checkbutton(self, text='Browser Data', onvalue='On', offvalue='Off', variable=self.browserVariable)
        self.browserDataV.grid(row=6, column=0, sticky='W',pady=(0,5))
        
        self.browserDataSize = ttk.Label(self, text='0 GB')
        self.browserDataSize.grid(row=6, column=2, sticky='E')
        
        self.mobileapps = ttk.Checkbutton(self, text='Mobile apps', onvalue='On', offvalue='Off', variable=self.mobileappsVariable)
        self.mobileapps.grid(row=7, column=0, sticky='W',pady=(0,5))
        
        self.mobileappsSize = ttk.Label(self, text='0 GB')
        self.mobileappsSize.grid(row=7, column=2, sticky='E')
        
        self.itunesTempFiles = ttk.Checkbutton(self, text='iTunes temp files', onvalue='On', offvalue='Off', variable=self.itunestempVariable)
        self.itunesTempFiles.grid(row=8, column=0, sticky='W',pady=(0,5))
        
        self.itunesTempFilesSize = ttk.Label(self, text='0 GB')
        self.itunesTempFilesSize.grid(row=8, column=2, sticky='E')
        
        self.oldupdates = ttk.Checkbutton(self, text='Old Updates', onvalue='On', offvalue='Off', variable=self.oldupdatesVariable)
        self.oldupdates.grid(row=9, column=0, sticky='W',pady=(0,5))
        
        self.oldupdatesSize = ttk.Label(self, text='0 GB')
        self.oldupdatesSize.grid(row=9, column=2, sticky='E',pady=(0,10))
        
        self.cleanUpButton = ttk.Button(self, text='Clean Up', command=self.popupWindow)
        self.cleanUpButton.grid(row=10, column=1, pady=(0,5))
        
        self.showLargeFiles = ttk.Label(self, text='Show Large Files...')
        self.showLargeFiles.grid(row=11,column=1, pady=(0, 20))
        self.showLargeFiles.configure(style='Blue.TLabel', underline=True)
        
        self.logoimage = ImageTk.PhotoImage(Image.open("mad-man.jpg"))
        self.logoLabelImage = ttk.Label(self, image=self.logoimage)
        self.logoLabelImage.grid(row=12,column=1,pady=(0,50))
        
        self.builder = ttk.Label(self, text='This app was built with tkinter in python', font=self.myFont2)
        self.builder.grid(row=13, column=1)
        
#       ----------------------------------------------------------------------------------- 

#   gets Caches directory in mac
    def __getLibrarydirMacos(self):
        thehome = os.environ.get('HOME')
        newpath = os.path.join(thehome, 'Library/Caches')
        return newpath

#   calculates all files and directory in Caches folder and returns the total    
    def __getFolderLibrarySizeMacos(self, path):
        total = 0
        for items in os.scandir(path):
            if items.is_dir():
                total += self.__getFolderLibrarySizeMacos(items.path)
            else:
                total += os.path.getsize(items)
        return total

#   checks which platform the sys is whether mac or windows and returns the path to the cache          
    def __getcachefoldersize(self):
        if sys.platform == 'darwin':
            return self.__getLibrarydirMacos()

#   calculator to convert the size of the cache to b, kb, mb, or gb        
    def __convertfoldersize(self, folder):
        thefolder = self.__getFolderLibrarySizeMacos(folder)
        if thefolder < 1000:
            thefolderbytes = f'{thefolder} bytes'
            return thefolderbytes

        elif thefolder >= 1000 and thefolder < 1000000:
            thefolderkb = math.trunc(thefolder / 1000)
            thefolderkbstr = f'{thefolderkb} KB'
            return thefolderkbstr

        elif thefolder >= 1000000 and thefolder < 1000000000:
            thefoldermb = round(thefolder / 1000000, 1)
            thefoldermbstr = f'{thefoldermb} MB'
            return thefoldermbstr

        elif thefolder >= 1000000000 and thefolder < 1000000000000:
            thefoldergb = round(thefolder / 1000000000, 2)
            thefoldergbstr = f'{thefoldergb} GB'
            return thefoldergbstr

    def __displayCacheFileSize(self):
        if (self.cacheVariable.get() == 'On'):
            self.calculatedSizeVariable.set(self.__convertfoldersize(self.__getcachefoldersize()))
            self.cachefilessizeVariable.set(self.__convertfoldersize(self.__getcachefoldersize()))
            thesize = self.__convertfoldersize(self.__getcachefoldersize())
            thesizeText = f'up {thesize} of disk space on your Mac.'
            self.popUpwindowFileSize.set(thesizeText)

        else:
            self.calculatedSizeVariable.set('0 GB')
            self.cachefilessizeVariable.set('0 GB')
            
            
    def popupWindow(self):
        global popvariable
        popvariable = tk.Toplevel()
        
        
        theframe = ttk.Frame(popvariable)
        theframe.grid(row=0, column=0, padx=(20,20), pady=(20,20))
        
        theframe2 = ttk.Frame(popvariable)
        theframe2.grid(row=1, column=0, padx=(20,20))
        
        firstlabel = ttk.Label(theframe, text='Are you sure you want to delete')
        firstlabel.grid(row=0, column=0, pady=(20, 0))
        
        firstlabel2 = ttk.Label(theframe, text='the selected files?')
        firstlabel2.grid(row=1, column=0, pady=(0, 10))
        
        secondlabel = ttk.Label(theframe, text='If you click "Delete", Clean Drive will free')
        secondlabel.grid(row=2, column=0, pady=(0,0))
        
        secondlabel2 = ttk.Label(theframe, textvariable=self.popUpwindowFileSize)
        secondlabel2.grid(row=3, column=0, pady=(0, 20))
        
        cancelButton = ttk.Button(theframe2, text='Cancel', command=self.__destroyPopUpSizeWindow)
        cancelButton.grid(row=0, column=0, padx=(0,10))
        
        deleteButton = ttk.Button(theframe2, text='Delete')
        deleteButton.grid(row=0, column=1, padx=(0,0))

    def __destroyPopUpSizeWindow(self):
      popvariable.destroy()
            
        
            
        
        
root = Viewport()
root.mainloop()