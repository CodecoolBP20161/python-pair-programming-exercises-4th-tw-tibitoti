class Person():
    _name = None
    _phone_number = None

    def __init__(self, name, phone_number):
        self.name = name
        self.phone_number = phone_number

    def is_phone_number_matching(self, input_phone_number):
        self.input_phone_number = input("Please give me a phone number: ")

    def get_name(self):
        pass

    @staticmethod
    def normalize_phone_number(phone_number):
        # implent this method
        pass  # delete this
