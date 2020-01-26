#!/usr/bin/python3
import os 
filename = "/etc/passwd"
filename1 = "/etc/shadow"
filename2 = "/etc/group"
filename3 = "/etc/gshadow"
filename4 = "/etc/passwd-"
filename5 = "/etc/shadow-"
filename6 = "/etc/group-"
filename7 = "/etc/gshadow-"
mask = oct(os.stat(filename).st_mode)[-3:]  
mask1 = oct(os.stat(filename1).st_mode)[-3:]  
mask2 = oct(os.stat(filename2).st_mode)[-3:]  
mask3 = oct(os.stat(filename3).st_mode)[-3:]  
mask4 = oct(os.stat(filename4).st_mode)[-3:]  
mask5 = oct(os.stat(filename5).st_mode)[-3:]  
mask6 = oct(os.stat(filename6).st_mode)[-3:]  
mask7 = oct(os.stat(filename7).st_mode)[-3:]    
os.chmod('/etc/passwd', 0o600)
os.chmod('/etc/shadow', 0o600)
os.chmod('/etc/group', 0o600)
os.chmod('/etc/gshadow', 0o600)
os.chmod('/etc/passwd-', 0o600)
os.chmod('/etc/shadow-', 0o600)
os.chmod('/etc/group-', 0o600)
os.chmod('/etc/gshadow', 0o600)

