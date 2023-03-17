import core
from id_char import CharIdentification as Ident

def main():
    ident = Ident()

    locker = core.Locker()
    door = core.Door(locker)
    
    core.run(door, ident)

if __name__ == "__main__":
    main()