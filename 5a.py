print("MENGECEK KELULUSAN")
jwb = "y"
while jwb.lower() == "y":
    n = input("Masukan nilai =") 
    if int(n) > 60:
        status = "Lulus"
    else:
        status = "Ulang" 
    print(status)

    jwb = input("Input Lagi y/t")
    if jwb.lower() == "t":
        print(jwb)
        break