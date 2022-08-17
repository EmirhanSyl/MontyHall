import random

host_can_open = 2
car_can_appear = 3
contestant_can_select = 3

doors = [1, 2, 3]
selectedDoor = random.choice(doors)
openedDoor = random.choice(doors)

while openedDoor == selectedDoor:
    openedDoor = random.choice(doors)
    break



# Arabanın 1 numarada olma ihtimalini bul P(A)
1 / car_can_appear

# Sunucunun 2 numarada Keçi olan kapıyı açma ihtimalini bul |
# P(B) = P(A,B) + P(NA,B) => hem 1 numarada araba olup hem 2 numarada sunucunun keçi çıkarma ihtimali +
# hem 1 numarada araba olmayıp hem sunucunun 2'den keçi çıkartma ihtimali




