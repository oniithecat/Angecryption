#!/usr/bin/env python3

from Crypto.Cipher import *
import sys
import argparse
from colorama import *

init()

banner = Fore.BLUE + Style.BRIGHT + "[~] Angecryption, v1.0.0\n"

def main(options):
                try : 
                    with open(options.file,"rb") as a :
                        encrypted = a.read()
                except:
                    print(Fore.RED + f"[-] Problem for reading the file")
                try :
                    options.iv = bytes.fromhex(options.iv) 
                except:
                    print(Fore.RED + f"[-] The IV is not in the right format")
                    return
                try:
                    aes = AES.new(options.key, AES.MODE_CBC, options.iv)
                except:
                    print(Fore.RED + f"[-] Problem when creating the AES key")
                    return
                decrypted = aes.decrypt(encrypted)
                try:        
                    with open(options.output,'wb') as b:
                        b.write(decrypted)
                except:
                    print(Fore.RED + f"[-] Problem when creating the new file")
                    return
                b.close()
        
def parseArgs():
    description = "This script can be used for a file that uses Angecryption"
    parser = argparse.ArgumentParser(
        description=description,
        formatter_class=argparse.RawTextHelpFormatter,
    )
    parser.add_argument("-f", "--file", default=None, action="store_true", help="Name of the input file")
    parser.add_argument("-k", "--key", default=None, action="store_true", help="Angecryption's key")
    parser.add_argument("-o", "--output", default="decrypted", action="store_true", help="Name of the output file")
    parser.add_argument("-i", "--iv", default=None, action="store_true", help="Angecryption's IV")
    if len(sys.argv)==1:
	    parser.print_help(sys.stderr)
	    sys.exit(1)
    return parser.parse_args()
    
    
if __name__ == "__main__" :
    print(banner)
    options = parseArgs()
    main()   
