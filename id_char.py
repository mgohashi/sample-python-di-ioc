import core

class CharIdentification(core.Identification):
    def validate(self) -> bool:
        password = input("What is the password? ")
        if password == "abcd":
            return True
        return False
