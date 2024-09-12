 # Модуль 3.2 Рассылка писем

def send_email (message, recipiant, *, sender = "university.help@gmail.com"):

    proverka_= "@" in sender and "@" in recipiant # проверка на @
    proverka_sender = ".com" in sender or '.ru' in sender or '.net' in sender # проверка sender на окончания
    proverka_recipiant = ".com"  in recipiant or '.ru'  in recipiant or '.net'  in recipiant  # проверка recipiant на окончания
    proverka = proverka_ and proverka_sender and proverka_recipiant # итоговая проверка

    if proverka == False:
        print (f"Невозможно отправить письмо с адреса: {sender} на адрес: {recipiant}")

    elif sender == recipiant :
        print (f"Невозможно отправить самому себе")

    elif sender=='university.help@gmail.com':
        print(f"Письмо успешно отправлено с адреса: {sender} на адрес: {recipiant}")

    else:
        print (f"Нестандартный отправитель! Письмо успешно отправлено с адреса: {sender} на адрес: {recipiant}")


send_email('Это сообщение для проверки связи', 'vasyok1337@gmail.com')
send_email('Вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.ru', sender='urban.info@gmail.com')
send_email('Пожалуйста, исправьте задание', 'urban.student@mail.ru', sender='urban.teacher@mail.uk')
send_email('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru', sender='urban.teacher@mail.ru')
