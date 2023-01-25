
print("----------------- Selamat Datang di TokoKita -----------------")
print(" PROMO HARI INI")
print("""
   ==========PROMOTIONAL ITEMS==========
    -----------------------------------
    |KODE| ITEMS         | HARGA         |
    --------------------------------------
    | 1  | SUSU          | Rp. 50.000,00 |
    | 2  | MASKER        | Rp. 25.000,00 |
    
    -----------------------------------
    """)

pembeli = input("Masukkan nama Pembeli: ")
print ("Nama Pembeli :", pembeli) 
data_belanja = []

all_items = [   { "item": "susu", "harga": 50000 }, {"item": "daging", "harga": 20000} , 
                {"item": "lampu","harga": 15000} , {"item": "masker", "harga": 25000}, 
                {"item": "apel", "harga": 30000} ]

promotional_items = [ { "item": "susu", "harga": 50000 }, {"item": "masker", "harga": 25000} ]

def itempromo():

   global totalpromo
   global qty
   global item
   print("""
    ==========PROMOTIONAL ITEMS==========
    -----------------------------------
    |KODE| ITEMS         | HARGA         |
    --------------------------------------
    | 1  | SUSU          | Rp. 50.000,00 |
    | 2  | MASKER        | Rp. 25.000,00 |
    
    
    -----------------------------------
    """)
   nomor=int(input("Masukan Pilihan: "))
   qty= int(input("Qty Promo: "))
   
   if nomor==1:
       totalpromo=qty*50000
       print (qty," SUSU = Rp", totalpromo)
       item=("MASKER")
   elif nomor==2:
       totalpromo=qty*25000
       print (qty," MASKER = Rp", totalpromo)
       item=("MASKER")
   else:
      print("Pilihan tidak ada, silahkan masukan lagi!!")
      itempromo()
   
def allitems():
   global totalitem
   global items
   global qtyitem
   print("""
    ========== ALL ITEMS =================
    -----------------------------------
    |KODE| ITEMS         | HARGA         |
    --------------------------------------
    | 1  | SUSU          | Rp. 50.000,00 |
    | 2  | DAGING        | Rp. 20.000,00 |
    | 3  | LAMPU         | Rp. 15.000,00 |
    | 4  | MASKER        | Rp. 25.000,00 |
    | 5  | APEL          | Rp. 30.000,00 |
    
    
    -----------------------------------
   """)
   nomor=int(input("Masukan Pilihan: "))
   qtyitem= int(input("Qty: "))

   if nomor==1:
       totalitem=qtyitem*50000
       print (qtyitem," SUSU = Rp", totalitem)
       items=(" SUSU")
   elif nomor==2:
       totalitem=qtyitem*20000
       print (qtyitem, " DAGING = Rp", totalitem)
       items=("DAGING")
   elif nomor==3:
       totalitem=qtyitem*15000
       print (qtyitem, " LAMPU = Rp", totalitem)
       items=("LAMPU")
   elif nomor==4:
       totalitem=qtyitem*25000
       print (qtyitem, " MASKER = Rp", totalitem)
       items=("MASKER")  
   elif nomor==5:
       totalitem=qtyitem*30000
       print (qtyitem, " APEL = Rp", totalitem)
       items=("APEL")       
   else:
      print("Pilihan tidak ada, silahkan masukan lagi!!")
      allitems()

itempromo()
allitems()
totalsemua= totalpromo + totalitem

print("\nTotal harus Dibayar: Rp",totalsemua)
uang=int(input("Uang Tunai Pembeli: Rp "))
kembalian=int(uang-totalsemua)
print("Kembalian :",kembalian)

print("\n=============================================")
print("========== S T R U K   B E L A N J A =========")
print("==============================================")
print ("Nama\t\t:",pembeli)
print ("Beli\t\t:",qty,item,"( Rp", totalpromo,")")
print ("\t\t ",qtyitem,items,"( Rp", totalitem,")")
print ("Tagihan\t\t: Rp",totalsemua)
print ("Dibayar\t\t: Rp",uang)
print ("Kembalian\t: Rp",kembalian)
print("==============================================")
print("==============================================")