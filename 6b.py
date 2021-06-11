print("Hitung total nilai transaksi pembelian printer eposn t20 harga 660000")
epsonPrint = 660000
jumlah = int(input("Masukan jumlah barang = "))
hasil =  jumlah * epsonPrint
if hasil > 1500000 :
    hasil = hasil * 15/100
print("Total Harga Rp ",hasil)
