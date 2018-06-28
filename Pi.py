#!/bin/python
#SAFA BAYAR  Ogrenci No: 161906001
#calistirmak icin: 'mpiexec -n 4 python Pi.py' 
#Sonucun tam cikmasi icin son asamaya kadar beklenmesi gerekiyor. fonksiyondan otomatik cikmiyor. 

from mpi4py import MPI				#Kutuphane tanimlamalari

comm = MPI.COMM_WORLD
rank = comm.Get_rank()				#Paralellestirmek icin kutuphanedekileri degisken olarak ataniyor.
size = comm.Get_size()

def pis():			#pis adinda fonksiyon tanimlamasi
        N=0			#N sayac amacina kullanilacaktir
        TOPLAM=0		#Sonucu belirtir.
        SON=10**7		#Bu kisimda hangi satira kadar hesaplanacagi girilecektir.#degerlerin tanimlanmasi ve deger verilmesi
        
        while N<SON:		#Girilen basamaga kadar gitmesini geldikten sonra durmasini soyler.
                TOPLAM=TOPLAM+int((-1)**N)/float(2*N+1)		#Toplam degerin hesaplamasi sonrasinda Sizin verdiginiz hesaplama formulunu kullandim.
                N=N+1						#Sayac tutulmustu bu sayede while dongusu sonlanacagi yere geldiginde duracaktir.
                z=4*TOPLAM				#Formulden gelen 4 ile carpma vardir ve sonucu bastirmistir.
        print z

if comm.rank == 0:			#sifirinci  yani main cekirdek atatigimiz degere gelince asagidakini uygula anlamina geliyor. 
        for i in range(1,size):		#size degiskeni yukarda kac cekirdege sahip oldugumuzu gosterir. 
                data = pis()		 #fonksiyonu degiskene atiyoruz. mpi'da parametre olarak fonksiyon kullanamamaktayiz. 
                sum = comm.recv(source=i)	 #sum degeri butun cekirdeklere dagitilan islemin sonucudur.
                        

else:
        sum = pis()			#eger cekirdeklere dagitilmiyor ise sifirinci yani main cekirdekte islemin yapilmasini belirtmekte
        comm.send(sum, dest=0)

