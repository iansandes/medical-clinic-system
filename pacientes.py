import json


def cadastro():
        dados = {}
        dados['name'] = input('Nome: ')
        dados['email'] = input('Email:')
        dados['phone'] = input('Telefone: ')
        dados['rg'] = input('RG: ')
        dados['cpf'] = input('CPF: ')
        dados['number'] = input('Endereço: ')
        dados['address'] = input('número: ')
        dados['hood'] = input('Bairro: ')
        dados['city'] = input('Cidade: ')
        dados['estado'] = input('UF: ')
        dados['plano'] = input('Plano de saúde: ')
        return dados


def listar_pacientes():
    lista_pacientes = json.load(open('dados_pacientes.json', 'r'))
    print('Pacientes\n')
    for i in range(len(lista_pacientes)):
        print(lista_pacientes[i]['name'])
    print('-'*20)

def menu():
    while True:
        print('''1 - Cadastrar novo paciente
2 - Listar pacientes
3 - Sair
        ''')
        opcao = int(input('Selecione uma opção: '))
        if opcao == 1:
            try:
                with open('dados_pacientes.json') as pacientes:
                    antigos_pacientes = json.loads(pacientes.read())
                with open('dados_pacientes.json', mode='w') as dados_pacientes:
                    antigos_pacientes.append(cadastro())
                    x = json.dumps(antigos_pacientes)
                    dados_pacientes.write(x)
            except:
                with open('dados_pacientes.json', mode='w') as dados_pacientes:
                    novos_pacientes = []
                    novos_pacientes.append(cadastro())
                    x = json.dumps(novos_pacientes)
                    dados_pacientes.write(x)

        elif opcao == 2:
            listar_pacientes()
        elif opcao == 3:
            break
        else:
            print("Opção inválida!")