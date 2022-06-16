data1=[1,3,4,5,7,9]
data2=[10,11,14,17,19,40,41]
print(data1)
print(data2)
#manipulasi data1
print(data1)
#menambahkan data dalam list
data1.append(6)
print(data1)
#menghapus data dalam list
data1.remove(4)
print(data1)
#mengganti data dalam list
data1 [1]=10
print(data1)
#menampilkan data ke-n atau data tertentu
print(data1[:-2])
print(data1[0:3])
print(data1[2:-1])

#penggabungan dua atau lebih list
data1=[0,1,4]
data2=[10,11,14]
data3=[40,41,44]
print("\n")
#cara menggabungkan list
print(data1+data2+data3)
x=(data1,data2,data3)
print(x)
print(x[2][-3])
print(x[0][2])
x[2][-2]=21
print(x)
x[0][1]=100
print(x)

#cara menduplikasi list
print("\n")
a=[0,1,4,10,11,14]
b=a
print(a)
print(b)
b[-4]=41
print(b)
print(a)
#cara agar nilai a tidak ikut berubah
b=a[:]
print(b,"dan",a)
a[-4]=4
print(a,"dan",b)
