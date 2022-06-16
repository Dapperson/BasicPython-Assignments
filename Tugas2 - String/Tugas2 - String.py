"roni"
"roni merdiansah"
'roni merdiansah'
text1='roni merdiansah'
print(text1)
#atau
text1="Roni Merdiansah"
print(text1)

#penggunaan kutip dua dan kutip satu pada string
text1="\nRoni Merdi'ansah"
text2='Roni Merdi\'ansah'
print(text1,text2)
text1="saya berkata,\"panggil saja saya Roni\""
print(text1)

#contoh dialog percakapan
text1="\nroni:\"hari minggu besok kamu mau kemana di?\",merdi:\"sepertinya saya mau lari pagi ron, kamu mau ikut?\",roni:\"oh boleh di\""
print(text1)
text2="roni:\'hari minggu besok kamu mau kemana di?\',\nmerdi:\'sepertinya saya mau lari pagi ron, kamu mau ikut?\',\nroni:\'oh boleh di\'"
print(text2)

#row string
text1="\nc:\nyamuk"
print(text1)
text1= r'c:\nyamuk'
print(text1)

#dialog percakapan dengan menggunakan 3 buah kutip dua
text1="""
roni:hari minggu besok kamu mau kemana di?
merdi:sepertinya saya mau lari pagi ron, kamu mau ikut?
roni:oh boleh di
"""
print(text1)

#menentukan huruf dalam kata
text1="roni merdiansah"
a=text1[7]
print(a)
a=text1[0:10]
print(a)
a=text1[:-2]
a=text1[1:-8]
print(a)
a=text1[0:4]
print("nama saya",a)
