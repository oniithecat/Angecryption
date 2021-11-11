#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from Crypto.Cipher import AES
import binascii
from termcolor import colored
from art import *
import sys
import argparse

banner = "[~] Angecryption, v1.0\n"

def main(options):
		try :
			with open(options.file,"rb") as a :
				encrypted = a.read()
		except:
			print(f"Problème lors de la lecture du fichier")
			return
		try :
			options.iv = binascii.unhexlify(iv.encode('utf-8')) 
		except:
			print(f"L'iv n'est pas au bon format")
			return
		try:
			aes = AES.new(options.key, AES.MODE_CBC, options.iv)
		except:
			print(f"Problème lors de la création de la clé AES")
			return
		decrypted = aes.decrypt(encrypted)
		try:		
			with open(options.output,'wb') as b:
				b.write(decrypted)
		except:
			print(f"Problème lors de la création du nouveau fichier")
			return
		b.close()

		
def parseArgs():
    description = "Ce script peut être utilisé pour un fichier qui utilise l'Angecryption"
    parser = argparse.ArgumentParser(
        description=description,
        formatter_class=argparse.RawTextHelpFormatter,
    )
    parser.add_argument("-f", "--file", default=None, action="store_true", help="Nom du fichier d'entrée")
    parser.add_argument("-k", "--key", default=None, action="store_true", help="Clé de l'angecryption")
    parser.add_argument("-o", "--output", default="decrypted", action="store_true", help="Nom du fichier de sortie")
    parser.add_argument("-i", "--iv", default=None, action="store_true", help="IV de l'angecryption")
    if len(sys.argv)==1:
	    parser.print_help(sys.stderr)
	    sys.exit(1)
    return parser.parse_args()
    
    
if __name__ == "__main__" :
    print(banner)
    options = parseArgs()
    main()
        
        
        
