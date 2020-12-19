import OpenSSL

key = OpenSSL.crypto.PKey()
key.generate_key(OpenSSL.crypto.TYPE_RSA, 1024)

ca = OpenSSL.crypto.X509()
ca.set_version(1)
ca.get_subject().CN = "Omar Herrera"
ca.get_subject().C = "MX"
ca.get_subject().ST = "Jalisco"
ca.get_subject().L = "Guadalajara"
ca.get_subject().O = "Empresa Cooler S.A. de C.V."
ca.get_subject().OU = "IT"
ca.get_subject().emailAddress = "omar@herrera.mx"
ca.set_issuer(ca.get_subject())
ca.set_pubkey(key)
ca.add_extensions([
    OpenSSL.crypto.X509Extension(b'basicConstraints', True, b'CA:TRUE, pathlen:0'),
    OpenSSL.crypto.X509Extension(b'subjectKeyIdentifier', False, b'hash', subject=ca),
])
ca.sign(key, "sha1")
open("./cert/ca.cer", "wb").write(
    OpenSSL.crypto.dump_certificate(OpenSSL.crypto.FILETYPE_PEM, ca))