from Crypto.Cipher import AES
import codecs

aes_obj = AES.new(b'whyisthisthing11', AES.MODE_ECB)
plaintext=b'wow this message is so important'
ciphertext = aes_obj.encrypt(plaintext)

b64cipher = codecs.encode(ciphertext, "base64")
print(b64cipher)
