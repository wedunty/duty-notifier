from datetime import datetime, timedelta

def get_current_week_dates():
    today = datetime.now()
    start_of_week = today - timedelta(days=today.weekday())
    week_dates = [(start_of_week + timedelta(days=i)).strftime("%d.%m.%Y") for i in range(7)]
    return week_dates

def get_attendants_list(label):
    attendants = {}
    with open(f"files/tables/{label}_table.txt", "r", encoding="utf-8") as file:
        attendants_table = list(map(lambda x: x.replace("\n", "").split(), file.readlines()))

    for *info, date, state in attendants_table:
        if state == "д":
            attendants[date] = {"attendant": " ".join(info)}
        elif state == "р":
            attendants[date].update({"reserve_attendant": " ".join(info)})

    return attendants

def get_week_attendants_list(week_dates, attendants):
    week_attendants = ""
    for date in week_dates:
        if date in attendants.keys():
            if attendants[date].values() == 2:
                week_attendants += f"<u><b>{date}</b></u>: <b>дежурный</b> - {attendants[date]["attendant"]} с <b>18:00</b> до <b>{(datetime.strptime(date, "%d.%m.%Y").date() + timedelta(days=1)).strftime("%d.%m.%Y")} 9:00</b>, <b>резервный дежурный</b> - {attendants[date]["reserve_attendant"]}\n\n"
            else:
                week_attendants += f"<u><b>{date}</b></u>: <b>дежурный</b> - {attendants[date]["attendant"]} с <b>18:00</b> до <b>{(datetime.strptime(date, "%d.%m.%Y").date() + timedelta(days=1)).strftime("%d.%m.%Y")} 9:00</b>\n\n"
        else:
            break
    return week_attendants

def get_current_attendant(attendants):
    date = datetime.today().strftime("%d.%m.%Y")
    if attendants[date].values() == 2:
        current_attendant = f"<u><b>{date}</b></u>: <b>дежурный</b> - {attendants[date]["attendant"]} с <b>18:00</b> до <b>{(datetime.strptime(date, "%d.%m.%Y").date() + timedelta(days=1)).strftime("%d.%m.%Y")} 9:00</b>, <b>резервный дежурный</b> - {attendants[date]["reserve_attendant"]}\n\n"
    else:
        current_attendant = f"<u><b>{date}</b></u>: <b>дежурный</b> - {attendants[date]["attendant"]} с <b>18:00</b> до <b>{(datetime.strptime(date, "%d.%m.%Y").date() + timedelta(days=1)).strftime("%d.%m.%Y")} 9:00</b>\n\n"
    return current_attendant
<<<<<<< HEAD

def get_key(dict, value):
    return list(dict.keys())[list(dict.values()).index(value)]


=======

>>>>>>> ccaedf7c771c997a5c166bafbbd3e98eef5861ec