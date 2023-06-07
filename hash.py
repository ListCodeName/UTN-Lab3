"""
import hashlib

password = "contraseña1"

print(len(hashlib.sha256(password.encode()).hexdigest()))

print(len(hashlib.sha512(password.encode()).hexdigest()))

print(len(hashlib.md5(password.encode()).hexdigest())) 

"""

cadena = input("Ingrese palabra para hashear: ")
hashcode = 0
for x in range (len(cadena)):
    hashcode += int(ord(cadena[x]))*31 and 0xFFFFFFFF
print(hashcode)