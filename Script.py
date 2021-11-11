from Crypto.Cipher import AES
import binascii

if __name__ == "__main__" : 
    with open('flag.png', 'rb') as f:

        content = f.read()

        # 16 bytes lenght key
        key = "enter your key"
        
        # 32 bytes lenght IV 
        IV = binascii.unhexlify('enter your IV'.encode('utf-8'))

        aes = AES.new(key, AES.MODE_CBC, IV)

        content = aes.decrypt(content)

        with open("flag.png", 'wb') as x : 

            x.write(content)

        x.close()
