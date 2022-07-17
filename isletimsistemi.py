from time import sleep
import sys, os
import random
import enum


# işletim sistemininden çıkış methodu
def ExitOS():
    print("")
    print("İşletim Sisteminden çıkışınız yapılıyor...")
    print("Lütfen bekleyiniz.")
    cizgiUret(20)
    
#arrival biz giriyoruz
#burst biz  giriyoruz


# tasarım amaçlı çizgi üreten method
def cizgiUret(cizgiSayisi):
    cizgi = "-"
    for i in range(cizgiSayisi):
        print(cizgi, end=" ")
        #sleep(0.5)

print("")
#Sınırlı bir olası değeri olan değişken grubumuz olduğu için enum kullandık 
# Processlerimizi tutan Enum sınıfımız
class Loglevel(enum.Enum):
    def StartProcess():
         return "Süreç Başlıyor      :"
    def SystemCall():
        return "Sistem Çağrısı      :"
    def StopProcess():
        return "Süreç sonlandı      :"
    def TimerCut():
        return "Zamanlayıcı Kesimi  :"

        
#ilk giren ilk çıkar algoritması
def ScheduleAlgorithm(n):
    
    
    
    print("Mevcut süreç sayısı: ",n);#süreç sayımız
    d = dict()
     
   
    
    for i in range(n):
        key = "P: "+str(liste[i]())
        a = int(input(str(liste[i]())+" için başlangıç zamanını (arrival time) giriniz: "))
        b = int(input(str(liste[i]())+" için çalışma süresi (burst time) giriniz: "))
        l = []
        l.append(a)
        l.append(b)
        d[key] = l#süreçlerimizin giriş ve süreç vakitlerini buradan ayarlıyoruz
     
    d = sorted(d.items(), key=lambda item: item[1][0])
     
    ET = []
    for i in range(len(d)):
        # first process
        if(i==0):
            ET.append(d[i][1][1])
     
        # get prevET + newBT
        else:
            ET.append(ET[i-1] + d[i][1][1])
  #exit=bir önceki exit+burst
#wait=turnaround-arival   
    TAT = []
    for i in range(len(d)):
        TAT.append(ET[i] - d[i][1][0])
     
    WT = []
    for i in range(len(d)):
        WT.append(TAT[i] - d[i][1][1])

    avg_WT = 0
    for i in WT:
        avg_WT +=i
    avg_WT = (avg_WT/n)
     
    print("Process                     | Arrival | Burst | Exit | Turn Around | Wait |")
    
    ths = open("okubeni.txt", "w") # Dosya oluştur
    ths.write("Process                     | Arrival | Burst | Exit | Turn Around | Wait |\n")
    
    for i in range(n):
          print("",d[i][0],"   |   ",d[i][1][0]," |    ",d[i][1][1]," |    ",ET[i],"  |    ",TAT[i],"  |   ",WT[i],"   |  ")
          
          
          ths.write("");
          ths.write(str(d[i][0]));
          ths.write("   |   ")
          ths.write(str(d[i][1][0]))
          ths.write(" |         ")
          ths.write(str(d[i][1][1]))
          ths.write(" |    ")
          ths.write(str(ET[i]))
          ths.write("  |    ")
          ths.write(str(TAT[i]))
          ths.write("  |   ")
          ths.write(str(WT[i]))
          ths.write("   |         ")
          ths.write("\n")
         
            
    print("Ortalama Bekleme Süresi: ",avg_WT)
    print("Veriler Dosyalanıyor...")
    sleep(3)
    print("Veriler dosyalandı.")
    sleep(1)

 
   

# MAIN KISMI


# Processlerimizi içeren listemiz.
liste=[Loglevel.StartProcess, Loglevel.SystemCall, Loglevel.StopProcess, Loglevel.TimerCut]

boyut = len(liste)

ScheduleAlgorithm(boyut)

kalan = []

print("")
print("Listemizin Adresi: ", hex(id(liste))) 

counter = 0
while counter<=3:
    
    
    #print(str(counter)+". eleman için Sanal adres "+str(liste[counter]()))
    print(liste[counter](), "Decimal : "  ,(id(liste[counter])))
    kalan.append(id(liste[counter]) % 100000) # Logical Adresimizin son 5 hanesini saklıyoruz.
    
    #print(str(counter)+". eleman için Fiziksel adres "+str(liste[counter]))
    liste[counter]()
    # Döngüyü sonlandırabilmek için sayacımızı 1 arttırıyoruz.
    counter = counter+1

print("")
print("")

print("")
print("47 bit Logical Adresler: ")
counter = 0
while counter <= 3:
    sayi = id(kalan[counter])
    ikilikSayi = " "
    
    while sayi!=0:
        ikilikSayi = str(sayi%2)+ikilikSayi
        sayi = sayi//2
    
    print(ikilikSayi)
        #0010011100110000
    counter += 1

# Kendi rastgele oluşturduğumuz sayfa tablomuz.
page = [9, 1, 14, 10, 11, 13, 8, 15, 3, 0, 5, 4 , 3, 3, 2,16,21,19,18,7,2,21,5,8,9,6,3,2,15,4,8,9,6,3] 



print("\n ##### SAYFALAMA HESAPLAYICI ##### \n")

counter =0
while counter <=3:
    

    # Request input
    kb = 4
    virtual_address = kalan[counter]
    
    # Operating functions
    page_kd = (kb * 1024)
    virtual_page_number = (int(virtual_address) / page_kd)
    #sanal sayfa numarası
    offset = (int(virtual_address) % page_kd)
    #sayfa çerçevesi
    pageFrame=page[int(virtual_page_number)]
    sayfaAdresi=(page_kd*pageFrame)-1
    fizikselAdres=sayfaAdresi+offset
    
    # Display operations
    print("\n ##### İşlemler ##### \n")
    
    print(" Note: 1kb = 1024\n")
    print(" boyut: "+str(kb)+"kb ve sanal adres - "+str(virtual_address))
    print(" "+str(virtual_address)+"/"+str(kb)+"k")
    print(" "+str(virtual_address)+"/"+str(page_kd)+" = "+str(int(virtual_page_number))+" rem "+str(offset))
    
    # Display result
    print("\n ##### Answer ##### \n")
    print(" Sanal sayfa numarası = " + str(int(virtual_page_number)))
    print(" Offset = " + str(offset))
    
    print("Sayfa Çerçevesi: ", str(pageFrame))
    print("Sayfa Adresi: ", str(sayfaAdresi))
    print("Fiziksel Adres: ", str(fizikselAdres))
    
    print("")
    print("")
    counter+=1





# Sistemden çıkış methodu
ExitOS()