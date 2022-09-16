# Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя: имя, фамилия,
# год рождения, город проживания, email, телефон. Функция должна принимать параметры как именованные аргументы.
# Реализовать вывод данных о пользователе одной строкой.
def personal_data(name='unknown', surname='unknown', birthday='unknown', residence='unknown', email='unknown',
                  phone='unknown'):
    return f'ФИ: {surname} {name} день рождение: {birthday} город проживания: {residence} mail: {email} тел: {phone} '
