
class Name:
    def __init__(self, name):
        self.name = name
        self.last_name = None

    def get_name(self):
        return self.name

    def get_last_name(self):
        last_name = input('Last name: ')
        self.last_name = last_name

person = Name('Jamshid')
person.get_name()
person.get_last_name()
