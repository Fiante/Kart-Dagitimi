import random 
Item = ['Et', 'Gold', 'Kalkan', 'Kask', 'Kazan', 'Kılıç', 'Ok', 'Taç']
Karakter = ['Aeon', 'Bark', 'Boblin', 'Heliom', 'Leorio', 'Ren', 'Set', 'Vael', 'Vang', 'Veny']
ParaBirimi = ['Silver', 'Bronz']
while True:
    print("Tüm kartlar arasından sana gelenler")
    print(random.choice(Item))
    print(random.choice(Item))
    print(random.choice(ParaBirimi))
    print(random.choice(Karakter))
    print(random.choice(Karakter))
    print(random.choice(Karakter))
    input("Bi 6'lık daha istiyorsan enter'a bas")