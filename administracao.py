import folha_pagamento as fp


def menu_administracao():
    while True:
        print("\n1 - Folha de pagamento individual\n"
              "2 - Despesas totais com pessoal\n"
              "3 - Estatísticas de consultas\n")
        opcao = int(input('Selecione uma opção: '))
        if opcao == 1:
            folha_individual()
        elif opcao == 2:
            listar_pacientes()
        elif opcao == 3:
            from menu_principal import menu_principal
            menu_principal()
        else:
            print("Opção inválida!")


def folha_individual():
    medico = fp.selecionar_medico()
    salario_bruto = int(medico['salary'])
    print("FOLHA DE PAGAMENTO\n"
          "Nome do médico: {}".format(medico["name"]))
    fp.folha(salario_bruto)
