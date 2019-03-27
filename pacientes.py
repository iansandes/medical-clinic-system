import json



def cadastro():
        dados = {}
        dados['name'] = input('Nome: ')
    #    dados['email'] = input('Email:')
    #   dados['phone'] = input('Telefone: ')
    #    dados['rg'] = input('RG: ')
    #    dados['cpf'] = input('CPF: ')
    #    dados['number'] = input('Endereço: ')
    #    dados['address'] = input('número: ')
    #    dados['hood'] = input('Bairro: ')
    #    dados['city'] = input('Cidade: ')
    #    dados['estado'] = input('UF: ')
    #    dados['plano'] = input('Plano de saúde: ')
        return dados


def listar_pacientes():
    lista_pacientes = json.load(open('dados_pacientes.json', 'r'))
    print(lista_pacientes)

def menu():
    while True:
        print('''1 - Cadastrar novo paciente
2 - Listar pacientes
3 - Sair
        ''')
        opcao = int(input('Selecione uma opção: '))
        if opcao == 1:
            pacientes = json.loads(open('dados_pacientes.json', 'r').readlines())
            with open('dados_pacientes.json', mode='w') as dados_pacientes:
                pacientes.append(cadastro())
                x = json.dumps(pacientes)
                dados_pacientes.write(x)


        elif opcao == 2:
            listar_pacientes()
        elif opcao == 3:
            break
        else:
            print("Opção inválida!")