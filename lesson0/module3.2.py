def send_email(message, recipient, *, sender="university.help@gmail.com"):
    def is_valid_mail(email):
        return "@" in email and (email.endswith(".com") or email.endswith(".ru") or email.endswith(".net"))
    if not is_valid_mail(sender) or not is_valid_mail(recipient):
        print(f"Невозможно отправить с адреса {sender} на адрес {recipient}")
    elif sender == recipient:
        print(f"Нельзя отправить письмо самому себе!")
    elif sender == "university.help@gmail.com":
        print(f"Письмо успешно отправлено с адреса {sender} на адрес {recipient}.")
    else:
        print(f"НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса {sender} на адрес {recipient}.")


send_email('Это сообщение для проверки связи', 'vasyok1337@gmail.com')
send_email('Вы видите это сообщение как лучший студент курса!', 'urban.info@gmail.ru',
           sender='urban.info@gmail.com')
send_email('Пожалуйста, исправьте задание', 'urban.student@mail.ru',
           sender='urban.teacher@mail.uk')
send_email('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru',
           sender='urban.teacher@mail.ru')
