# letmein
Its a python script, when added and used with bootable medium can create backdoor on multiple OS even on multi boot system. Like bootable linux (with pre install python) on usb stick or cd/dvd rom. I personally prefer tahr puppy linux (only around 250mb) written on a usb stick only takes almost 30 seconds to boot. Once the desktop appears it means script has already ran in background.

# How Does It Work
It can create backdoor on Windows xp, 7, 8 (Win 10 yet to be tested) etc and on Linux. It doesn't matter how many and what type of OS (only windows and linux) are installed on target hard disk. To create backdoor you have to access your target pc physically, and the only condition is that the hard drive on target pc should not be encrypted.

This creates backdoor on windows xp by replacing the "msv1_0.dll" file with the patched one, so on next boot up it wont ask any password. For Win 7 and 8 it rename the 'cmd.exe' to 'sethc.exe', so when login screen appears just press 'shift' key for 5 times. This would give you command prompt. From here you can do many things without logging in. You can open registry editor, computer mangement and many more. For Linux OS it creates another user named 'sysh' with same authorization as root user. The username and password in this script is 'sysh:Iamalive'.
