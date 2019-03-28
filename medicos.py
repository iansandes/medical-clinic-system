import json


def cadastro():
        dados = {}
        dados['name'] = input('Nome: ')
        dados['email'] = input('Email:')
        dados['phone'] = input('Telefone: ')
        dados['crm'] = input('CRM: ')
        dados['rg'] = input('RG: ')
        dados['cpf'] = input('CPF: ')
        dados['specialization'] = input('Especialização: ')
        dados['number'] = input('Endereço: ')
        dados['address'] = input('Número: ')
        dados['hood'] = input('Bairro: ')
        dados['city'] = input('Cidade: ')
        dados['state'] = input('UF: ')
        dados['plan'] = input('Plano de saúde: ')
        return dados


def listar_medicos():
    with open('dados_medicos.json',) as dados_medicos:
        lista_medicos = json.load(dados_medicos)
        print('Médicos     Especialização\n')
        for medico in lista_medicos:
            print(medico['name'] + ' ' + medico['specialization'] )
    print('-'*20)


def remover_medico():


def menu():
    while True:
        print('''1 - Cadastrar novo médico
2 - Listar médicos
3 - Remover médicos
4 - Sair
        ''')
        opcao = int(input('Selecione uma opção: '))
        if opcao == 1:
            try:
                with open('dados_medicos.json') as medicos:
                    antigos_medicos = json.load(medicos)
                with open('dados_medicos.json', mode='w') as dados_medicos:
                    antigos_medicos.append(cadastro())
                    novos_medicos = json.dumps(antigos_medicos)
                    dados_medicos.write(novos_medicos)
            except:
                with open('dados_medicos.json', mode='w') as dados_medicos:
                    novos_medicos = []
                    novos_medicos.append(cadastro())
                    medicos = json.dumps(novos_medicos)
                    dados_medicos.write(medicos)

        elif opcao == 2:
            listar_medicos()
        elif opcao == 3:
            remover_medico()
        elif opcao == 4:
            break
        else:
            print("Opção inválida!")