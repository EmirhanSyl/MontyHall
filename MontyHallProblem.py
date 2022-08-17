import random
from time import sleep

doors = ["A", "B", "C"]
carDoorIndex = random.randint(0,2)
chosenDoor = ""

def FirstPhase():
    print("Yarışmaya Hoş Geldiniz! Lütfen bir kapı seçiniz...")
    print(" _____     _____     _____")
    print("|     |   |     |   |     |")
    print("|  A .|   |  B .|   |  C .|")
    print("|_____|___|_____|___|_____|")
    print()

    for x in doors:
        chosenDoor = input("Seçtiğiniz Kapı(A, B, C): ")
        if chosenDoor == x:
            break

    if chosenDoor == "A":
        print("A Kapısını Kitlediniz. Bol Şans!")
        print(" _____     _____     _____")
        print("|  ▽  |   |     |   |     |")
        print("|  A .|   |  B .|   |  C .|")
        print("|_____|___|_____|___|_____|")
        print()
        sleep(2)

        randomSelectedDoor = random.randint(1,2)
        if randomSelectedDoor == 1:
            print("B Kapısı Açılıyorr...!")
            print("3!")
            sleep(1)
            print("2!")
            sleep(1)
            print("1!")
            sleep(1)
            print(" _____     ___---    _____")
            print("|  ▽  |   |  |  |   |     |")
            print("|  A .|   |B.|  |   |  C .|")
            print("|_____|___|__|--| __|_____|")
            print()

        elif randomSelectedDoor == 2:
            print("C Kapısı Açılıyorr...!")
            print("3!")
            sleep(1)
            print("2!")
            sleep(1)
            print("1!")
            sleep(1)
            print(" _____     _____    ___---")
            print("|  ▽  |   |     |   |  |  |")
            print("|  A .|   |  B .|   |C.|  |")
            print("|_____|___|_____|___|__|--|")
            print()

        if carDoorIndex == randomSelectedDoor:
            print("Tebrikler! Arabayı Kaybettiniz Ancak Artık Bir Keçiye Sahipsiniz.1 Yıllık Yem Masrafınız da Bizden:)")
        else:
            SecondPhase()

    elif chosenDoor == "B":
        print("B Kapısını Kitlediniz. Bol Şans!")
        print(" _____     _____     _____")
        print("|     |   |  ▽  |   |     |")
        print("|  A .|   |  B .|   |  C .|")
        print("|_____|___|_____|___|_____|")
        print()
        sleep(2)

        randomSelectedDoor = random.randint(1, 2)
        if randomSelectedDoor == 1:
            print("A Kapısı Açılıyorr...!")
            print("3!")
            sleep(1)
            print("2!")
            sleep(1)
            print("1!")
            sleep(1)
            print(" ___---    _____    _____")
            print("|  |  |   |  ▽  |   |     |")
            print("|A.|  |   |  B .|   |  C .|")
            print("|__|--|___|_____|___|_____|")
            print()

        elif randomSelectedDoor == 2:
            print("C Kapısı Açılıyorr...!")
            print("3!")
            sleep(1)
            print("2!")
            sleep(1)
            print("1!")
            sleep(1)
            print(" _____     _____    ___---")
            print("|     |   |  ▽  |   |  |  |")
            print("|  A .|   |  B .|   |C.|  |")
            print("|_____|___|_____|___|__|--|")
            print()

        if carDoorIndex == 0 or carDoorIndex == 2:
            print(
                "Tebrikler! Arabayı Kaybettiniz Ancak Artık Bir Keçiye Sahipsiniz.1 Yıllık Yem Masrafınız da Bizden:)")
        else:
            SecondPhase()

    elif chosenDoor == "C":
        print("C Kapısını Kitlediniz. Bol Şans!")
        print(" _____     _____     _____")
        print("|     |   |     |   |  ▽  |")
        print("|  A .|   |  B .|   |  C .|")
        print("|_____|___|_____|___|_____|")
        print()
        sleep(2)

        randomSelectedDoor = random.randint(0, 1)
        if randomSelectedDoor == 0:
            print("A Kapısı Açılıyorr...!")
            print("3!")
            sleep(1)
            print("2!")
            sleep(1)
            print("1!")
            sleep(1)
            print(" ___---    _____    _____")
            print("|  |  |   |     |   |  ▽  |")
            print("|A.|  |   |  B .|   |  C .|")
            print("|__|--|___|_____|___|_____|")
            print()

        elif randomSelectedDoor == 1:
            print("B Kapısı Açılıyorr...!")
            print("3!")
            sleep(1)
            print("2!")
            sleep(1)
            print("1!")
            sleep(1)
            print(" _____     ___---    _____")
            print("|     |   |  |  |   |  ▽  |")
            print("|  A .|   |B.|  |   |  C .|")
            print("|_____|___|__|--| __|_____|")
            print()

        if carDoorIndex == randomSelectedDoor:
            print(
                "Tebrikler! Arabayı Kaybettiniz Ancak Artık Bir Keçiye Sahipsiniz.1 Yıllık Yem Masrafınız da Bizden:)")
        else:
            SecondPhase()


def SecondPhase():
    print("Tebrikler! Bir üst turdasınız")
    yesNo = ["0", "1"]
    decision = ""
    for x in yesNo:
        decision = input("Seçiminizi değiştirmek ister misiniz?(0 => Hayır, 1 => Evet): ")
        if chosenDoor == x:
            break

    print("SON Kapı Açılıyorr...!")
    print("3!")
    sleep(1)
    print("2!")
    sleep(1)
    print("1!")
    sleep(1)
    if chosenDoor == carDoorIndex:
        if decision == "0":
            print("Tebrikler! Arabayı kazandınızz ^^")
        else:
            print("Son Anda Arabayı Kaçırdınız! Ama Üzülmeyin Artık Bir Keçiye Sahipsiniz.1 Yıllık Yem Masrafınız da Bizden:)")
    else:
        if decision == "0":
            print("Son Anda Arabayı Kaçırdınız! Ama Üzülmeyin Artık Bir Keçiye Sahipsiniz.1 Yıllık Yem Masrafınız da Bizden:)")
        else:
            print("Tebrikler! Arabayı kazandınızz ^^")


if __name__ == "__main__":
    FirstPhase()


