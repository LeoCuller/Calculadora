print ('BEM VINDO A SUA CALCULADORA!!!!!!')


# função para adição

def adicao(n1,n2):
    return n1 + n2

# função para subtração

def subtracao(n1,n2):
    return n1 - n2

# função para multiplicação

def multiplicacao(n1,n2):
    return n1 * n2

# função para divisão

def divisao(n1,n2):
    return n1 / n2




operação = input('''
        Escolha a operação que deseja realizar
        + para adição
        - para subtração
        * para multiplicação
        / para divisão
        Sair para sair
        
        
          ''')


while operação != "sair":   
    
    
    n1 = int(input('Digite seu primeiro numero: '))
    n2 = int(input('Digite seu segundo numero: '))

    # Adição
    if operação == '+':
        print(adicao(n1,n2))

    # Subtração

    elif operação == '-':
        print(subtracao(n1,n2))

    # Multiplicação

    elif operação == '*':
        print(multiplicacao(n1,n2))

    # Divisão    
    elif operação == '/':
        print(divisao(n1,n2))
    
    else: ('saindo do loop')
    
    
    operação = input('''
        Escolha a operação que deseja realizar
        + para adição
        - para subtração
        * para multiplicação
        / para divisão
        Sair para sair
        
        
          ''')

        
        
        
    

