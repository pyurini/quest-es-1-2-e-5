def fibonaci(n):
    a , b = 0 , 1
    if n == a or n == b:
        return True
    
    while True:
        proximo_numero = a + b
        if proximo_numero == n:
            return True
        elif proximo_numero > n:
            return False
        a, b = b, proximo_numero

numero_escolhido = int(input())

if fibonaci(numero_escolhido) == True:
    print(f'o numero {numero_escolhido} ta na sequencia')
else:
    print(f'o numero {numero_escolhido} não ta na sequencia')