from cryptography.fernet import Fernet

content = "Reshma"

# Random generation of Encryption
keys = Fernet.generate_key()
print(keys)

# Python understandable encoding (b'content')
contentencode = content.encode()
print(contentencode)

# Actual encryption -> Fernet(random generation).encrypt(Python understandable encoding)
encrypt = Fernet(keys).encrypt(contentencode)
print(encrypt)

decrypt = Fernet(keys).decrypt(encrypt)
print(decrypt)

contentdecode = decrypt.decode()
print(contentdecode)
