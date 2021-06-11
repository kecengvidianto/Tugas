print("Penilian Mahasiswa")
jwb = "y"
while jwb.lower() == "y":  
    i = int(input("Masukan bilangan = "))
    if i >= 91 and i < 100:
            print('A')
    elif i >= 81 and i < 91:
            print('B')
    elif i >= 71 and i < 81:
            print('C')
    elif i < 71:
            print('D')
   
    jwb = input("Input lagi y/t")
    if jwb.lower() == "t":
        break
    