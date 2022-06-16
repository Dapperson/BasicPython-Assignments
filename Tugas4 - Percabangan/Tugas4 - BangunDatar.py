#Persegi
print("\nMENGHITUNG LUAS & KELILING PERSEGI")
s=int(input("Masukan Panjang Sisi: "))
l=s**2
k=4*s
print("\nLuas Persegi \t\t:",l)
print("Keliling Persegi\t:",k)

#Persegi Panjang
print("\nMENGHITUNG LUAS & KELILING PERSEGI PANJANG")
panjang=int(input("Masukan Panjang: "))
lebar=int(input("Masukan Lebar: "))
luas=panjang*lebar
kel=(panjang+lebar)*2
print("\nLuas Persegi Panjang \t\t:",luas)
print("Keliling Persegi Panjang\t:",kel)

#Jajargenjang
print("\nMENGHITUNG LUAS & KELILING JAJARGENJANG")
a=int(input("Masukkan Alas: "))
b=int(input("Masukkan Sisi Miring: "))
t=int(input("Masukkan Tinggi: "))
luas=a*t
kel=2*(a+b)
print("\nLuas Jajargenjang \t\t:",luas)
print("Keliling Jajargenjang\t:",kel)

#Trapesium
print("\nMENGHITUNG LUAS & KELILING TRAPESIUM")
a=int(input("Masukkan Sisi Sejajar 1: "))
b=int(input("Masukkan Sisi Sejajar 2: "))
c=int(input("Masukkan Sisi Miring 1: "))
d=int(input("Masukkan Sisi Miring 2: "))
t=int(input("Masukkan Tinggi: "))
luas=1/2*(a+b)*t
kel=a+b+c+d
print("\nLuas Trapesium \t\t:",luas)
print("Keliling Trapesium\t:",kel)

#Layang-Layang
print("\nMENGHITUNG LUAS & KELILING LAYANG-LAYANG")
a=int(input("Masukkan Sisi 1: "))
b=int(input("Masukkan Sisi 2: "))
d1=int(input("Masukkan Diagonal 1: "))
d2=int(input("Masukkan Diagonal 2: "))
luas=1/2*d1*d2
kel=2*(a+b)
print("\nLuas Layang-Layang \t\t:",luas)
print("Keliling Layang-Layang\t:",kel)

#Belah Ketupat
print("\nMENGHITUNG LUAS & KELILING BELAH KETUPAT")
s=int(input("Masukkan Sisi: "))
d1=int(input("Masukkan Diagonal 1: "))
d2=int(input("Masukkan Diagonal 2: "))
luas=1/2*d1*d2
kel=4*s
print("\nLuas Belah Ketupat \t\t:",luas)
print("Keliling Belah Ketupat\t:",kel)

#Segitiga
print("\nMENGHITUNG LUAS & KELILING SEGITIGA")
a=int(input("Masukkan Alas: "))
b=int(input("Masukkan Sisi 1: "))
c=int(input("Masukkan Sisi 2: "))
t=int(input("Masukkan Tinggi: "))
luas=1/2*a*t
kel=a+b+c
print("\nLuas Segitiga \t\t:",luas)
print("Keliling Segitiga\t:",kel)

#Lingkaran
print("\nMENGHITUNG LUAS & KELILING LINGKARAN")
r=int(input("Masukkan Jari-Jari: "))
phi=22/7
luas=phi*r*r
kel=2*phi*r
print("\nLuas Lingkaran \t\t:",luas)
print("Keliling Lingkaran\t:",kel)