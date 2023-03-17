from abc import ABC, abstractmethod
from enum import Enum

class Identification(ABC):
    @abstractmethod
    def validate(self) -> bool:
        pass

class LockerState(Enum):
    CLOSED=0
    OPENED=1

class Locker(ABC):
    def __init__(self) -> None:
        self.state = LockerState.OPENED

    def open(self, ident: Identification) -> bool:
        print('Opening the locker...')
        if ident.validate():
            self.state = LockerState.OPENED
            return True
        return False
        
    def close(self) -> None:
        self.state = LockerState.CLOSED

class Door(ABC):
    def __init__(self, locker: Locker) -> None:
        self.locker = locker
        
    def open(self, ident: Identification) -> bool:
        print('Opening the door...')
        if (self.locker.state != LockerState.CLOSED):
            return self.locker.open(ident)
        return False

def run(door: Door, ident: Identification):
    result = door.open(ident)
    print(f'Has the door opened? {result}')