print("vailolluon")
from fractions import*

#cong so thap phan va tu rut gon
frac1 = Fraction(6,9)
frac2 = Fraction(5,10)
frac3 = frac1 + frac2
print(frac3)

c = complex(2,5)  #;;;;;;

print(c.real)   #lay phan thuc
print(c.imag)   #lay phan ao
#so thuc va so ao
kk = '''v'lol"\nconketnhincc'''
print(kk)

#nhinconcaknhincc

'''cailolma'''
print('\a')
#ra tieng bip \a
strA = "cc"
strB = " hung"
strC = strA*10 + strB*7
print(strC)
#cong chuoi
strA = "hungoccho"
strB = strA[1:len(strA) - 1]
strC = strB in strA
print(strB)
#hong biet
strA = "hungoccho"
strB = strA[None:5:-1]
strC = strB in strA
print(strB)
#gan gia trij them cho chuoi a la quyen
a = 'my name is %s %s'
result = a %('quyen','dz')
print(result)

#class something
# def_repr_(self)
#   return'day la _repr_'
#def_str_(self)
#   return'daay la _str_'
#_repr_ = %r
#_str_ = %s

k = 'chohung'
re = f'{k} mat day'
print(re)

name = 'chó hùng'
address = 'nhà thờ'
phone = 'pỏn hub'
re = f'name : {name}\naddress: {address}\nphone : {phone}'
print(re)

g1 = '+{:^2}'.format('')
print(g1) 

ac = '1222222'
print(int(ac))
print(type(ac))
#viet hoa chu cai dau tien
a = 'hungoccho'
b = a.capitalize()

print(a)
print(b)
#viet hoa het chu trong chuoi
a = 'hungoccho'
b = a.upper()

print(a)
print(b)
#vietb thuong het cac chu viet hoa
a = 'HUNGOCCHO'
b = a.lower()

print(a)
print(b)
#chu viet thuong thi viet ra chu viet hoa, nguoc lai]
a = 'OcchoQQ'
b = a.swapcase()

print(a)
print(b)
#vailol ko can biet cx dc 
a = 'OcchoQQ'
b = a.title()

print(a)
print(b)
#dua chu nam giua
a = 'OcchoQQ'
b = a.center(30, '*')

print(a)
print(b)
#can trai
a = 'OcchoQQ'
b = a.rjust(30, '*')

print(a)
print(b)
#can phai
a = 'OcchoQQ'
b = a.ljust(30, '*')

print(a)
print(b)
#ma hoa
a = 'dc'
b = a.encode(encoding='utf-8', errors='strict')

print(a)
print(b)
# ----------- #
a = 'có gì hót hùng ăn c'
b = a.encode()

print(a)
print(b)

a = 'có gì hót hùng ăn c'
b = a.join(['1','2','3'])

print(a)
print(b)
#thay the
a = 'có gì hót hùng ăn c'
b = a.replace('ó','lolhung')

print(a)
print(b)
#loai bo chu dau va cuoi----#
a = 'có gì hót hùng ăn c'
b = a.strip('c')

print(a)
print(b)
#loai bo ki tu dau
a = 'có gì hót hùng ăn c'
b = a.lstrip('c')

print(a)
print(b)
#cat chuoi----#
a = 'có gì hót hùng ăn c'
b = a.split('h')

print(a)
print(b)





