import random
import string


def password_validation(self, p1, p2):
    password1 = p1
    password2 = p2

    min = 6
    lowerc = False
    upperc = False
    num = False
    special = False
    special_characters = "\\\"!@#$%^&*()-+?_=,<>/\{\}\[\]|:;'.~´¡%^1234567890"

    if any(c in special_characters for c in password1):
        special = True

    for c in password1:
        if c.islower():
            lowerc = True

        if c.isupper():
            upperc = True

        if c.isdigit():
            num = True

    if len(password1) < min:
        self.add_error(
            'repeat_password',
            'La contraseña debe tener al menos 6 caracteres'
        )

    if password1 != password2:
        self.add_error(
            'repeat_password',
            'Las contraseñas no coinciden'
        )

    if lowerc == False and upperc == False:
        self.add_error(
            'repeat_password',
            'La contraseña debe contener al menos una letra'
        )

    if special == False and num == False:
        self.add_error(
            'repeat_password',
            'La contraseña debe contener al menos un caracter especial o un número'
        )


def generate_random_code(size=4, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))
