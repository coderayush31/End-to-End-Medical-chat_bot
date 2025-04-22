import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')


list_of_files = [
    "src/__init__.py",
    "src/helper.py",
    "src/prompt.py",
    ".env",
    "setup.py",
    "research/trials.ipynb",
    "app.py",
    "store_index.py",
    "static/.gitkeep",
    "templates/chat.html"

]

for filepath in list_of_files:
   filepath = Path(filepath)                                            #so that the issue of operating on different OS is resolved
   filedir, filename = os.path.split(filepath)                          #splits file name and folder name and store them in respective variables 

   if filedir !="":                                                         #if folder is not empty 
      os.makedirs(filedir, exist_ok=True)                                   #To make folder also .makedirs created intermediate folders if needed unlike .mkdir 
      logging.info(f"Creating directory; {filedir} for the file {filename}")#Logs an informational message that we're creating the folder. This helps track in logs when and why a directory was created
                                                                            
   if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):#checks if file doesn't exist or is empty & os.path.getsize(filepath) == 0 → checks if the file on disk is empty
         filepath.touch()                                                # Creates an empty file at the specified path. If the file already exists, it updates its last modified time (but doesn't erase content).   
         logging.info(f"Creating empty file: {filepath}")                #Logs the message: "Creating empty file: yourfilename.txt" at the INFO level.#Useful for debugging or tracking when/why the file was created.
   else:
      logging.info(f"{filename} is already created")
      
      
    