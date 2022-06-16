#Kubus
print("\nMENGHITUNG LUAS & VOLUME KUBUS")
r=int(input("Masukan Panjang Rusuk: "))
l=6*r*r
v=r*r*r
print("\nLuas Kubus \t\t:",l)
print("Volume Kubus\t:",v)

#Balok
print("\nMENGHITUNG LUAS & VOLUME BALOK")
p=int(input("Masukan Panjang: "))
l=int(input("Masukan Lebar: "))
t=int(input("Masukan Tinggi: "))
luas=2*((p*l)+(p*t)+(l*t))
v=p*l*t
print("\nLuas Balok \t\t:",luas)
print("Volume Balok\t:",v)

#Prisma
print("\nMENGHITUNG LUAS & VOLUME PRISMA")
a=int(input("Masukkan Alas: "))
la=int(input("Masukkan Luas Alas: "))
ka=int(input("Masukkan Keliling Alas"))
t=int(input("Masukkan Tinggi: "))
luas=(2*la)+(ka*t)
v=la*t
print("\nLuas Prisma \t:",luas)
print("Volume Prisma\t:",v)

#Limas
print("\nMENGHITUNG LUAS & VOLUME LIMAS")
tl=int(input("Masukkan Total Luas Sisi Miring: "))
a=int(input("Masukkan Alas: "))
la=int(input("Masukkan Luas Alas: "))
t=int(input("Masukkan Tinggi: "))
luas=la+tl
v=1/3*la*t
print("\nLuas Limas \t\t:",luas)
print("Volume Limas\t:",v)

#Tabung
print("\nMENGHITUNG LUAS & VOLUME TABUNG")
r=int(input("Masukkan Jari-Jari: "))
t=int(input("Masukkan Tinggi: "))
phi=22/7
luas=2*phi*r*(t+r)
v=phi*r*r*t
print("\nLuas Tabung \t:",luas)
print("Volume Tabung\t:",v)

#Kecurut
print("\nMENGHITUNG LUAS & VOLUME KERUCUT")
r=int(input("Masukkan Jari-Jari: "))
s=int(input("Masukkan Garis Pelukis: "))
t=int(input("Masukkan Tinggi: "))
phi=22/7
luas=phi*r*(r+s)
v=1/3*phi*r*r*t
print("\nLuas Kerucut \t:",luas)
print("Volume Kerucut\t:",v)

#Bola
print("\nMENGHITUNG LUAS & VOLUME BOLA")
r=int(input("Masukkan Jari-Jari: "))
phi=22/7
luas=4*phi*r*r
v=4/3*phi*r*r*r
print("\nLuas Bola \t:",luas)
print("Volume Bola\t:",v)