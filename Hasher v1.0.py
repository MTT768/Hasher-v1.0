import hashlib as hasher

encoder = hasher.sha256()
metin = input("Type What You Want to Encrypt:")
encoder.update(metin.encode("utf-8"))
hash = encoder.hexdigest()

print("Şifreleme Başarıyla Tamamlandı:",hash)
print("Coded by: MuhammedTr768")