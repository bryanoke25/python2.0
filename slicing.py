from random import randint,choice


fullname = "Bryan Oke".lower()

split_names = fullname.split(" ")
firstname = split_names[0]
lastname = split_names[1]

cmb1 = firstname[:3] + lastname[-2:]
print(cmb1)

cmb2 = firstname[:] + str(randint(1, 1000))
print(cmb2)

characters = [ '!', '£', '$', '%', '^', '&', '*', '()', '-' ]
cmb3 = lastname[: :-1]  + choice(characters)
print(cmb3)