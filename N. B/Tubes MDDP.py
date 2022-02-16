import numpy as np
import pandas 
import os

d_training = pandas.read_csv(r'Data Training Klasifiaksi Obat.csv')
data = pandas.DataFrame(d_training)


#Masukkan data testting
print('\n')
print('=====Data Testing=====')
print('==================')
print('Memasukan Data Testing')
iu=eval(input('Masukan Umur : '))
ijeniskelamin=input('Masukan Jenis Kelamin : ')
itekanandarah=input('Masukan Tingkat Tekanan Darah : ')
ikolesterol=eval(input('Masukan Status Kolesterol : '))
print('=======================================================\n')


judul=('=======Deteksi Klasifikasi Obat=======')
kel=  ('========= Metode Naive Bayes=========')
print(judul.center(70))
print(kel.center(70))
print('================================================================')
print('================================================================')
print(data)
print('\n')

#umur Muda, Parobaya, Tua
umY = 18/54
umT = 31/91
upY = 23/54
upT = 38/91
utY = 14/54
utT = 27/91

#JENIS KELAMIN PEREMPUAN & LAKI-LAKI
dYY = 27/54
dYT = 47/91
dTY = 27/54
dTT = 44/91

#Tingkat Tekanan Darah
irY = 18/54
irT = 30/91
isY = 36/54
isT = 23/91
itY = 0/54
itT = 38/91

#Status Kolesterol 
hYY = 34/54
hYT = 44/91
hTY = 20/54
hTT = 47/91



#menghitung jumlah kelas
print('     Baca data training     ')
print('============================')
jml_class=data.groupby('Obat').size()
print(round(jml_class, 5))
print('\n')

print('   Menghitung kelas P(Ci)   ')
print('     pada data training     ')
print('============================')
jml_classOBATX = 54/145
jml_classOBATY = 91/145
print('(OBAT = X) = 54/145 =',(round(jml_classX,5)))
print('(OBAT = Y) = 91/145 =',(round(jml_classY,5)))
print('\n')
print('\n')


print('  Hitung Probabilitas Atribut Untuk Setiap Kelas P(X|Ci)')       
print('========================================================')
#umur MUDA, PAROBAYA, TUA
if iu >= 15 and iu <= 35 :
    print('UMUR = '+str(iu)+ '| OBAT = X = ',(round(umY,5)))
    print('UMUR = '+str(iu)+ '| OBAT = Y = ',(round(umT,5)))
    print('---------------------------------------------------------')
elif iu >= 36 and iu <= 56 :
    print('UMUR = '+str(iu)+ '| OBAT = X = ',(round(upY,5)))
    print('UMUR = '+str(iu)+ '| OBAT = Y = ',(round(upT,5)))
    print('---------------------------------------------------------')
elif iu >= 57 and iu < 77 :
    print('UMUR = '+str(iu)+ '| OBAT = X = ',(round(utY,5)))
    print('UMUR = '+str(iu)+ '| OBAT = Y = ',(round(utT,5)))
    print('---------------------------------------------------------')

#jenis kelamin perempuan dan laki-laki
if ijeniskelamin == 'PEREMPUAN' :
    print('JENISKELAMIN '+ijeniskelamin+' | OBAT = X = ',(round(dYY, 5)))
    print('JENISKELAMIN '+ijeniskelamin+' | OBAT = Y = ',(round(dYT, 5)))
    print('---------------------------------------------------------')
elif ijeniskelamin == 'LAKI-LAKI' :
    print('JENISKELAMIN '+ijeniskelamin+' | OBAT = X = ',(round(dTY, 5)))
    print('JENISKELAMIN '+ijeniskelamin+' | OBAT = Y  = ',(round(dTT, 5)))
    print('---------------------------------------------------------')

#tingkat tekanan darah 
if itekanandarah == 'RENDAH' :
    print('TEKANANDARAH = '+str(itekanandarah)+'| OBAT = X = ',(round(irY,5)))
    print('TEKANANDARAH = '+str(itekanandarah)+'| OBAT = Y =',(round(irT,5)))
    print('---------------------------------------------------------')
elif itekanandarah == 'NORMAL' :
    print('TEKANANDARAH = '+str(itekanandarah)+'| OBAT = X = ',(round(isY,5)))
    print('TEKANANDARAH = '+str(itekanandarah)+'| OBAT = Y =',(round(isT,5)))
    print('---------------------------------------------------------')
elif itekanandarah == 'TINGGI' :
    print('TEKANANDARAH = '+str(itekanandarah)+'| OBAT = X = ',(round(itY,5)))
    print('TEKANANDARAH = '+str(itekanandarah)+'| OBAT = Y =',(round(itT,5)))

#kolesterol
if ikolesterol == 'NORMAL' :
    print('KOLESTEROL '+ikolesterol+' | OBAT = X  = ',(round(hYY, 5)))
    print('KOLESTEROL '+ikolesterol+' | OBAT = Y  = ',(round(hYT, 5)))
    print('---------------------------------------------------------')
elif ikolesterol == 'TINGGI' :
    print('KOLESTEROL '+ikolesterol+' | OBAT = X  = ',(round(hTY, 5)))
    print('KOLESTEROL '+ikolesterol+' | OBAT = Y = ',(round(hTT, 5)))
    print('---------------------------------------------------------')


print('=======================================================\n')
print('\n')


#P(X|OBAT = X)

print('===Mencari P(X|OBAT = X )===')
print('=================================')

#Kategori umur dan OBAT X
if iu >= 15 and iu <= 35 :
    print('UMUR = '+str(iu)+ '| OBAT = X = ',(round(umY,5)))
    uky = (round(umY,3))
elif iu >= 36 and iu <- 56 :
    print('UMUR = '+str(iu)+ '| OBAT = X = ',(round(upY,5)))
    uky = (round(upY,3))
elif iu >= 57 and iu < 77 :
    print('UMUR = '+str(iu)+ '| OBAT = X = ',(round(utY,5)))
    uky = (round(utY,3))


#Kategori JENIS KELAMIN
if ijeniskelamin == 'PEREMPUAN' :
    print('JENIS KELAMIN '+ijeniskelamin+' |  OBAT = X = ',(round(dYY, 5)))
    dky = (round(dYY,3))
elif ijeniskelamin == 'LAKI-LAKI' :
    print('JENIS KELAMIN '+ijeniskelamin+' |  OBAT = X = ',(round(dTY, 5)))
    dky = (round(dTY,3))

#Kategori TEKANAN DARAH
if itekanandarah == 'RENDAH' :
    print('TEKANAN DARAH '+itekanandarah+' | OBAT = X = ',(round(hYY, 5)))
    hky = (round(hYY,3))
elif itekanandarah == 'NORMAL' :
    print('TEKANAN DARAH '+itekanandarah+' | OBAT = X = ',(round(hTY, 5)))
    hky = (round(hTY,3))
elif itekanandarah == 'TINGGI' :
    print('TEKANAN DARAH '+itekanandarah+' | OBAT = X = ',(round(hTY, 5)))
    hky = (round(hTY,3))

#intraokular KOLESTEROL
if ikolesterol == 'NORMAL' :
    print('KOLESTEROL = '+str(ikolesterol)+'| OBAT = X =  ',(round(irY,5)))
    iky = (round(irY,3))
elif ikolesterol == 'TINGGI' :
    print('KOLESTEROL = '+str(ikolesterol)+'| OBAT = X =  ',(round(isY,5)))
    iky = (round(isY,3))


hasilPX=float(uky*dky*hky*iky)
print('=======================================================')
print('P(X|OBAT = X ) = '+str(uky)+'*'+str(dky)+'*'+str(hky)+'*'+str(iky)+' = ',(round(hasilPX,5)))
print('=======================================================\n')

#P(X|OBAT = Y )
print('===Mencari P(X|OBAT = Y )===')
print('====================================')

#Umur 
if iu >= 15 and iu <= 35 :
    print('UMUR = '+str(iu)+ '| OBAT = Y = ',(round(umY,5)))
    uky = (round(umY,3))
elif iu >= 36 and iu <- 56 :
    print('UMUR = '+str(iu)+ '| OBAT = Y = ',(round(upY,5)))
    uky = (round(upY,3))
elif iu >= 57 and iu < 77 :
    print('UMUR = '+str(iu)+ '| OBAT = Y = ',(round(utY,5)))
    uky = (round(utY,3))

#Kategori JENIS KELAMIN
if ijeniskelamin == 'PEREMPUAN' :
    print('JENIS KELAMIN '+ijeniskelamin+' |  OBAT = Y = ',(round(dYY, 5)))
    dky = (round(dYY,3))
elif ijeniskelamin == 'LAKI-LAKI' :
    print('JENIS KELAMIN '+ijeniskelamin+' |  OBAT = Y = ',(round(dTY, 5)))
    dky = (round(dTY,3))

#Kategori TEKANAN DARAH
if itekanandarah == 'RENDAH' :
    print('TEKANAN DARAH '+itekanandarah+' | OBAT = Y = ',(round(hYY, 5)))
    hky = (round(hYY,3))
elif itekanandarah == 'NORMAL' :
    print('TEKANAN DARAH '+itekanandarah+' | OBAT = Y = ',(round(hTY, 5)))
    hky = (round(hTY,3))
elif itekanandarah == 'TINGGI' :
    print('TEKANAN DARAH '+itekanandarah+' | OBAT = Y = ',(round(hTY, 5)))
    hky = (round(hTY,3))

#intraokular KOLESTEROL
if ikolesterol == 'NORMAL' :
    print('KOLESTEROL = '+str(ikolesterol)+'| OBAT = X =  ',(round(irY,5)))
    iky = (round(irY,3))
elif ikolesterol == 'TINGGI' :
    print('KOLESTEROL = '+str(ikolesterol)+'| OBAT = X =  ',(round(isY,5)))
    iky = (round(isY,3))

    
hasilPY = float(ukt*dkt*hkt*ikt)
print('+======================================================+')
print('P(X|OBAT = Y ) = '+str(ukt)+'*'+str(dkt)+'*'+str(hkt)+'*'+str(ikt)+' = ',(round(hasilPY,3)))
print('========================================================\n')
print('\n')

#menjumlahkan seluruh probabilitas sesuai kelas OBAT
print('  Menghitung probabilitas kelas terhadap  ')
print('       seluruh prediktor sebelumnya       ')
print('==========================================')
print('         P(Ci|X)=P(X|Ci).P(Ci)')
posteriorX = ((hasilPX) * (jml_classOBATX))
posteriorY = ((hasilPY) * (jml_classOBATY))
print('OBAT "X"   = '+str(round(hasilPX,3))+' * '+str(round(jml_classOBATX,3))+') = ',(round(posteriorX,5)))
print('OBAT "Y"= '+str(round(hasilPY,3))+' * '+str(round(jml_classOBATY,3))+') = ',(round(posteriorY,5)))
print('\n')

print('Bandingkan Hasil :')
if posteriorX > posteriorY :
    print('Hasil "X" lebih besar, Dengan nilai ',(round(posteriorX,5)))
else: 
    print('Hasil "Y" lebih besar, Dengan nilai ',(round(posteriorY,5)))
    print('===============================================================')

print('HASIL AKHIR :')
if posteriorX > posteriorY :
    print('Karena Hasil "X" lebih besar, Jadi Pasien tersebut Kemungkinan Mengkonsumsi Obat X')
else: 
    print('Karena Hasil "Y" lebih besar, Jadi Pasien tersebut Kemungkinan Mengkonsumsi Obat Y')
    print('\n')
    print('\n')
