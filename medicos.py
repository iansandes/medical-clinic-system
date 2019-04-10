import json


def coletar_informacoes():
    """

    Recebe as informações do médico que são informadas pelo
    usuário do sistema.
    """
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
    salario = float(input('Salario Bruto: '))

    dados = dict(name=nome, email=email.lower(), phone=telefone, crm=crm,
                 rg=rg, cpf=cpf, specialization=especializacao,
                 address=endereco, number=numero, hood=bairro,
                 city=cidade, state=uf, plan=planoDeSaude, salary=salario)
    return dados


def cadastrar_medico():
    """

    Carrega o arquivo de médicos, caso ele exista, e adiciona as informações
    coletadas pela função coletar_informacoes(). Caso não exista o arquivo de
    médicos, um novo arquivo é aberto pra ser feito o cadastro dos médicos.
    """
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
    finally:
        print('\nMédico cadastrado com sucesso!')


def listar_medicos():
    """

    Carrega o arquivo de médicos e imprime o nome de cada médico cadas-
    trado. Caso não exista o arquivo, é informado que nenhum médico está cadastrado.
    Se o arquivo existir e estiver vazio, irá impimir a lista de médicos vazia.
    """
    try:
        with open('dados_medicos.json', ) as dados_medicos:
            lista_medicos = json.load(dados_medicos)

            for medico in lista_medicos:
                print("Médico: {} | Especialização: {}".format(medico['name'], medico['specialization']))
        print('-' * 20)
    except:
        print("\nNenhum médico cadastrado!")
        menu_medicos()


def remover_medico():
    """

    Carrega o arquivo de médicos e pede para o usuário informar o número do
    CPF do médico que deseja remover. Caso o número do CPF informado esteja cadastrado
    no arquivo de médicos, esse médico será removido, e uma nova lista de médicos atualiza-
    da irá sobrescrever a lista desatualizada. Caso o médico não seja encontrado ou nenhum CPF
    seja informado, será exibido na tela.
    """
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
        print('\nNenhum CPF encontrado')
        menu_medicos()


def menu_medicos():
    while True:
        print("\n1 - Cadastrar novo médico\n"
              "2 - Listar médicos\n"
              "3 - Remover médico\n"
              "4 - Sair")
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
            print("\nOpção inválida!")
