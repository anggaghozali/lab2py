a=input("masukan nilai a:")
b=input("masukan nilai b:")

print("variavel a=",a)
print("variabel b=",b)

print("hasil penggabungan {1}&{0}=%s".format (a,b) % (a+b))

a=int (a)
b=int (b)
print("hasil penjumlahan {1}+{0}=%d".format (a,b) % (a+b))
print("hasil pembagian {1}/{0}=%d".format (a,b) % (a/b))