import pacientes as pt
import medicos as md
import consultas as ct
import administracao as adm

" Author: Ian Sandes "


def menu_principal():
    print("\n")
    print(20 * "-=")
    print("       SISTEMA DE CLÍNICA MÉDICA")
    print(20 * "-=")

    print("--------------------\n"
          "1 - Pacientes\n"
          "2 - Médicos\n"
          "3 - Consultas\n"
          "4 - Administrativo\n"
          "--------------------")

    while True:
        atendimento = int(input("Escolha o tipo de atendimento a ser usado: "))
        if atendimento == 1:
            pt.menu_pacientes()
        elif atendimento == 2:
            md.menu_medicos()
        elif atendimento == 3:
            ct.menu_consultas()
        elif atendimento == 4:
            adm.menu_administracao()
        else:
            print("Opção inválida!\n")


menu_principal()
