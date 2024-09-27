def main():
    money_due = 50                          #estabelecer o valor de uma cola
    while True:                             #mecanismo para repetir ate comprar a cola e ai dar break e terminar
        print ("Amount Due:", money_due)
        coin = int(input("Insert Coin: "))
        if coin in [5, 10, 25]:             #verificar se a moeda e aceitada, caso nao volta-se a pedir moeda
            money_due -= coin
            
            if money_due <= 0:              #verificar se se pagou a cola na totalidade e indicar o troco e break,
                print ("Change Owed:", -money_due)                           #caso nao volta-se a pedir moeda
                break
            else:
                continue
        else:
            continue

main()
