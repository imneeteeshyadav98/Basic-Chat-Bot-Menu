import os
print()
print("Press 1 to open: Chrome")
print("Press 2 to open: Gedit")
print("Press 3 to open: VLC")
print()

print("Enter your choice:")
p=input()
if int(p)==1:
 os.system("firefox")
elif int(p)==2:
 os.system("gedit")
elif int(p)==3:
 os.system("vlc")
else:
 print("Not supported")
