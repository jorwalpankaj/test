from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto import Random
from Crypto.Util.Padding import pad,unpad

key = get_random_bytes(32)

iv = Random.new().read(AES.block_size)
plaintext = b'11234567812345678234567812345678'

Encrypt_obj = AES.new(key, AES.MODE_CBC, iv)

cyphertext1 = iv + Encrypt_obj.encrypt(pad(plaintext, AES.block_size))
print(cyphertext1.hex())

Dec_obj = AES.new(key, AES.MODE_CBC, iv)
plaintext2 = iv + unpad(Dec_obj.decrypt(cyphertext1), AES.block_size)

print(str(plaintext2))
