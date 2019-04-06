import json
import administracao as adm

def selecionar_medico():
    """

    Carrega a lista de médicos e pede o CPF do médico que o usuário
    deseja ver a folha de pagamento. Se o médico for encontrado, serão retor-
    nados os dados dele. Caso não seja, será informado a tela.
    """
    try:
        with open('dados_medicos.json', ) as dados_medicos:
            lista_medicos = json.load(dados_medicos)
            cpf = int(input('Qual o CPF do médico que você deseja ver a folha?'))
            for medico in lista_medicos:
                if medico['cpf'] == cpf:
                    medico_selec = medico
                    return medico_selec

    except:
        print('Médico não encontrado!')
        adm.menu_administracao()


def calculo_inss(salario_bruto):
    """ Faz o cálculo do INSS a partir do salário bruto."""
    if salario_bruto < 1693.73:
        inss = salario_bruto * 8 / 100
    elif salario_bruto >= 1693.73 and salario_bruto < 2822.91:
        inss = salario_bruto * 9 / 100
    elif salario_bruto > 2822.90 and salario_bruto < 5645.80:
        inss = salario_bruto * 11 / 100
    else:
        inss = 621.03
    return inss


def calculo_irrf(salario_bruto):
    """ Faz o cálculo do IRRF a partir do salário bruto."""
    salario = salario_bruto - calculo_inss(salario_bruto)
    if salario >= 1903.99 and salario < 2826.66:
        irrf = (salario - 142.82) * 7.5 / 100
    elif salario >= 2826.66 and salario < 3751.06:
        irrf = (salario - 354.80) * 15 / 100
    elif salario >= 3751.05 and salario < 4664.69:
        irrf = (salario - 636.13) * 22.5 / 100
    elif salario >= 4664.69:
        irrf = (salario - 869.36) * 27.5 / 100
    else:
        irrf = 0
    return irrf


def folha(salario_bruto):
    """ Imprime a folha. """
    print("Salario Bruto")
    print(salario_bruto)
    print("Descontos")
    print("_______________________")
    print("INSS")
    print("{:.2f}".format(calculo_inss(salario_bruto)))
    print("IRRF")
    print("{:.2f}".format(calculo_irrf(salario_bruto)))
    print("Total de descontos")
    total = calculo_irrf(salario_bruto) + calculo_inss(salario_bruto)
    print("{:.2f}".format(total))
    salario_liquido = salario_bruto - total
    print("_______________________")
    print("Salario líquido")
    print("{:.2f}".format(salario_liquido))
    print("_______________________")
