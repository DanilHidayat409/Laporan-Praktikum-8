# -*- coding: utf-8 -*-
"""
@judul : menentukan numerical number
@hari/tanggal : 20211411
@nim : 065002100032
@author : Muhammad Danil Hidayat
"""

jawab = -1 

while (jawab == -1):
    hasil = int(input("masukan angka nya: "))
    
    

    def cekangka(hasil):
    
      if hasil == 1  or hasil == 11 or hasil == 31 or hasil == 41  :
        print(hasil,"ST")
        
      elif hasil == 2 or hasil == 22 or hasil == 32 or hasil == 42 :
        print(hasil,"ND")
        
      elif hasil == 3 or hasil == 13 or hasil == 23 or hasil == 43 :
        print(hasil,"RD")
        
      elif (hasil <= 50):
        print(hasil,"TH")
       
      else:
        print("tolong masukan angka yang pasti")
        
        
    cekangka(hasil)

