sayilar = ["mono", "di", "tri", "tetra", "penta", "hekza", "hepta", "okta", "nona", "deka"]
elementler = []
element_isimleri = []
formul = input("Formül gir: ")
t = ""
with open("elements.csv", "r", encoding="utf-8") as file:
    for satir in file.readlines():
        elementler.append(satir.split(";")[1].strip())
        element_isimleri.append(satir.split(";")[0].strip())
    elementler.pop(0)
    element_isimleri.pop(0)
i = 0
while i < len(formul):
    if formul[i].isupper():
        element = formul[i]
        if i + 1 < len(formul) and formul[i + 1].islower():
            element += formul[i + 1]
            i += 1
        if element in elementler:
            element_adi = element_isimleri[elementler.index(element)]
            if i + 1 < len(formul) and formul[i + 1].isdigit():
                numara = int(formul[i + 1])
                if numara <= len(sayilar):
                    t += sayilar[numara - 1] + " " + element_adi + " "
                i += 1
            else:
                t += element_adi + " "
    i += 1
print(t)