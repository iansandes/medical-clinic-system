import json


def coletar_informacoes():
    nome = input('Nome: ')
    email = input('Email:')
    telefone = input('Telefone: ')
    crm = input('CRM: ')
    rg = input('RG: ')
    cpf = int(input('CPF: '))
    endereco = input('Endereço: ')
    especializacao = input('Especialização: ')
    numero = input('Número: ')
    bairro = input('Bairro: ')
    cidade = input('Cidade: ')
    uf = input('UF: ')
    planoDeSaude = input('Plano de saúde: ')
    salario = input('Salario Bruto: ')

    dados = dict(name=nome, email=email, phone=telefone, crm=crm,
                 rg=rg, cpf=cpf, specialization=especializacao,
                 address=endereco, number=numero, hood=bairro,
                 city=cidade, state=uf, plan=planoDeSaude, salary=salario)
    return dados


def cadastrar_medico():
    try:
        with open('dados_medicos.json') as medicos:
            antigos_medicos = json.load(medicos)
        with open('dados_medicos.json', mode='w') as dados_medicos:
            antigos_medicos.append(coletar_informacoes())
            novos_medicos = json.dumps(antigos_medicos)
            dados_medicos.write(novos_medicos)
    except:
        with open('dados_medicos.json', mode='w') as dados_medicos:
            novos_medicos = [coletar_informacoes()]
            medicos = json.dumps(novos_medicos)
            dados_medicos.write(medicos)


def listar_medicos():
    try:
        with open('dados_medicos.json', ) as dados_medicos:
            lista_medicos = json.load(dados_medicos)
            print('Médicos     Especialização\n')
            for medico in lista_medicos:
                print('{}       {}'.format(medico['name'], medico['specialization']))
        print('-' * 20)
    except:
        print("Nenhum médico cadastrado!")
        menu_medicos()


def remover_medico():
    try:
        with open('dados_medicos.json') as dados_medicos:
            lista_medicos = json.load(dados_medicos)
            cpf = int(input('Qual o CPF do médico que você deseja remover?'))
            for medico in lista_medicos:
                if medico['cpf'] == cpf:
                    lista_medicos.remove(medico)
                    with open('dados_medicos.json', mode='w') as dados_medicos:
                        medicos = json.dumps(lista_medicos)
                        dados_medicos.write(medicos)
                    print('Médico removido com sucesso!\n')
                else:
                    print('Médico não encontrado!\n')
                    menu_medicos()
    except:
        print('Nenhum CPF informado')
        menu_medicos()


def menu_medicos():
    while True:
        print('''1 - Cadastrar novo médico
2 - Listar médicos
3 - Remover médicos
4 - Sair
        ''')
        opcao = int(input('Selecione uma opção: '))
        if opcao == 1:
            cadastrar_medico()
        elif opcao == 2:
            listar_medicos()
        elif opcao == 3:
            remover_medico()
        elif opcao == 4:
            from menu_principal import menu_principal
            menu_principal()
        else:
            print("Opção inválida!")
