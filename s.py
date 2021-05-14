try:
    sayı1 = int(input("Sayı gir"))
    sayı2 = int(input("sayı gir"))

    toplam = sayı1+sayı2
    print(toplam)

except ValueError:
    print("sa")

finally:
    print("f")