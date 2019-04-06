import folha_pagamento as fp
import estatisticas as es

def menu_administracao():
    while True:
        print("\n1 - Folha de pagamento individual\n"
              "2 - Estatísticas de consultas\n"
              "3 - Sair\n")
        opcao = int(input('Selecione uma opção: '))
        if opcao == 1:
            folha_individual()
        elif opcao == 2:
            try:
                es.grafico()
            except:
                print('Não existem dados de consulta!')
                menu_administracao()
        elif opcao == 3:
            from menu_principal import menu_principal
            menu_principal()
        else:
            print("Opção inválida!")


def folha_individual():
    """ Imprime a folha de pagamento do médico selecionado. """
    medico = fp.selecionar_medico()
    salario_bruto = int(medico['salary'])
    print("FOLHA DE PAGAMENTO\n"
          "Nome do médico: {}".format(medico["name"]))
    fp.folha(salario_bruto)
