#!/usr/bin/env python3
#imports
import shutil
import os

# Let's force our Python program to 'start' in the home user directory, which for us will be /home/student/mycode/. 
os.chdir("/home/student/mycode/")

# copy a file
shutil.copy("5g_research/sdn_network.txt", "5g_research/sdn_network.txt.copy")



# The following line will create the directory if it does not exist already
# copy a folder
shutil.copytree("5g_research/", "5g_research_backup/")
  
