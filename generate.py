from Crypto.PublicKey import RSA

key = RSA.generate(2048)

f = open("./cert/priv.pem", "wb")
f.write(key.exportKey("PEM"))
f.close()

f = open("./cert/pub.pem", "wb")
f.write(key.publickey().exportKey("PEM"))
f.close()