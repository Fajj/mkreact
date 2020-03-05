#CMD FONT IS VERY SUCK!


from tkinter import *
from tkinter import filedialog
import subprocess

#root = Tk()
#P4TH = filedialog.askdirectory()

#print(f"{P4TH}")
#project = input('Project: ')
project = "Memo"

subprocess.run(['expo', 'init',  project, '--template', 'blank'], shell=True, encoding='utf-8')