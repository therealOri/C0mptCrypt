import base64, hashlib, sys, time, os
from Crypto.Random import get_random_bytes
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad


# main.py
# Date: 01/02/2022
# Author: execution
# Contributor: therealOri


class Crypt0r:

    def __init__(self):
        try:
            option = int(input('1. Custom key\n2. Default key\n\nEnter: '))
            self.Clear()
            
            if option == 1:
                key = input('Pls gib encryption key?: ')
                salt = input('Pls gib a word for the salt? [16 characters MAX]: ')
                self.hash_key = hashlib.blake2b(key.encode('utf-8'), digest_size=16, salt=bytes(salt, 'utf-8')).digest()
            elif option == 2:
                print('Using the "Default key" option!\n')
                self.hash_key = hashlib.blake2b('c0mpt0_&_Ori'.encode('utf-8'), digest_size=16, salt=bytes('eihpliaghpitgblw', 'utf-8')).digest()
            else:
                print('That is not a valid option..Using the "Default key" option.\n')
                input('Press "Enter" to continue...')
                self.hash_key = hashlib.blake2b('c0mpt0_&_Ori'.encode('utf-8'), digest_size=16, salt=bytes('eihpliaghpitgblw', 'utf-8')).digest()
        except Exception as e:
            self.Clear()
            print(f'Oops..An error has occured..Using the "Default key" option.\nError: {e}\n')
            input('Press "Enter" to continue...')
            self.Clear()
            self.hash_key = hashlib.blake2b('c0mpt0_&_Ori'.encode('utf-8'), digest_size=16, salt=bytes('eihpliaghpitgblw', 'utf-8')).digest()
            

    def Clear(self):
        os.system('clear||cls')

    def EncryptSpinner(self):
        l = ['|', '/', '√', '\\']
        for i in l+l+l:#
            sys.stdout.write(f'\rEncrypting...'+i)
            sys.stdout.flush()
            time.sleep(0.2)

    def DecryptSpinner(self):
        l = ['|', '/', '√', '\\']
        for i in l+l+l:#
            sys.stdout.write(f'\rDecrypting...'+i)
            sys.stdout.flush()
            time.sleep(0.2)

    def Encrypt(self, string):
        r = get_random_bytes(AES.block_size)
        h = AES.new(self.hash_key, AES.MODE_CBC, r)
        e = base64.b64encode(r + h.encrypt(pad(string.encode('utf-8'), AES.block_size)))
        self.EncryptSpinner()
        self.Clear()
        return e.decode()
    
    def Decrypt(self, string):
        r = base64.b64decode(string)
        c = AES.new(self.hash_key, AES.MODE_CBC, r[:AES.block_size])
        d = unpad(c.decrypt(r[AES.block_size:]), AES.block_size)
        self.DecryptSpinner()
        self.Clear()
        return d.decode()



