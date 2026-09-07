# Type Casting = proses mengkonversikan variable dari tipe data ke tipe data lain
#                str() int() float() bool()
# Nabil
# 07-09-2026

Nama = "Nabil"
Umur = 17
Ipk = 3.5
is_student = True

print(type(Nama)) #str
print(type(Umur)) #int
print(type(Ipk))  #float
print(type(is_student)) #bool
print()

Ipk = int(Ipk)

print(Ipk) #INI KONVERSI FLOAT KE INT
print()

Umur = float(Umur)
print(Umur) #INI KONVERSI INT KE FLOAT
print()

Nama = bool(Nama) #jika variable nama kosong maka boolean akan bernilai false 
                   #jika tidak kosong maka boolean akan bernilai true
print(Nama) #INI KONVERSI STR KE BOOL