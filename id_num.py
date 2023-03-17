import core

class NumIdentification(core.Identification):
    def validate(self) -> bool:
        password = input("What is the password? ")
        if password == "1234":
            return True
        return False