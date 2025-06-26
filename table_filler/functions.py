import calendar
import os
from datetime import timedelta, datetime, date

def basic_table_filling():
    month = datetime.now().month
    year = datetime.now().year
    days = calendar.monthrange(year, month)[1]
    first_date = date(year, month, 1)
    dates = {(first_date + timedelta(days=i)).strftime('%d.%m.%Y'): {} for i in range(days)}
    
    with open('./table_filler/next_month.txt', 'a', encoding='utf-8') as file:
        for day in dates:
            file.write(f"{day} - -\n")

def check_if_table_exists(basic_table_filling):
    
    if not os.path.exists('./table_filler/next_month.txt'):
        basic_table_filling()
        
def check_if_table_empty(basic_table_filling):
    
    if open('./table_filler/next_month.txt', 'r', encoding='utf-8').read() == '':
        basic_table_filling()

def get_attendants_list():
    
    with open('./table_filler/next_month.txt', 'r', encoding='utf-8') as file:
        attendants = {}
        attendants_table = list(map(lambda x: x.replace('\n', '').split(), file.readlines()))
        
    for day, *info, state in attendants_table:
        if state == 'д':
            attendants[day] = {'attendant': f'{' '.join(info)} д'}
        elif state == 'р':
            try:
                if attendants[day].get('undefined'):
                    attendants[day].update({'attendant': '- д', 'reserve_attendant': f'{' '.join(info)} р'})
                    attendants[day].pop('undefined')
                else:
                    attendants[day].update({'reserve_attendant': f'{' '.join(info)} р'})
            except:
                attendants[day] = {'attendant': '- д', 'reserve_attendant': f'{' '.join(info)} р'}
        elif state == '-': 
            attendants[day] = {'undefined': '- -'}
    return attendants

def save_changes(attendants):
    
    with open('./table_filler/next_month.txt', 'w', encoding='utf-8') as file:        
        for date in attendants:            
            if len(attendants[date]) == 2:
                if attendants[date]['attendant'].split()[-1] == 'д':
                    file.write(f'{date} {attendants[date]['attendant']}\n')                   
                else:
                    file.write(f'{date} {attendants[date]['attendant']} д\n')                   
                if attendants[date]['reserve_attendant'].split()[-1] == 'р':
                    file.write(f'{date} {attendants[date]['reserve_attendant']}\n')                    
                else:
                    file.write(f'{date} {attendants[date]['reserve_attendant']} р\n')
            elif len(attendants[date]) == 1:                
                if list(attendants[date].keys())[0] == 'attendant':                    
                    if attendants[date]['attendant'].split()[-1] == 'д':
                        file.write(f'{date} {attendants[date]['attendant']}\n')                        
                    else:
                        file.write(f'{date} {attendants[date]['attendant']} д\n')                        
                elif list(attendants[date].keys())[0] == 'undefined':
                    file.write(f'{date} {attendants[date]['undefined']}\n')
                    
def clear_table(basic_table_filling):
    
    open('./table_filler/next_month.txt', 'w').close()
    
    basic_table_filling()
            