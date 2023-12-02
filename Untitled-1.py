

import defs

defs.limpaTerminal()

while True:
    
    escolha = defs.menu()

    if escolha == '1':
        defs.cadastro()
    elif escolha == '2':
        defs.triagem()
    elif escolha == '3':
        defs.mostraDados()
    elif escolha == '4':
        defs.PlanoSaude()
    elif escolha == '5':
        defs.agendar_consulta()
    elif escolha == '6':
        defs.clientesCadastrados()
    elif escolha == '7':
        defs.relatorio()
    elif escolha == '0':
        print('\033[1;31m''Agradecemos por nos escolher para cuidar da sua saúde. Até logo e continue trilhando o caminho do bem-estar com o Hapvida!''\033[0;0m')
        break
    else:
        defs.limpaTerminal()
        defs.criaBarra()
        print('\033[1;31m''Insira uma opção válida!''\033[0;0m')
        defs.criaBarra() 