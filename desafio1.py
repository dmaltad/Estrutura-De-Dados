from curses.ascii import isdigit
import os

menu = """
Menu:
1 - Registrar entrada de veículo
2 - Registrar saída de veículo
3 - Listar veículos estacionados
0 - Sair
"""

lista_placas = []

lista_horarios = []

if __name__ == '__main__':
    while True:
        os.system('clear')
        print(menu)
        try:
            opcao = int(input('Escolha uma opção: '))
            if opcao not in (1,2,3,0):
                raise ValueError()
        except ValueError:
            os.system('clear')
            print('Opção inserida inválida!')
            input('\nDigite ENTER para prosseguir: ')
            continue
        match opcao:
            case 1:
                os.system('clear')
                print('REGISTRO DE ENTRADA')
                placa = input('Digite a placa do carro: ').upper()
                if placa in lista_placas:
                    os.system('clear')
                    print('Entrada não registrada! Placa digitada já está no sistema!')
                    input('\nDigite ENTER para prosseguir: ')
                    continue
                horario = input('Digite o horário (Ex: 00:00): ')
                os.system('clear')
                lista_placas.append(placa)
                lista_horarios.append(horario)
                print(f'Entrada registrada com sucesso!\nPlaca: {placa}\nHorário: {horario}')
                input('\nDigite ENTER para prosseguir: ')
            case 2:
                os.system('clear')
                print('REGISTRO DE SAÍDA')
                placa = input('Digite a placa do carro: ').upper()
                if placa not in lista_placas:
                    os.system('clear')
                    print('Placa informada não registrada!')
                    input('\nDigite ENTER para prosseguir: ')
                    continue
                horario_saida = input('Digite o horário (Ex: 00:00): ').split(':')
                os.system('clear')
                indice_placa = lista_placas.index(placa)
                horario_entrada = lista_horarios[indice_placa].split(':')
                horas = int(horario_saida[0]) - int(horario_entrada[0])
                estadia = 0
                valor = 0
                if horas < 0:
                    print('Horário de saída inválido! Não pode ser menor que o de entrada.')
                    input('\nDigite ENTER para prosseguir: ')
                    continue
                match horas:
                    case 0:
                        estadia = 1
                        valor = 7
                    case _:
                        estadia = horas
                        valor = horas * 7
                print(f'Estadia: {estadia}h\nValor a pagar: R$ {valor},00')
                lista_horarios.remove(lista_horarios[indice_placa])
                lista_placas.remove(placa)
                input('\nDigite ENTER para prosseguir: ')
            case 3:
                os.system('clear')
                print('LISTAGEM DE VEÍCULOS')
                for indice, placa in enumerate(lista_placas):
                    print(f'{indice+1} - Placa: {placa}')
                if not lista_placas:
                    print('Sem veículos registrados.')
                input('\nDigite ENTER para prosseguir: ')
            case 0:
                print('Finalizando o sistema...')
                break
