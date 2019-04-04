import json


def coletar_informacoes():
        nome = input('Nome: ')
        email = input('Email:')
        telefone = input('Telefone: ')
        rg = input('RG: ')
        cpf = input('CPF: ')
        endereco = input('Endereço: ')
        numero = input('Número: ')
        bairro = input('Bairro: ')
        cidade  = input('Cidade: ')
        estado = input('UF: ')
        planoDeSaude = input('Plano de saúde: ')

        dados = dict(name=nome, email=email, phone=telefone, rg=rg,
                     cpf=cpf, address=endereco, number=numero,
                     hood=bairro, city=cidade, state=estado, plan=planoDeSaude)
        return dados




def cadastrar_paciente():
    try:
        with open('dados_pacientes.json') as pacientes:
                    antigos_pacientes = json.load(pacientes)
        with open('dados_pacientes.json', mode='w') as dados_pacientes:
                    antigos_pacientes.append(coletar_informacoes())
                    novos_pacientes = json.dumps(antigos_pacientes)
                    dados_pacientes.write(novos_pacientes)
    except:
        with open('dados_pacientes.json', mode='w') as dados_pacientes:
                    novos_pacientes = [coletar_informacoes()]
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
        print("\n1 - Cadastrar novo paciente\n"
              "2 - Listar pacientes\n"
              "3 - Sair\n")
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