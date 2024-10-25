# Домашнее задание по теме "Try и Except"

def add_everything_up(a,b):
    try:
        res = round(a + b,3)
        return (res)
    except TypeError:
        if isinstance(a, str) or isinstance(b, str):
            return f'{a}{b}'


print(add_everything_up(123.456, 'строка'))
print(add_everything_up('яблоко', 4215))
print(add_everything_up(123.456, 7))