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
    from pacientes import *
    menu()
if atendimento == 2:
    from medicos import *
    menu()
