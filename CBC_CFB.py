from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto import Random
from Crypto.Util.Padding import pad,unpad

key = get_random_bytes(32)

iv = Random.new().read(AES.block_size)
plaintext = b'11234567812345678234567812345678'

Encrypt_obj = AES.new(key, AES.MODE_CFB, iv)
Encrypt_obj1 = AES.new(key, AES.MODE_CBC, iv)

cyphertext = iv + Encrypt_obj.encrypt(pad(plaintext, AES.block_size))
cyphertext1 = iv + Encrypt_obj1.encrypt(pad(plaintext, AES.block_size))

Dec_obj = AES.new(key, AES.MODE_CFB, iv)
Dec_obj2 = AES.new(key, AES.MODE_CBC, iv)

plaintextcfb = iv + unpad(Dec_obj.decrypt(cyphertext), AES.block_size)
plaintextcbc = iv + unpad(Dec_obj2.decrypt(cyphertext1), AES.block_size)

print("CBC: " + str(plaintextcbc))
print("CFB: " + str(plaintextcfb)) 
