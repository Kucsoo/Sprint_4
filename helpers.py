import random as r

def random_name():
    names =['Анна', 'Виктор', 'Кристофер', 'Екатерина', 'София']
    r_name = r.choice(names)
    return r_name


def random_surname():
    surnames = ['Акопян', 'Гайдар', 'Смит', 'Валентайн', 'Абрау']
    r_surname = r.choice(surnames)
    return r_surname

def random_address():
    addresses = ['Ленина пр. 154', 'ул. Комсомольская 32', 'Кутузовский пр. 48', 'ул. Мира 9', 'Земляной Вал 48']
    r_address = r.choice(addresses)
    return r_address

def random_telephone():
    region_id = '+7'
    operator_id = r.randint(900, 999)
    number = r.randint(100000, 999999)
    r_telephone = region_id + str(operator_id) + str(number)
    return r_telephone

def random_comment():
    comments = ['Не звоните после 20.00!', 'не звоните спит ребенок',
                'в доме шлагбаумб звоните', 'можно два самоката?', 'пишите в мессендер']
    r_comment = r.choice(comments)
    return r_comment