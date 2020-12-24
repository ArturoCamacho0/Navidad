from datetime import datetime

class Navidad:
    def mensaje(self, month, day):
        if(month == 12 and day == 24):
            return "Feliz noche buena!"
        elif(month == 12 and day == 25):
            return "Feliz navidad!"
        else:
            return "Feliz día en la fecha que estés! <3"

    def mostrar_mensaje(self):
        date = datetime.now()
        mensaje = self.mensaje(date.month, date.day)

        print(("Programación&+").center(30))
        for i in range(1,30,2):
            print(('^'*i).center(30))

        for i in range(3):
            print(('|||').center(30))

        print(('\_____/').center(30))
        print(' '+30*'-')
        print(' (*"*', mensaje ,'*"*)')
        print('-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-')

if __name__ == '__main__':
    navidad = Navidad()
    navidad.mostrar_mensaje()

