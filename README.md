<h1 align="center">
	<img src="https://www.nicepng.com/png/full/395-3955868_security-shield-lock-icon.png" width="150px"><br>
    C0mptCrypt - An object-oriented, minamalistic, simple encryption library in Python.
</h1>
<p align="center">
    C0mptCrypt allows you to encrypt and decrypt strings of text via AES. Your encrypted data/strings can only be decrypted using either your own custom key you set before encrypting said data, or by using C0mptCrypt's default key options. You can use this for a variety of things from creating passwords, to encrypting HWIDs and much more!. Making AES encryption a little bit easier!
</p>

<h1></h1>

<br />
<br />

# Updates
What has been updated as of | 2/23/22:

> - New hashing method using blake2b instead of md5.
> - Cleaned up the old clear() function so now it still works on windows and linux systems but with no if checks/statements.
> - Changed Class name to avoid redundancy in names when importing. (The class name is now "Crypt0r")
> - Updated the code in my sample file linked below under the Code Examples to reflect Class name change update.
> - A way for you as a user to use your own custom key for the encryption. (Making things even MORE secure.)
> - Blake2b hash salting. Making the hashing even more unique and secure!
> - And finally updated the Code Example below to match the Class name change update, as well as some minor improvements to this README.md file.
__ __

What has been updated as of | 2/24/22:

> - Decryption error handling. `Crypt0r().Decrypt(string2)` will return `None` now if any errors happen and will allow you to contine on with the rest of your code.

<br />
<br />

# Installation

```
My version/fork:
(Uses Blake2b hashing instead of md5, has a better clear function, and has a different class name when importing.)
- pip install git+https://github.com/therealOri/C0mptCrypt

Original Version:
- https://github.com/execution/C0mptCrypt
```
__ __

<br />
<br />

# Code Example

```python
from C0mptCrypt import Crypt0r

#Encrypting
string = input("Enter string: ")
encr = Crypt0r().Encrypt(string)
print(encr)


#Decrypting
string2 = input("Enter string: ")
decr = Crypt0r().Decrypt(string2) #Will return "None" if any errors happen.
print(decr)
```
__ __

My own sample file for this project: [crypt_sample.py](https://haste.powercord.dev/kopibogovo.py)
