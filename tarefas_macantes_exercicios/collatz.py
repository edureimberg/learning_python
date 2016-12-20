def verifica_num(numero):
    if numero % 2 == 0:
        return numero // 2
    else:
        return 3 * numero + 1
    
num = input('Digite o numero desejado: ')

try:
    while True:
        num = verifica_num(int(num))
        print(num)
        if num == 1:
            break
except ValueError:
    print('Digite um inteiro!')