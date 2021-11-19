bil1 = int(input("Masukkan bilangan pertama: "))
bil2 = int(input("Masukkan bilangan kedua: "))
kalimat = str(input("Masukkan kalimat: "))

if kalimat == ("Brendi meminta anda mengkalikan kedua bilangan itu"):
    print ("Hasil perkalian", float(bil1) ,"dengan", float(bil2) ,"adalah", float(bil1*bil2) ,)

elif kalimat == ("Halo programku! Tolong kurangkan bilangan pertama dengan bilangan kedua"):
    print ("Hasil pengurangan", float(bil1) ,"dengan", float(bil2) ,"adalah", float(bil1-bil2) ,)

elif kalimat == ("Berapakah hasil pembagian kedua bilangan diatas"):
    print ("Hasil pembagian", float(bil1) ,"dengan", float(bil2) ,"adalah", float(bil1/bil2) ,)

elif kalimat == ("Bisa gak aku minta tolong untuk tambahin 2 bilangan ini?"):
    print ("Hasil penjumlahan", float(bil1) ,"dengan", float(bil2) ,"adalah", float(bil1+bil2) ,)

else:
    print("error")
    