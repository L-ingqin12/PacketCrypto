from PacketCrypto import *

generateRsaKey()
setPublicKey()
encode = encryptPacket(
    {'name': 123, 'dasd': 'dasdasd', 'list': [123, 21, 21, 2]})
print(encode)
decode = decryptPacket(encode)
print(decode)
