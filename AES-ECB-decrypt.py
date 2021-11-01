from Crypto.Cipher import AES
import codecs

ciphertext = codecs.decode(b'3MTxX3+WjWTbLu397Th/M4f4RMg4ROG0ZaIhgP7htVo=\n', 'base64')
aes_obj = AES.new(b'whyisthisthing11', AES.MODE_ECB)
plaintext = aes_obj.decrypt(ciphertext)
print(plaintext)
