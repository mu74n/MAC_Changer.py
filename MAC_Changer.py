import subprocess
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-i","--interface", dest="interface",help="Indica la interfaz de red")
parser.add_argument("-M","--MAC-address",dest="new_mac", help="Ingresa la nueva direccion MAC asociada a la interfaz elegida")
args=parser.parse_args()
try:
	print ("[+] La interfaz " + args.interface + " ahora tiene la MAC Adress: "+ args.new_mac)
	subprocess.call("ifconfig " + args.interface + " down", shell=True)
	subprocess.call("ifconfig " + args.interface + " hw ether " + args.new_mac, shell=True)
	subprocess.call("ifconfig " + args.interface + " up",shell=True)
except:
	print("No se han ingresado los parametros adecuados. Try again!")

