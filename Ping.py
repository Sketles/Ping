import os
import time
import pyfiglet
logo = pyfiglet.figlet_format("Ping the world")
google = pyfiglet.figlet_format("Google")
amazon = pyfiglet.figlet_format("Amazon")
youtube = pyfiglet.figlet_format("Youtube")
cmd = "color 2"
os.system(cmd)
cmd = "cls"
os.system(cmd)
while(True):
    print(logo)
    print("Bienvenido que desea pingear")
    print("1-Google")
    print("2-Amazon")
    print("3-Youtube")
    print("4-Salir")
    option = input()
    cmd = "cls"
    os.system(cmd)
    if(option=="1"):
        print(google)
        print("Haciendo Ping a Google.com")
        cmd = "ping www.google.com"
        os.system(cmd)
        print("--------->>>> Terminado con exito")
        time.sleep(2.0)
        cmd = "cls"
        os.system(cmd)
    elif(option=="2"):
        print(amazon)
        print("Haciendo Ping a Amazon.com")
        cmd = "ping www.amazon.com"
        os.system(cmd)
        print("--------->>>> Terminado con exito")
        time.sleep(2.0)
        cmd = "cls"
        os.system(cmd)
    elif(option=="3"):
        print(youtube)
        print("Haciendo Ping a Youtube.com")
        cmd = "ping www.youtube.com"
        os.system(cmd)
        print("--------->>>> Terminado con exito")
        time.sleep(2.0)
        cmd = "cls"
        os.system(cmd)
    elif(option=="4"):
        cmd = "cls"
        os.system(cmd)
        print("Preciona Ctrl + C to exit")
        time.sleep(3.0)
    else:
        print("--------->>>> Opcion Incorrecta")
