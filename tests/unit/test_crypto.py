import i6

i6.errors

aes = i6.crypto.AES()

ct = aes.encrypt('hello')

print(ct)
print(aes.decrypt(ct))
