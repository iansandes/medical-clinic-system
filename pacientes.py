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
    import pickle
    lista_pacientes = pickle.load(open('dados_pacientes.txt', 'rb'))
    print(lista_pacientes)

def menu():
    import pickle
    dados_pacientes = []
    while True:
        print('''1 - Cadastrar novo paciente
        2 - Listar pacientes
        3 - Sair
        ''')
        opcao = int(input('Selecione uma opção: '))
        if opcao == 1:
            pickle.dump(cadastro(), open('dados_pacientes.txt', 'wb'))
        elif opcao == 2:
            listar_pacientes()
        elif opcao == 3:
            break
        else:
            print("Opção inválida!")




