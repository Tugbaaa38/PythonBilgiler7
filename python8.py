#LISTE(list) 

#Listelerde tum veri tipleri bir arada bulunabilir.(int,float,string,bool)
#Bir liste olusturalim ve icinde tum veri tipleri bir arada bulunsun..
#Not: Liste oldugunu [] gordugumuzde anlayabiliriz.

myList=[3,7,24,"Tugba",5.8,True]
print(myList)  #Listemizdeki elemanlarin hepsini bu sekilde yazdirabiliriz.
#Peki listemizde belli bir indexdeki elemana nasil ulasiriz?
print(myList[0])
print(myList[1])
print(myList[2])              #Bu sekilde istedigimiz indexdeki elemana ulasabiliriz.
print(myList[3])
print(myList[4])
print(myList[5])
print(type(myList))           #Bize list turunde oldugunu soyleyecektir.

#Listelerde de istedigimiz elemanin degerini degistirebiliyoruz.Peki nasil?
myList[3]="Hasan"  #Listedeki 3.indexde bulunan "Tugba" stringi yerine "Hasan" stringini atadik.
print(myList)       #Listenin yeni hali 3,7,24,"Hasan",5.8,True olacaktir.

#LISTE METODLARI
#--->append() Listenin sonuna istedigimiz elemani ekler.
myList.append(18)  #veri tipi fark etmez.
myList.append("Silanur")
print(myList)

#--->insert() ise indexse gore eleman ekler.
myList.insert(2,"Can")  #kacinci indexe eklemek istiyorsak once indexi yazariz sonra ekleyecegimiz elemani.
print(myList)           #artik 2.indexde 'Can' var.

#--->pop() metodu listeden eleman siler.
myList.pop(4)           #pop metodunda silmek istedigimiz indexi yazariz.
print(myList) 
myList.pop()            #eger indexi belirtmezsek sondaki elemani silecektir.
print(myList)

#--->index() metodu ise aradigimiz elemanin kacinci indexde oldugunu soyler.
print(myList.index(3))   #ciktisi:0 

#--->count() metodu istedigimiz elemanin listede kac tane oldugunu bize sayar.
print(myList.count(7))   #ciktisi:1

#--->remove() metodu verdigimiz elemani siler.Burada pop() metodu ile karisabilir.
#Fakat pop() metodunun icinde indexe gore silme islemi yaparken remove() metodunda elemana gore silme islemi yapiyoruz.
myList.remove(True)
print(myList)            #Listeden True sildi.

#--->sort() metodu listeyi kucukten buyuge siralar.Burada string ifade kullanamayiz.
myList2=[5,8,15,3,1,9,45,65,38]
myList2.sort()
print(myList2)

myList3=["Hasan","Zeynep","Ali","Mahir"]
print(tuple(sorted(myList3)))    #Bu ifade ile Listeyi kucukten buyuge dogru siralayabiliriz.Alfabetik olarak..

#--->reverse() metodu da listeyi ters cevirmemizi saglar.
ornekListe=[1,2,3,4,5,6,"Tugba"]
ornekListe.reverse()
print(ornekListe)

ornekListe[::-1]   #remove metodu ile ayni ciktiyi bu sekilde de elde edebiliriz
print(ornekListe)

#--->copy() metodu adindan da anlasilacagi uzere listemizdeki elemanlari yedekler.
ogrenciler=["Tugba","Mahir","Hasret","Silanur","Hasan","Can"]
ogrenciler_yedek=ogrenciler.copy()
print(ogrenciler_yedek)

#--->extend() metodu sayesinde listemizde olmayan elemanlari ekleyebiliriz ve iki listeyi birlestirebiliriz.
ogrenciler.extend(["Melo","Fatmanur","Emine"])  #bu sekilde yapabiliriz. [] dikkat cunku liste eklemek zorundayiz..
print(ogrenciler)

# ya da su sekilde yapabiliriz:
eklenecek_ogrenciler=["Ali","Taha","Mustafa"]
ogrenciler.extend(eklenecek_ogrenciler)
print(ogrenciler)

#--->clear() metodu listedeki tum elemanlari siler..
myList.clear()
myList2.clear()
myList3.clear()
ogrenciler.clear()                        #Tum listeler temizlendi.
ornekListe.clear()
ogrenciler_yedek.clear()
eklenecek_ogrenciler.clear()

print(myList)            #ciktisi:  [] olacaktir.Cunku listemizdeki tum elemanlari sildik.
print(ogrenciler)
