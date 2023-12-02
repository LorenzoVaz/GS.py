import valida
import datetime
import os
from time import sleep
import locale

from agenda_medica import agenda_medica

locale.setlocale(locale.LC_TIME, 'pt_BR.utf8')

def limpaTerminal():              
    return os.system('cls' if os.name == 'nt' else 'clear')
    
def criaBarra():                  
    return print('-' * 32)
    
data = datetime.datetime.now()   
dia = data.day
mes = data.month
ano = data.year

def menu():
    print('==== <<<>>> ''\033[33;41m''Hapvida''\033[0;0m'' <<<>>> ====')
    print('|  [''\033[31;7m''1''\033[0;0m''] \33[37;7mCadastrar Cliente \33[m      |\n')
    print('|  [''\033[31;7m''2''\033[0;0m''] \33[37;7mTriagem \33[m               |\n')
    print('|  [''\033[31;7m''3''\033[0;0m''] \33[37;7mDados do Cliente \33[m       |\n')
    print('|  [''\033[31;7m''4''\033[0;0m''] \33[37;7mPlano de Saude  \33[m        |\n')
    print('|  [''\033[31;7m''5''\033[0;0m''] \33[37;7mAgendar Consulta \33[m       |\n')
    print('|  [''\033[31;7m''6''\033[0;0m''] \33[37;7mMostrar Clientes \33[m       |\n')
    print('|  [''\033[31;7m''7''\033[0;0m''] \33[37;7mGerar Relatório  \33[m       |\n')
    
    print('|  [''\033[31;7m''0''\033[m''] \33[37;7m Sair  \33[m                 |')
    print('--------------------------------')
    x = input('\033[33;41m''Insira a opção: ''\033[0;0m')
    print('--------------------------------')
    return x


'''def triagem'''
def triagem():
    limpaTerminal()
    criaBarra()
    print('\033[1;33m''Bem-vindo à Triagem!''\033[0;0m')
    criaBarra()

    print('Por favor, responda algumas perguntas para realizar a triagem:')

    sintomas = input('Descreva brevemente seus sintomas: ')
    
    print('\nAgora, avalie a gravidade dos seus sintomas de 1 a 10:')
    gravidade = input('Em uma escala de 1 (leve) a 10 (grave), quão grave são seus sintomas? ')

    gravidade = int(gravidade)
    
    if gravidade <= 5:
        print('\nSeus sintomas são leves. Recomendamos monitorar sua condição.')
    elif 5 < gravidade <= 8:
        print('\nSeus sintomas são moderados. Pode ser útil procurar aconselhamento médico.')
    else:
        print('\nSeus sintomas são graves. Recomendamos buscar atendimento médico imediatamente.')

    criaBarra()
    sleep(2)  


'''def de Cadastrar / Checar login existente / Adicionar dados no arquivo txt de logins'''
def cadastro():
    limpaTerminal()
    print('==== < ''\033[1;31m''Cadastrar Usuário''\033[0;0m'' > =====')
    nome  = valida.Nome()    
    login = valida.Login()   
    
    # --> Conferir se já existe o login cadastrado
    lerlogins = open('logins.txt', 'r')
    for linha in lerlogins.readlines():   
        
        valores = linha.split('-')
       
        
        if login == valores[1].split(':')[1].strip():  
       
        
            limpaTerminal()
            criaBarra()
            print('\033[1;31m''Login já existente!''\033[0;0m')    
            criaBarra()
            return
        
       
                                
    lerlogins.close()
    
    idade = valida.Idade()
    data  = valida.Data() 
    rg = valida.Rg()
    cpf = valida.Cpf()
    ps = valida.PS()  
    senha = valida.Senha()   
    email = valida.Email()      
    tele  = valida.tele()    
    ender = valida.ender() 
    
    
    limpaTerminal()
    criaBarra()
    print('\033[1;31m''Cliente Cadastrado com sucesso!''\033[0;0m')
    criaBarra()
            
    # --> Adiciona dados no banco de dados login.txt
    logins = open("logins.txt", 'a')
    logins.write(f'Nome: {nome}  -Idade:{idade} -Rg:{rg} -Cpf:{cpf} -Data de Nascimento:{data}  -Email: {email}  -Numero de celular: {tele} -Endereco:{ender}  Plano de saude:{ps}  -Login: {login} -Senha: {senha}\n')
    logins.close()
    return 

'''Logar um usuário e printar seus dados cadastrados'''
def mostraDados():
    
    limpaTerminal() 
    print('==== << ''\033[1;33m''Dados do Cliente''\033[0;0m'' >> ====')
    criaBarra()
    print('\033[1;33m''Logue para acessar seus dados!''\033[0;0m')
    criaBarra()
    
    userlogin = input('Login: ')       
    usersenha = input('Senha: ')      
            
    valida = False                     # Variavel de validação do login
    logins = open('logins.txt', 'r')   
    for linha in logins.readlines():   # Percorre cada linha do logins.txt
        valores = linha.split('-')
        if userlogin == valores[1].split(':')[1].strip() and usersenha in valores[2].split(':')[1].strip():
            
            # Checa se login e senha são iguais no Logim e Senha da linha
            limpaTerminal()
            criaBarra()
            print('\033[1;31m''Cliente Logado! Dados do usuário: ''\033[0;0m')
            criaBarra()                
            
            for percorre in range(len(valores)):  
           
                
                if valores[percorre].split(':')[0] == 'Endereco': 
                
                    
                    dictEndereco = eval(valores[percorre].split('Endereco:')[1])
                    
                    
                    for chave in dictEndereco:
                        print(f'{chave}: {dictEndereco[chave]}')
                        sleep(0.2)
                
                else:
                    print(valores[percorre])
                    sleep(0.2)
            
            criaBarra()
            valida = True    
            logins.close()
            break
    
    if not valida:
        limpaTerminal()
        criaBarra()
        print('\033[1;31m''Erro! Login ou senha inválidos''\033[0;0m')  
        criaBarra()


'''def para exibir todos os clientes ja cadastrados'''        
def clientesCadastrados():
    limpaTerminal()
    print('===== Clientes Cadastrados =====')
    logins = open('logins.txt', 'r')
    for linha in logins.readlines():    
       
        l = linha.split('-')            
       
        print('\33[33m'f'{l[0]} | {l[1]}''\033[0;0m') 
        
    criaBarra()
    return 

'''def para exibir o plano de saude '''
def PlanoSaude():
    limpaTerminal()
    print('\033[33;7m ===== Plano de saude =====\33[m\n')
    print('\33[31m DIFERENCIAIS\33[m')
    print('\33[33m-REDE EXCLUSIVA,Com 32 Hospitais próprios, 20 Prontos atendimentos e 105 Clínicas, o Hapvida conta com uma completa estrutura à sua disposição.\33[m\n')
    print('\33[33m-ODONTOLOGIA INCLUÍDA, Só no Hapvida você tem um plano completo de odontologia incluído, com prevenção, diagnóstico, urgência 24h e cobertura em todo Brasil.\33[m\n')
    print('\33[33m-CONTACT CENTER 24h, Sem perda de tempo: a sua saúde não espera. Marcação de consulta, exames e autorização via call center exclusivo\33[m\n')
    print('\33[33m-MAIOR REDE, EXCLUSIVA PEDIÁTRICA. A maior rede exclusiva de atendimento infantil com infraestrutura moderna e especializada, UTI neonatal e acompanhamento pediátrico.\33[m\n')
    print('\33[33m-SITE HAPVIDA, Agendamento de consultas, autorização online e tira dúvidas direto pelo chat são alguns serviços oferecidos em nosso site.\33[m\n')
    
'''def para criar relatorio conforme exemplo pedido'''
def relatorio():
    
    countClient = 0    
    nomess = []       
    
    logins = open('logins.txt', 'r')
    for linhas in logins.readlines():
        l = linhas.split('-')              
        nomess.append(l[0])                
        countClient += 1         
     
    limpaTerminal()                      
    arquivo = open("dados.txt", "w+")             # "w+" para criar o relatorio 
    arquivo.write('Relatorio de Clientes \n')
    arquivo.write('\n')
    arquivo.write(f'A   empresa Hapvida possui {countClient} cliente(s) \n')
    
    for i in range(len(nomess)):               
        arquivo.write(str(f'{i + 1}.{nomess[i].split(":")[1]} \n'))    
    arquivo.write(f'R. Dr. Renato Paes de Barros, 955, {dia}/{mes}/{ano}.')  
    criaBarra()
    print('\33[33m'"Relatorio gerado em 'dados.txt'"'\033[0;0m')
    criaBarra()
    arquivo.close()
    return 

'''def para consultas '''
locale.setlocale(locale.LC_TIME, 'pt_BR.utf8')
class Validador:
    def DataC(self):
        # Lógica para validar a data
        # Retorna a data validada
        pass

def agendar_consulta():
    try:
        print("Especialidades disponíveis:")
        for num, especialidade in enumerate(agenda_medica.keys(), start=1):
            print(f"{num}. {especialidade}")

        escolha_numero = int(input("Escolha o número da especialidade da consulta: "))

        if escolha_numero < 1 or escolha_numero > len(agenda_medica):
            raise ValueError("Número de especialidade inválido")

        especialidade_escolhida = list(agenda_medica.keys())[escolha_numero - 1]

        print(f"Médicos disponíveis em {especialidade_escolhida}:")
        for num, medico in enumerate(agenda_medica[especialidade_escolhida].keys(), start=1):
            print(f"{num}. {medico}")

        escolha_numero = int(input("Escolha o número do médico da consulta: "))

        if escolha_numero < 1 or escolha_numero > len(agenda_medica[especialidade_escolhida]):
            raise ValueError("Número de médico inválido")

        medico_escolhido = list(agenda_medica[especialidade_escolhida].keys())[escolha_numero - 1]
        
        dataC = valida.DataC()

        print(f"Horários disponíveis para {medico_escolhido}:")
        for horario in agenda_medica[especialidade_escolhida][medico_escolhido]:
            print(f"- {horario}")
            
        

        horario_escolhido = input("Escolha o horário da consulta (no formato HH:MM): ")

        if horario_escolhido not in agenda_medica[especialidade_escolhida][medico_escolhido]:
            raise ValueError("Horário inválido")

        

        print(f"Consulta agendada com o(a) {medico_escolhido} em {dataC} às {horario_escolhido}.")

    except ValueError as e:
        print(f"Erro: {e}")

    return

