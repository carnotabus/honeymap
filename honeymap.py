import os
import time
from colorama import init, Fore, Back, Style
#deben tener colorama

def banner():
    print("\x1b[1;33m"+"""
                                                  
     /\  /\___  _ __   ___ _   _  /\/\   __ _ _ __  
    / /_/ / _ \| '_ \ / _ \ | | |/    \ / _` | '_ \ 
   / __  / (_) | | | |  __/ |_| / /\/\ \ (_| | |_) |
   \/ /_/ \___/|_| |_|\___|\__, \/    \/\__,_| .__/ 
                        |___/             |_|    
                      __
                     // \
                     \\_/ //
   ''-.._.-''-.._.. -(||)(')
                     '''
           ---------------------------
           [Automatizar basico de NMAP]
           [-Busqueda de vulnerabilidades]
           [-Ataque pasivo, ataque agresivo]
           [-BY: vulk4no, 2/05/2021]
           [BAJO TU RESPONSABILIDAD,USO EDUCATIVO]
           -------------------------

           -fase alpha-

           [Instalacion]
           ¿Que utilizas?
           [1] Basado en debian/ubuntu
           [2] Termux
           [3] basado en Arch
    """)

def banner2():
    print(Fore.RED+"""
    
                       @@@@@@@@@@@@@@@@@@
                    @@@@@@@@@@@@@@@@@@@@@@@
                  @@@@@@@@@@@@@@@@@@@@@@@@@@@   <-- The creator --> 
                 @@@@@@@@@@@@@@@@@@@@@@@@@@@@@
                @@@@@@@@@@@@@@@/      \@@@/   @
                @@@@@@@@@@@@@@@@\      @@  @___@
               @@@@@@@@@@@@@ @@@@@@@@@@  | \@@@@@    <-- Hora de trabajar! --> 
               @@@@@@@@@@@@@ @@@@@@@@@\__@_/@@@@@ 
                @@@@@@@@@@@@@@@/,/,/./'/_|.\'\,\ 
                  @@@@@@@@@@@@@|  | | | | | | | |
                                \_|_|_|_|_|_|_|_| 
    
          [Opciones]
          [0] Escaneo basico
          [1] Busca vulnerabilidades
          [2] Detectar el sistema operativo y más datos del host
          [3] Escaneo sigiloso
          [4] Escaneo agresivo
          [5] Escanea un puerto especifico
          [6] Escanea los puertos principales

          ¿Cual elijes?
    """)

#instalacion de dependencias

def termux():
  print("\n Actualizando y descargando dependencias")
  time.sleep(3)
  print("\n Cargando...")
  time.sleep(3)
  os.system("pkg install curl")
  os.system("pkg install nmap")

def deb():
  print("\n Actualizando y descargando dependencias")
  time.sleep(3)
  print("\n Cargando...")
  time.sleep(3)
  os.system("sudo apt install nmap")

def arch():
  print("\n Actualizando y descargando dependencias")
  time.sleep(3)
  print("\n Cargando...")
  time.sleep(3)
  os.system("sudo pacman -S nmap")

def salir():
  os.system("clear")
  os.system("python3 pronto.py")

def n0():
  ip = input("\n Introduce el target a escanear: ")
  os.system(f"nmap {ip}")

def n1():
  ip = input("\n Introduce el target a escanear: ")
  os.system(f"nmap -sV -sS -O -f --script vuln {ip}")

def n2():
  ip = input("\n Introduce el target a escanear: ")
  os.system(f"nmap -A -v {ip}")

def n3():
  ip = input("\n Introduce el target a escanear: ")
  os.system(f"nmap -T2 -Pn -f -sV {ip}")

def n4():
  ip = input("\n Introduce el target a escanear: ")
  os.system(f"nmap -T4 -Pn -f -sV {ip}")

def n5():
  ip = input("\n Introduce el target a escanear: ")
  puerto = input("\n Introduce el puerto a escanear: ")
  os.system(f"nmap -p {puerto} {ip}")

def n6():
  ip = input("\n Introduce el target a escanear: ")
  os.system(f"nmap --top-ports 25 {ip}")


os.system("clear")

banner()
op=int(input("\n Responde: "))
if op == 1:
  deb()
elif op == 2:
  termux()
elif op == 3:
  arch()
else:
  print("\n HAS INTRODUCIDO ALGO INCORRECTO!!!")
  time.sleep(3)
  os.system("python3 honeymap.py")

os.system("clear")
banner2()
opp= int(input("\n Introduce tu elección: "))
if opp == 0:
  n0()
elif opp == 1:
  n1()
elif opp == 2:
  n2()
elif opp == 3:
  n3()
elif opp == 4:
  n4()
elif opp == 5:
  n5()
elif opp == 6:
  n6()
else:
  print("\n HAS INTRODUCIDO ALGO INCORRECTO!!!")
  time.sleep(3)
  os.system("python3 honeymap.py")

print("\n ¿Quieres hacer otra operación?")
el= int(input("\n [1]SI\n [2]No\n [Responde: "))
if el ==1:
  os.system("python3 honeymap.py")
else:
  os.system("clear")
  print("\n Gracias por utlizarme :D")
  exit