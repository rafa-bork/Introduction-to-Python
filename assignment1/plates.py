def main():
    placa = input("Plate: ")
    valid = 1

    while True:
        if len(placa) < 2 or len(placa) > 6:                #tem de ter 2 a 6 caracteres
            valid = 0
            break

        if not placa.isalnum():                              #tem de ter letras e numeros
            valid = 0
            break

        if not placa[:2].isalpha():                          #tem de começar com 2 letras
            valid = 0
            break

        num = 0
        for char in placa:
            if char.isnumeric():                             #a num acompanha a ordem dos numeros na string
                num += 1

            if num > 1 and char.isalpha():                   #Apos numeros nao pode haver letras
                valid = 0
                break

            if num == 1 and char == "0":                     #nao pode tar 0 como primeiro numero
                valid = 0
                break
        break

    if valid == 1:
        print ("Valid")
    else:
        print ("Invalid")

main()
