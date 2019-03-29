import json


def cadastro():
        dados = {}
        dados['name'] = input('Nome: ')
        dados['email'] = input('Email:')
        dados['phone'] = input('Telefone: ')
        dados['rg'] = input('RG: ')
        dados['cpf'] = input('CPF: ')
        dados['number'] = input('Endereço: ')
        dados['address'] = input('Número: ')
        dados['hood'] = input('Bairro: ')
        dados['city'] = input('Cidade: ')
        dados['state'] = input('UF: ')
        dados['plan'] = input('Plano de saúde: ')
        return dados


def cadastrar_paciente():
    try:
        with open('dados_pacientes.json') as pacientes:
                    antigos_pacientes = json.load(pacientes)
        with open('dados_pacientes.json', mode='w') as dados_pacientes:
                    antigos_pacientes.append(cadastro())
                    novos_pacientes = json.dumps(antigos_pacientes)
                    dados_pacientes.write(novos_pacientes)
    except:
        with open('dados_pacientes.json', mode='w') as dados_pacientes:
                    novos_pacientes = []
                    novos_pacientes.append(cadastro())
                    pacientes = json.dumps(novos_pacientes)
                    dados_pacientes.write(pacientes)


def listar_pacientes():
    try:
        with open('dados_pacientes.json',) as dados_pacientes:
            lista_pacientes = json.load(dados_pacientes)
            print('Pacientes\n')
            for paciente in lista_pacientes:
                print(paciente['name'])
        print('-'*20)
    except:
        print('Nenhum paciente encontrado!')
        menu_pacientes()


def menu_pacientes():
    while True:
        print('''1 - Cadastrar novo paciente
2 - Listar pacientes
3 - Sair
        ''')
        opcao = int(input('Selecione uma opção: '))
        if opcao == 1:
            cadastrar_paciente()
        elif opcao == 2:
            listar_pacientes()
        elif opcao == 3:
            from menu_principal import menu_principal
            menu_principal()
        else:
            print("Opção inválida!")