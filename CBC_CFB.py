from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto import Random
from Crypto.Util.Padding import pad,unpad

key = get_random_bytes(32)

iv = Random.new().read(AES.block_size)
plaintext = b'11234567812345678234567812345678'

Encrypt_obj = AES.new(key, AES.MODE_CFB, iv)
Encrypt_obj1 = AES.new(key, AES.MODE_CBC, iv)
Encrypt_obj2 = AES.new(key, AES.MODE_OFB, iv)
Encrypt_obj3 = AES.new(key, AES.MODE_ECB)

ciphertext = iv + Encrypt_obj.encrypt(pad(plaintext, AES.block_size))
ciphertext1 = iv + Encrypt_obj1.encrypt(pad(plaintext, AES.block_size))
ciphertext2 = iv + Encrypt_obj2.encrypt(pad(plaintext, AES.block_size))
ciphertext3 = iv + Encrypt_obj3.encrypt(pad(plaintext, AES.block_size))

Dec_obj = AES.new(key, AES.MODE_CFB, iv)
Dec_obj1 = AES.new(key, AES.MODE_CBC, iv)
Dec_obj2 = AES.new(key, AES.MODE_OFB, iv)
Dec_obj3 = AES.new(key, AES.MODE_ECB)

plaintextcfb = iv + unpad(Dec_obj.decrypt(ciphertext), AES.block_size)
plaintextcbc = iv + unpad(Dec_obj1.decrypt(ciphertext1), AES.block_size)
plaintextOFB = iv + Dec_obj2.decrypt(ciphertext2), AES.block_size
plaintextECB = iv + unpad(Dec_obj3.decrypt(ciphertext3), AES.block_size)

print("PT" +str(plaintext))

print("CBC: " + str(plaintextcbc))
print("CFB: " + str(plaintextcfb)) 
print("OFB" + str(plaintextOFB))
print("ECB" + str(plaintextECB))
print("CTR" + str(plaintextCTR))
