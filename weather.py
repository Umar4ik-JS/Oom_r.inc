#Библиотеки
from tkinter import Tk, Button, Label, Entry
from tkinter.constants import END
import pyowm
# Логига приложухи
def delet():
    enter.delete(0, END)
def weath():
    try:
        town = enter.get()

        owm = pyowm.OWM("60367da15b3d6986f6159ed85cb744d6", language = "ru")
        observation = owm.weather_at_place(town)
        wit = observation.get_weather()
        global temp
        temp = wit.get_temperature("celsius")["temp"]
        nebo = wit.get_detailed_status()
    
        weather = Label(inter, text = "Сейчас в городе/стране " + "\n" + str(enter.get()) + "\n" + str(temp) + " градусов цельсия\n" + str(nebo),
                        background = "#28C8E1", 
                        justify = "left", 
                        font = "Arial 12")
        weather.place(x = "20", y = "180")
    
    except pyowm.exceptions.api_call_error.APIInvalidSSLCertificateError:
        error2 = Tk()
        error2.geometry("210x100+300+100")
        error2.resizable(False,False)
        error2.title("ERROR")
        error_2 = Label(error2, text = "ERRNO 2. Нет подключения\nк интернету!")
        error_2.pack()
        error2.update_idletasks()

    except pyowm.exceptions.api_response_error.NotFoundError:
        error3 = Tk()
        error3.geometry("210x100+300+100")
        error3.resizable(False,False)
        error3.title("ERROR")
        error_3 = Label(error3, text = "ERRNO 3. Такого города/страны \nне существует \nили допущена \nграмматическая ошибка")
        error_3.pack()
        error3.update_idletasks()

    if temp <= -5:
        sovet = Label(inter, text = "Сейчас пздц холодно, если не хочешь \nотморозить себе что - нибудь, то одевайся тепло",
                        background = "#28C8E1", 
                        justify = "left", 
                        font = "Arial 12")
        sovet.place(x = "20", y = "260")
    elif temp > 5 and temp <= 0:
        sovet = Label(inter, text = "Сейчас холодно, одевайся потеплее",
                        background = "#28C8E1", 
                        justify = "left", 
                        font = "Arial 12")
        sovet.place(x = "20", y = "260")
    elif temp > 0 and temp <=10:
        sovet = Label(inter, text = "Прохладно, надень штаны и верхную \nодежду с длинными рукавами.",
                        background = "#28C8E1", 
                        justify = "left", 
                        font = "Arial 12")
        sovet.place(x = "20", y = "260")
    elif temp > 10 and temp <= 20:
        sovet = Label(inter, text = "Всю равно прохладно, простудишся. \nНакинь на себя хотя бы лёгкую курточку",
                        background = "#28C8E1", 
                        justify = "left", 
                        font = "Arial 12")
        sovet.place(x = "20", y = "260")
    elif temp > 20 and temp <= 30:
        sovet = Label(inter, text = "Уже тепло и можешь выходить\n в шортах, если хочешь",
                        background = "#28C8E1", 
                        justify = "left", 
                        font = "Arial 12")
        sovet.place(x = "20", y = "260")
    elif temp > 30 and temp <= 40:
        sovet = Label(inter, text = "ЖАРКОООО! \nНе ходи под прямыми лучами солнца!\nПогода самое то что бы \nпойти на купание",
                        background = "#28C8E1", 
                        justify = "left", 
                        font = "Arial 12")
        sovet.place(x = "20", y = "260")
    else: 
        sovet = Label(inter, text = "Просто не выходи ни куда, \nсейчас больше сорока градусов.\n Только сумашедший выйдет на улицу \nв такое время",
                        background = "#28C8E1", 
                        justify = "left", 
                        font = "Arial 12")
        sovet.place(x = "20", y = "260")
#GUI
if __name__ == "__main__":
    inter = Tk()
    inter.geometry("325x390+300+100")
    inter.resizable(False,False)
    inter.title("PYWeather")
    inter.configure(background = "#28C8E1")
    inter.update_idletasks()

    global enter
    enter = Entry(font = ("Arial","19"), 
                justify = "center", 
                relief = "groove", 
                bd = "2")
    enter.place(x = "20",y = "70", width = "273",height = "45")

    btn = Button(relief = "groove", 
                text = "Показать погоду", 
                height = "2", 
                width = "28", 
                activebackground = "#37ABBD", 
                activeforeground = "#ffffff", 
                command = weath)
    btn.place(x= "20", y = "113")

    clear = Button(relief = "groove", 
                text = "Очистить", 
                height = "2", 
                width = "9", 
                activebackground = "#37ABBD", 
                activeforeground = "#ffffff", 
                command = delet)
    clear.place(x = "220", y = "113")

    city = Label(text = "Введите город:", 
                background = "#28C8E1", 
                justify = "center", 
                font = "Arial 14")
    city.place(x = "90", y = "35")

    inter.mainloop()

else:
    error1 = Tk()
    error1.geometry("210x100+300+100")
    error1.resizable(False,False)
    error1.title("ERROR")
    error_1 = Label(error1, text = "Во время запуска \nпрограммы возникла \nнеизветсная ошибка!")
    error_1.pack()
    error1.mainloop()
    error1.update_idletasks()
