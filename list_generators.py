cars = ['легковая', 'джип', 'монстр трак', 'большой грузовик']
#Найти машину больше джипа и меньше грузовика
result = []
for car in cars:
    if car >'джип' and car <'большой грузовик':
        result.append(car)
print(result)

result = [for car in cars if car >'джип' and car <'большой грузовик']
print(result)

name = ['leo','max','kate','mag']

names_upper = [name.upper() for name in names]
print(names_upper)

names_m = [name for name in names if name[0]=='m']
print(names_m)

result = [1 if number >5 else 0 for number in numbers]
print(result)


ipmort hashlib
hash_object = hashlib.md5(b'Hello World')
print(hash_object.hexdigest())

