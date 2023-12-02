import defs


def Nome():
    while True:
        nome = input('Nome Completo: ')
        if nome == '':
            print('Error! Entrada vazia.')
            continue
        temp = ''.join(nome.split(' '))
        for i in temp:
            if i.isdigit():
                print('Digite um nome valido.')
                break
        else:
            return nome.strip(' ')


def Idade():
    while True:
        idade = input('Idade: ')
        if idade == '':
            print('Error! Entrada vazia.')
            continue
        return idade.strip(' ')                    
        
def Data():
    while True:  
        data = input('Nascimento (dd/mm/aaaa): ')
        if data == '':
            print('Error! Entrada inválida.')
            continue        
        temp = ''.join(data.split('/'))
        if not temp.isnumeric():             
            print('Insira uma data válida')
            continue
        
        if data.count('/') == 2 and data != '//':   
            dia, mes, ano = data.split('/')  
            if 1 <= int(dia) <= 31 and 1 <= int(mes) <= 12 and 1900 <= int(ano) <= 2022:
                return data.strip(' ')
            else:
                print('Dia/Mes/Ano Inválido(s)')
        else:
            print('A data deve seguir o padrão dd/mm/aaaa') 

def Rg():
    while True:
        rg = input('RG (Apenas Números): ')
        if rg == '':
            print('Error! Entrada vazia.')
            continue
        elif not rg.isnumeric():
            print('Insira apenas números.')
            continue   
        else:
            if 7 <= len(rg) <= 11:
                return rg
            else:
                print('O número deve ter entre 7 - 11 caracteres.')  
                
def Cpf():
    while True:
        cpf = input('CPF (Apenas Números): ')
        if cpf == '':
            print('Error! Entrada vazia.')
            continue
        elif not cpf.isnumeric():
            print('Insira apenas números.')
            continue   
        else:
            if 11 <= len(cpf) <= 11:
                return cpf
            else:
                print('O número deve ter 11 caracteres.')                 
                          
def Email():
    while True:
        email = input('Email: ')
        if email == '':
            print('Error! Entrada vazia.')
        elif '@' and '.com' in email:
            return email.strip(' ')
        else:
            print('Email Inválido! Deve conter "@" e ".com"')  
            
def PS():
    while True:
        ps = input('Contem um Plano de saude: ')
        if ps == '':
            print('Error! Entrada vazia.')
            continue
        temp = ''.join(ps.split(' '))
        for i in temp:
            if i.isdigit():
                print('Digite um Plano de saude valido.')
                break
        else:
            return ps.strip(' ')
        
def Sintomas():
    while True:
        sintomas = input('Sintomas: ')
        if sintomas == '':
            print('Error! Entrada vazia.')
            continue
        return sintomas.strip(' ')
                            
def Login():
    while True:
        login = input('Login (numero da carterinha): ')
        if login == '':
            print('Error! Entrada vazia.')
            continue
        return login.strip(' ')
    
def Senha():
    while True:
        senha = input('Senha : ')
        if senha == '':
            print('Error! Entrada vazia.')
            continue
        return senha.strip(' ')
        
def tele():
    while True:
        tele = input('Telefone (Apenas Números): ')
        if tele == '':
            print('Error! Entrada vazia.')
            continue
        elif not tele.isnumeric():
            print('Insira apenas números.')
            continue   
        else:
            if 9 <= len(tele) <= 11:
                return tele
            else:
                print('O número deve ter entre 9 - 11 caracteres.')

def ender(): 
    while True:
        print('=== < ''\033[31m''Seu Endereço Completo!''\033[0;0m'' > ===')
        dados = {
            'Rua': input('Rua: '),
            'Numero': input('Numero: '),
            'CEP': input('CEP: '),
            'Cidade': input('Cidade: '),
            'Estado': input('Estado: '),
        }   

        return dados


def DataC():
    while True:  
        dataC = input('Data Consulta (dd/mm/aaaa): ')
        if dataC == '':
            print('Error! Entrada inválida.')
            continue        
        temp = ''.join(dataC.split('/'))
        if not temp.isnumeric():             
            print('Insira uma data válida')
            continue
        
        if dataC.count('/') == 2 and dataC != '//':   
            dia, mes, ano = dataC.split('/')  
            if 1 <= int(dia) <= 31 and 1 <= int(mes) <= 12 and 1900 <= int(ano) <= 2024:
                return dataC.strip(' ')
            else:
                print('Dia/Mes/Ano Inválido(s)')
        else:
            print('A data deve seguir o padrão dd/mm/aaaa') 