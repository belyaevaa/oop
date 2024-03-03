#Симуляция кроссплатформенного приложения при помощи абстрактной фабрики
#фабрика должна генерировать набор контроллов для различных ОС
#Все контроллы наследуются от базового класса Control(setPos, getPos)
#создадим по примеру контроллы: Form, Label, TextBox, ComboBox, Button
#Абстрактный класс с сетр/гетр
class Control:
    def __init__(self):
        self.x = 0
        self.y = 0

    def setPosition(self, x, y):
        self.x = x
        self.y = y

    def getPosition(self):
        print(f"Вызван метод getPosition из контролла {type(self).__name__}")
        return "(" + str(self.x) + ", " + str(self.y) + ")"


# Класс формы с наследованием
# все объекты будут здесь
class Form(Control):
    def __init__(self):
        super().__init__()
        self.controls = []
        print("Форма создана")

    def addControl(self, control):
        self.controls.append(control)

    def getControls(self):
        return self.controls

    def getInfo(self):
        print("\n.....Форма......")
        print("Cоздание формы с координатами" + self.getPosition())
        for i in self.getControls():
            if type(i).__name__ != "ComboBox":
                print(f"{type(i).__name__} = " + i.getText())
                print(f"{type(i).__name__} Coords = " + i.getPosition())
            else:
                print(f"{type(i).__name__} : ")
                for j in i.getItems():
                    print("   - " + j)
                print(f"{type(i).__name__} Coords = " + i.getPosition())

        print("\n")


class Label(Control):
    def __init__(self):
        super().__init__()
        self.text = ""

    def setText(self, text):
        print("- setText -для- Label")
        self.text = text

    def getText(self):
        print("- getText -для- Label")
        return self.text


class TextBox(Control):
    def __init__(self):
        super().__init__()
        self.text = ""

    def setText(self, text):
        print("- setText -для- TextBox")
        self.text = text

    def getText(self):
        print("- getText -для- TextBox")
        return self.text

    def onValueChanged(self):
        print("- onValueChanged -для- TextBox")


class ComboBox(Control):
    def __init__(self):
        super().__init__()
        self.selectedIndex = -1
        self.items = []

    def setSelectedIndex(self, index):
        print("- setSelectedIndex -для- ComboBox")
        self.selectedIndex = index

    def getSelectedIndex(self):
        print("- getSelectedIndex -для- ComboBox")
        return self.selectedIndex

    def setItems(self, items):
        print("- setItems -для- ComboBox")
        self.items = items

    def getItems(self):
        print("- getItems -для- ComboBox")
        return self.items

    def getText(self):
        return f"{type(self).__name__} with selected index {self.getSelectedIndex()}"

class Button(Control):
    def __init__(self):
        super().__init__()
        self.text = ""

    def setText(self, text):
        print("- setText -для- Button")
        self.text = text

    def getText(self):
        print("- getText -для- Button")
        return self.text

    def click(self):
        print("- click -для- Button")

#создаем классы контролов отдельно для каждой ОС
class WindowsLabel(Label):
    def __init__(self):
        super().__init__()

class LinuxLabel(Label):
    def __init__(self):
        super().__init__()

class MacOSLabel(Label):
    def __init__(self):
        super().__init__()

class WindowsTextBox(TextBox):
    def __init__(self):
        super().__init__()

class LinuxTextBox(TextBox):
    def __init__(self):
        super().__init__()

class MacOSTextBox(TextBox):
    def __init__(self):
        super().__init__()

class WindowsComboBox(ComboBox):
    def __init__(self):
        super().__init__()

class LinuxComboBox(ComboBox):
    def __init__(self):
        super().__init__()




class MacOSComboBox(ComboBox):
    def __init__(self):
        super().__init__()

class WindowsButton(Button):
    def __init__(self):
        super().__init__()

class LinuxButton(Button):
    def __init__(self):
        super().__init__()

class MacOSButton(Button):
    def __init__(self):
        super().__init__()


#Создаем класс-фабрику для генерации контролов
class ControlFactory:
    def createForm(self):
        pass

    def createLabel(self):
        pass

    def createTextBox(self):
        pass

    def createComboBox(self):
        pass

    def createButton(self):
        pass

#Создаем класс контролов для различных ОС
class WindowsFactory(ControlFactory):
    def __init__(self):
        print("Создан объект Windows ")

    def createForm(self):
        return Form()

    def createLabel(self):
        return WindowsLabel()

    def createTextBox(self):
        return WindowsTextBox()

    def createComboBox(self):
        return WindowsComboBox()

    def createButton(self):
        return WindowsButton()


class LinuxFactory(ControlFactory):
    def __init__(self):
        print("Создан объект Linux ")

    def createForm(self):
        return Form()

    def createLabel(self):
        return LinuxLabel()

    def createTextBox(self):
        return LinuxTextBox()

    def createComboBox(self):
        return LinuxComboBox()

    def createButton(self):
        return LinuxButton()


class MacOSFactory(ControlFactory):
    def __init__(self):
        print("Создан объект MacOS")

    def createForm(self):
        return Form()

    def createLabel(self):
        return MacOSLabel()

    def createTextBox(self):
        return MacOSTextBox()

    def createComboBox(self):
        return MacOSComboBox()

    def createButton(self):
        return MacOSButton()


if __name__ == "__main__":
    #создаем фабрику под нужную ОС
    factory = LinuxFactory()

    #создаем форму
    form = factory.createForm()

    #контроллы
    label = factory.createLabel()
    textbox = factory.createTextBox()
    combobox = factory.createComboBox()
    button = factory.createButton()

    #Задаем параметры
    label.setText("Организация киберспортивных турниров")
    label.setPosition(0, 1)

    textbox.setText("Выберите дисциплину:")
    textbox.setPosition(1, 1)

    combobox.setItems(["CS2", "DOTA 2", "EA FC24"])
    combobox.setSelectedIndex(1)
    combobox.setPosition(1, 5)

    button.setText("Отправить менеджеру")
    button.setPosition(6, 6)

    #добавление контроллов на форму
    form.addControl(label)
    form.addControl(textbox)
    form.addControl(combobox)
    form.addControl(button)

    form.getInfo()
