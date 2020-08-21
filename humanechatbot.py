import os
while True:
	print("Chat with me with your requarments:")
	p=input()
	if ((("run" in p) or ("launch" in p)or ("execute" in p) or ("open" in p)) and (("editor" in p)or("notepad" in p)or("text editor" in p) 		or("text"in p) or("wordpad" in p))):
		os.system("gedit")
	elif((("run" in p) or ("launch" in p)or ("execute" in p) or ("open" in p)) and (("vlc" in p) or ("video player" in p) or ("media player" in p) 		or("player" in p))):
		os.system("vlc")
	elif((("run" in p) or ("launch" in p)or ("execute" in p) or ("open" in p)) and (("firefox" in p) or ("browser" in p) or ("webpage" in p))):
		os.system("firefox")
	elif((("run" in p) or ("launch" in p)or ("execute" in p) or ("open" in p)) and (("sublime-text" in p) or ("sublime-text-editors" in p))):
		os.system("subl")
	elif((("run" in p) or ("launch" in p)or ("execute" in p) or ("open" in p)) and (("zoom" in p))):
		os.system("zoom")
	elif((("run" in p) or ("launch" in p)or ("execute" in p) or ("open" in p)) and (("cammera" in p))):
		os.system("cheese")
	elif((("run" in p) or ("launch" in p)or ("execute" in p) or ("open" in p)) and ((("anydesk" in p) or ("Share Screen" in p)))):
		os.system("anydesk")
	elif ((("start" in p)or ("status" in p)) and ("docker" in p)):
		os.system("systemctl status docker")
	elif ((("run" in p)) and ("docker" in p)):
		os.system("systemctl start docker")
	elif ((("start" in p)or ("status" in p)or ("stop" in p)) and ("docker" in p)):
		os.system("systemctl stop docker")
	elif ((("start" in p)or ("status" in p)or ("containers" in p) or ("running" in p)) and ("docker" in p)):
		os.system("docker ps -a")
	elif (((("status" in p)or ("images" in p)) and ("docker" in p))):
		os.system("docker images")
	elif ((("status" in p)) and (("apache" in p)or("httpd" in p) or ("webserver" in p))):
		os.system("systemctl status httpd")
	elif ((("stop" in p)) and (("apache" in p)or("httpd" in p) or ("webserver" in p))):
		os.system("systemctl stop httpd")
	elif ((("start" in p)) and (("apache" in p)or("httpd" in p) or ("webserver" in p))):
		os.system("systemctl start httpd")
	elif ((("show" in p) or ("version" in p)) and ("python" in p)):
		os.system("python3 --version")
	elif ((("show" in p) or ("version" in p)) and ("ansible" in p)):
		os.system("ansible --version")
	elif ((("show" in p) or ("status" in p)) and ("minikube" in p)):
		os.system("minikube status")
	elif ((("exit" in p) or ("stop" in p)) and ("minikube" in p)):
		os.system("minikube stop")
	elif ((("start" in p) or ("run" in p)) and ("minikube" in p)):
		os.system("minikube start")
	elif ((("show" in p) or ("pods" in p)) and ("kubernetes" in p)):
		os.system("kubectl get pods")
	elif((("open" in p) or ("run" in p)) and (("anacond"in p)or("navigator" in p))):
		os.system("anaconda-navigator")
	elif((("environment" in p)or("list" in p)or("env" in p)) and (("anacond"in p)or ("conda" in p))):
		os.system("conda env list")
	elif(("break" in p) or ("exit" in p)or ("quite" in p)or ("stop" in p)or ("logout"in p)):
		break
	else:
 		print("Not supported")
