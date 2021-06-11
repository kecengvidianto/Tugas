print("MENGECEK TINGKAT USIA")

jwb = "y"
while jwb.lower() == "y":  
    n = int(input("Masukan usia ="))
    if int(n) > 60:
        status = "Lansia"
    elif int(n) >= 35 and int(n)<= 59:
        status = "Dewasa" 
    elif int(n) >= 18 and int(n)<= 34:
        status = "Pemuda" 
    elif int(n) >= 15 and int(n)<= 17:
        status = "Remaja"
    else:
        status = "Anak2" 
    print(status)

    jwb = input("Input lagi y/t")
    if jwb.lower() == "t":
        print(jwb)
        break