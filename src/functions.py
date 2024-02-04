from datetime import datetime
import json
import re


def load_operation(our_file):
    """Функция, которая получает данные из json файла"""
    with open(our_file, "r", encoding='utf-8-sig') as file:
        operations = json.load(file)
    return operations


def get_executed_operations(operations):
    """Функция, которая выбирает только выполненные переводы"""
    new_dict = []
    for i in operations:
        if i.get('state') == "EXECUTED":
            new_dict.append(i)
    return new_dict


def sorted_operation(new_dict):
    """Функция, которые выбирает последние пять переводов"""
    sorted_operations = sorted(new_dict, key=lambda x: x['date'], reverse=True)
    five_dict = sorted_operations[:5]
    return five_dict


def changed_date(five_operation):
    """Функция, которая меняет формат записи даты"""
    for i in five_operation:
        date_str = i['date']
        date_format = "%Y-%m-%dT%H:%M:%S.%f"
        date_obj = datetime.strptime(date_str, date_format)
        new_date_format = "%d.%m.%Y"
        new_date_str = date_obj.strftime(new_date_format)
        i['date'] = new_date_str
    return five_operation


def operations_with_stars(ch_five_operations):
    """Функция, которая заменяет нужные цифры на звездочки"""
    for i in ch_five_operations:
        if i.get('from') is not None:
            if i['description'] == "Перевод организации":
                result = re.sub(r'(\d{4})(\d{2})(\d{2})(\d{4})', r'\1 \2** **** ', i['from'])
                i['from'] = result
            else:
                result = re.sub(r'(\d{16})', r'**', i['from'])
                i['from'] = result
        if "Счет" in i['to']:
            result = re.sub(r'(\d{16})', r'**', i['to'])
            i['to'] = result
        else:
            result = re.sub(r'(\d{4})(\d{2})(\d{2})(\d{4})', r'\1 \2** **** ', i['to'])
            i['to'] = result
    return ch_five_operations
