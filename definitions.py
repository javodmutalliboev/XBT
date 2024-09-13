class Shaxs:
    def __init__(shaxs, ism, familiya):
        shaxs.ismi = ism
        shaxs.familiyasi = familiya


class Xodim(Shaxs):
    id = -1
    lavozimi = ""

    def __str__():
        pass

    def terminalga_chiqarish2(xodim):
        print(f"Xodim: {xodim.ismi} {xodim.familiyasi}")

    def terminalga_chiqarish():
        print("Class methodi")

    @staticmethod
    def royxat():
        try:
            xodimlar_file = open("xodimlar.dat", "rb")
            for xodim in xodimlar_file.readlines():
                print(xodim.decode("utf-8"), end="")
        except Exception as istisno:
            print(istisno)

    @staticmethod  # decorator
    def qoshish():
        try:
            ism = input("Yangi xodim ismi: ")
            familiya = input("Yangi xodim familiyasi: ")
            yangi_xodim = Xodim(ism, familiya)
            yangi_xodim.lavozimi = input("Yangi xodim lavozimi: ")

            try:
                xodimlar_file = open("xodimlar.dat", "rb")
                oxirgi_xodim = xodimlar_file.readlines()[-1].decode("utf-8").strip()
                xodimlar_file.close()
                id = int(oxirgi_xodim.split(",", 1)[0]) + 1
            except FileNotFoundError:
                id = 1
            except Exception as istisno:
                print(istisno)

            yangi_xodim.id = id

            xodimlar_file = open("xodimlar.dat", "ab")
            xodimlar_file.write(
                f"{yangi_xodim.id},{yangi_xodim.ismi},{yangi_xodim.familiyasi},{yangi_xodim.lavozimi}\n".encode(
                    "utf-8"
                )
            )
            print("Yangi xodim muvaffaqiyatli qo'shildi.")
            xodimlar_file.close()

        except Exception as istisno:
            print(istisno)

    def __str__(xodim):
        return f"Xodim: {xodim.ismi} {xodim.familiyasi}, {xodim.lavozimi}"

    def olib_tashlash(xodim):
        pass

    def lavozimini_ozgartirish(xodim):
        pass
