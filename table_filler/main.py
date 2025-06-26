from functions import *
from datetime import datetime

check_if_table_exists(basic_table_filling)

action = int(input('\n\nСhoose an action:\n\n1 - Edit the duty table.\n2 - Save the changes.\n3 - Clear the table.\n4 - Exit the program.\n\n'))

while action != 4:

    check_if_table_empty(basic_table_filling)

    if action == 1:
        
        attendants = get_attendants_list()
        
        days = input('\nDays of duty (write in a line, with a space)\n').strip().split()
        attendant = input("\nAttendant's data\n").strip()
        reserve_attendant = input("\nReserve attendant's data\n").strip()

        for day in days:

            if len(day) == 1:
                day = f'0{day}{datetime.now().strftime(".%m.%Y")}'
            elif len(day) == 2:
                day = f'{day}{datetime.now().strftime(".%m.%Y")}'

            socket = attendants[day]
            
            if list(socket.keys())[0] == 'undefined':
                socket.pop('undefined')

            if attendant != '-' and reserve_attendant == '-':
                
                if socket.get('reserve_attendant'):
                    socket['attendant'] = attendant
                    del socket['reserve_attendant']

                elif not socket.get('reserve_attendant'):
                    socket['attendant'] = attendant

            elif attendant == '-' and reserve_attendant != '-':
                socket['attendant'] = '-'
                socket['reserve_attendant'] = reserve_attendant
            
            elif attendant != '-' and reserve_attendant != '-':
                socket['attendant'] = attendant
                socket['reserve_attendant'] = reserve_attendant
            
        
    elif action == 2:
        save_changes(attendants)
        print('\nData saved.')
        
    elif action == 3:
        clear_table(basic_table_filling)
        attendants = get_attendants_list()

    action = int(input('\n\nСhoose an action:\n\n1 - Edit the duty table.\n2 - Save the changes.\n3 - Clear the table.\n4 - Exit the program.\n\n'))