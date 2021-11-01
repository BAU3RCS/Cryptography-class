from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
import codecs

file_in=open("encrypted.bin","rb")
nonce, tag, ciphertext = [ file_in.read(x) for x in (16, 16, -1) ]
file_in.close()
cipher=AES.new(b'\xd0\x1e\x84\xaeR\x8f\xf2\x83\xf5"\xf6\x98\xc6\x91m\xa9', AES.MODE_EAX, nonce)
decrypted=cipher.decrypt_and_verify(ciphertext,tag)
print(decrypted)
