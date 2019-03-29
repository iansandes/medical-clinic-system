def menu_principal():
    print(20 * "-=")
    print("       SISTEMA DE CLÍNICA MÉDICA")
    print(20 * "-=")

    print('''--------------------
    1 - Pacientes
    2 - Médicos
    3 - Consultas
    4 - Administrativo
    --------------------''')

    atendimento = int(input("Escolha o tipo de atendimento a ser usado: "))

    if atendimento == 1:
        import pacientes as pt
        pt.menu_pacientes()
    if atendimento == 2:
        import medicos as md
        md.menu_medicos()
    if atendimento == 3:
        import consultas as ct
        ct.menu_consultas()


menu_principal()
