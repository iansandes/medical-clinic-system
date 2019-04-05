import json


def marcar_consulta():
    dados = {}
    nome_paciente = input('Informe seu nome: ')
    with open('dados_pacientes.json') as dados_pacientes:
        lista_pacientes = json.load(dados_pacientes)
        for paciente in lista_pacientes:
            if nome_paciente == paciente['name']:
                print('Vefificado com sucesso! ')
                print('-' * 20 + '\n')
                dados['name'] = nome_paciente
            else:
                print('Não encontrado!')
                return marcar_consulta()

    with open('dados_medicos.json') as dados_medicos:
        lista_medicos = json.load(dados_medicos)
        print('Lista de médicos: \n')
        print('Médicos     Especialização\n')
        for medico in lista_medicos:
            print(medico['name'] + '     ' + medico['specialization'])
            print('-' * 20 + '\n')
    nome_medico = input('Escolha seu medico: ')
    dados['medico'] = nome_medico

    dados['dia'] = input('Informe o dia [dd]:  ')
    dados['mes'] = input('Informe o mês [mm]: ')
    dados['ano'] = input('Informe o ano [aaaa]: ')
    dados['hora'] = input('Qual hora? ')

    return dados


def listar_consultas():
    try:
        with open('dados_consultas.json') as listas_consultas:
            lista_consultas = json.load(listas_consultas)
            print('Consultas: \n')
            for consulta in lista_consultas:
                print('Paciente: {} | Médico: {} | Data: {}/{}/{} | Hora: {}'.format(consulta['name'],
                                                                                     consulta['medico'],
                                                                                     consulta['dia'], consulta['mes'],
                                                                                     consulta['ano'],
                                                                                     consulta['hora']))
            print('-' * 20)
        menu_consultas()
    except:
        print("Nenhum dado de consulta foi encontrado!")
        menu_consultas()


def remover_consulta():
    nome_paciente = input('Informe o nome do paciente: ')
    dia_consulta = input('Informe o dia da consulta [dd]: ')
    mes_consulta = input('Informe o mês da consulta [mm]: ')
    try:
        with open('dados_consultas.json') as dados_consultas:
            lista_consultas = json.load(dados_consultas)
            for paciente in lista_consultas:
                if paciente['name'] == nome_paciente and paciente['dia'] == dia_consulta and paciente['mes'] == mes_consulta:
                        lista_consultas.remove(paciente)
                        with open('dados_consultas.json', mode='w') as dados_consultas:
                            consultas = json.dumps(lista_consultas)
                            dados_consultas.write(consultas)
                            print('Consulta removida com sucesso!\n')
                else:
                    print('Consulta não encontrada!\n')
                    menu_consultas()
    except:
        print('Nenhum paciente informado!\n')
        menu_consultas()


def menu_consultas():
    while True:
        print('  1 - Marcar nova consulta \n  2 - Listar consultas \n  3 - Remover Consulta \n  4 - Sair ')
        opcao = int(input('Selecione uma opção: '))
        if opcao == 1:
            try:
                with open('dados_consultas.json') as consultas:
                    antigos_consultas = json.load(consultas)
                with open('dados_consultas.json', mode='w') as dados_consultas:
                    antigos_consultas.append(marcar_consulta())
                    novos_consultas = json.dumps(antigos_consultas)
                    dados_consultas.write(novos_consultas)
                    print('Consulta marcada com sucesso!')

            except:
                with open('dados_consultas.json', mode='w') as dados_consultas:
                    novas_consultas = [marcar_consulta()]
                    consultas = json.dumps(novas_consultas)
                    dados_consultas.write(consultas)
                    print('Consulta marcada com sucesso!')

        elif opcao == 2:
            listar_consultas()
        elif opcao == 3:
            remover_consulta()
        elif opcao == 4:
            from menu_principal import menu_principal
            menu_principal()
        else:
            print('Opção inválida!\n')
            menu_consultas()
