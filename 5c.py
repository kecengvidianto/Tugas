print("Menampilkan nilai huruf dengan menginputkan sebuah bilangan antara 1 - 100")
jwb = "y"
while jwb.lower() == "y":  
    i = int(input("Masukan bilangan antara 1 - 100 "))
    if i in range(1,101):    
        if i > 80:
                print('Baik Sekali')
        elif i >= 65:
                print('Baik')
        elif i >= 55:
                print('Cukup')
        elif i >= 45:
                print('Kurang')
        else:
                print('Kurang Sekali')

        jwb = input("Input lagi y/t")
        if jwb.lower() == "t":
            break
    else:
        print("Hanya bilangan 1 - 100")