def create_phone_number(text):
    return '({}{}{}) {}{}{}-{}{}{}{}'.format(*text)

print(create_phone_number('8003332222'))
