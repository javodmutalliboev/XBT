from definitions import Xodim

if __name__ == "__main__":
    tanlov = -1
    while tanlov:
        print("0. Chiqish;")
        print("1. Yangi xodim qo'shish;")
        print("2. Xodimni olib tashlash;")
        print("3. Xodim lavozimini o'zgartirish;")
        print("4. Xodimlarni ko'rish;")

        tanlov = int(input("Tanlovingizni kiriting: "))

        Xodim.terminalga_chiqarish()
        # Xodim.terminalga_chiqarish2()
        xodim = Xodim("John", "Doe")
        xodim.terminalga_chiqarish2()

        match tanlov:
            case 0:
                tanlov = 0
            case 1:
                Xodim.qoshish()
            case 4:
                Xodim.royxat()
            case _:
                print("Mavjud bo'lmagan tanlov kiritdingiz")
