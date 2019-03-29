from medicos import *
from pacientes import *


# Marcar consulta(medico, paciente, data, hora)
def marcar_consulta():
    dados = {}
    nome_paciente = input('Informe seu nome: ')
    with open('dados_pacientes.json',) as dados_pacientes:
        lista_pacientes = json.load(dados_pacientes)
        for paciente in lista_pacientes:
            if nome_paciente == paciente['name']:
                print('Vefificado com sucesso ')
                dados['name'] = nome_paciente
            else:
                print('Não encontrado!')
                return marcar_consulta()

    
    with open('dados_medicos.json',) as dados_medicos:
        lista_medicos = json.load(dados_medicos)
        print('Lista de médicos: \n')
        for medico in lista_medicos:
            print(medico['name'])
    nome_medico = input('Escolha seu medico:')
    dados['médico'] = nome_medico

    dados['data'] = input('Qual data [dia/mês/ano] ?') # Aqui não importar a data ou hora nesse sistema
    dados['hora'] = input('Qual hora [hh:mm] ?')

    print('Consulta marcada com sucesso!')
    return dados

def listar_consultas():
    with open('dados_consultas.json',) as dados_consultas:
        lista_consultas = json.load(dados_consultas)
        print('Consultas: \n')
        for consulta in lista_consultas:
            print(consulta)
    print('-'*20)



def menu_consultas():
    while True:
        print('''1 - Marcar nova consulta
2 - Listar consultas
3 - Sair
        ''')
        opcao = int(input('Selecione uma opção: \n'))
        if opcao == 1:
            try:
                with open('dados_consultas.json') as consultas:
                    antigos_consultas = json.load(consultas)
                with open('dados_consultas.json', mode='w') as dados_consultas:
                    antigos_consultas.append(marcar_consulta())
                    novos_consultas = json.dumps(antigos_consultas)
                    dados_consultas.write(novos_consultas)
            except:
                with open('dados_consultas.json', mode='w') as dados_consultas:
                    novos_consultas = []
                    novos_consultas.append(marcar_consulta())
                    consultas = json.dumps(novos_consultas)
                    dados_consultas.write(consultas)

        elif opcao == 2:
            listar_consultas()
        elif opcao == 3:
            from menu_principal import menu_principal
            menu_principal.menu_principal()
        else:
            print("Opção inválida!")