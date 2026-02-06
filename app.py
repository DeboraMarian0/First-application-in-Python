import os  # biblioteca usada para limpar terminal
'''
Os nomes dos novos restaurantes só ficam salvos durante a execução do programa, 
depois são apagados.

foram colocados nomes dos restaurantes para iniciar para que fosse possível listar 
mais de um ao executar o programa.
'''
restaurants = [{'name': 'Italian Pizza', 'category': 'Italian', 'active': False},
               {'name': 'Ohanna', 'category': 'Japanese', 'active': True}
               ]


def app_name():
    print('''
    ▒█▀▀▀ █░█ █▀▀█ █▀▀█ █▀▀ █▀▀ █▀▀ 　 ▒█▀▀▀ █░░ █▀▀█ ▀█░█▀ █▀▀█ █▀▀█
    ▒█▀▀▀ ▄▀▄ █░░█ █▄▄▀ █▀▀ ▀▀█ ▀▀█ 　 ▒█▀▀▀ █░░ █▄▄█ ░█▄█░ █░░█ █▄▄▀
    ▒█▄▄▄ ▀░▀ █▀▀▀ ▀░▀▀ ▀▀▀ ▀▀▀ ▀▀▀ 　 ▒█░░░ ▀▀▀ ▀░░▀ ░░▀░░ ▀▀▀▀ ▀░▀▀
    \n''')


def options():
    print('1. Register restaurant')
    print('2. List restaurant')
    print('3. Change restaurant status')
    print('4. Finish\n')


def end_app():
    display_text('Finishing app\n')


def return_to_menu():
   #  retorna para o início do programa (main)
    input('\n\033[1;41mPress enter to return to the main menu\033[0m ')
    main()


def invalid_option():
    ''' Exibe mensagem de opção inválida e retorna ao menu principal 

    Outputs:
    - Retorna ao menu principal
    '''
    print('\n\033[0;31mInvalid option! \033[0m\n')
    return_to_menu()


def display_text(text):
    # limpa terminal - 'cls' para Windows -  'clear' para mac
    os.system('cls')
    line = '*' * len(text)
    print(f'\033[0;33m{line}\033[0m')
    print(f'\033[0;42m{text}\033[0m')
    print(f'\033[0;33m{line}\033[0m')
    print()


def new_restaurant():
    '''
    Cadastra novos restaurantes.

    inputs:
    -Nome do restaurante
    -categoria do restaurante

    output:
    Envia ao usuário um feedback informando que foi cadastrado
    '''
    display_text('Registration of new restaurants: ')
    restaurant_name = input('Enter the restaurant name: ')
    category = input('Enter the restaurant category: ')

    restaurant_data = {'name': restaurant_name,
                       'category': category, 'active': False}

    restaurants.append(restaurant_data)

    print(
        f'\nThe restaurant "\033[1;35m{restaurant_name}\033[0m" was \033[2;32msuccessfully registered!\033[0m')

    return_to_menu()


def list_restaurant():
    display_text('Listed restaurants: ')

    print(f'{'Restaurant name'.ljust(22)} | {'Category'.ljust(20)} | Status')
    for restaurant in restaurants:
        name_restaurant = restaurant['name']
        category_restaurant = restaurant['category']
        restaurant_situation = 'Active' if restaurant['active'] else 'disabled'
        print(
            f'- {name_restaurant.ljust(20)} | {category_restaurant.ljust(20)} | {restaurant_situation}')

    return_to_menu()


def change_restaurant_activity():
    display_text("Changing the restaurant's status: ")
    restaurant_name = input(
        'Enter the name of the restaurant whose status you want to change: ')
    restaurant_found = False

    for restaurant in restaurants:
        if restaurant_name == restaurant['name']:
            restaurant_found = True
            # o not altera a atividade, se foi salva como false fica true e vice-versa
            restaurant['active'] = not restaurant['active']
            message = f'\nThe restaurant \033[1;35m{restaurant_name}\033[0m was successfully \033[2;32mactivated!\033[0m' if restaurant[
                'active'] else f'\nThe restaurant \033[1;35m{restaurant_name}\033[0m was successfully shut down!'

            print(message)
    if not restaurant_found:  # ou if restaurant_found == False, ou seja, o valor é falso
        print('The restaurant could not be found!')

    return_to_menu()


def choice():
    try:
        option_chosen = int(input('Choose an option: '))
        print(f'You chose the option {option_chosen}')

        match option_chosen:
            case 1:
                new_restaurant()
            case 2:
                list_restaurant()
            case 3:
                change_restaurant_activity()
            case 4:
                end_app()
            case _:
                invalid_option()
    except ValueError:
        invalid_option()


def main():
    os.system('cls')
    app_name()
    options()
    choice()


if __name__ == '__main__':
    main()
