from abc import ABC, abstractmethod
#abstract product - Button
class Button(ABC):
    @abstractmethod
    def display(self):
        pass
#abstract product - checkbox
class Checkbox(ABC):
    @abstractmethod
    def display(self):
        pass
#concrete product - Windows
class WindowsButton(Button):
    def display(self):
        print("Displaying Windows Button")
class WindowsCheckbox(Checkbox):
    def display(self):
        print("Displaying Windows Checkbox")
#concrete product - Mac
class MacButton(Button):
    def display(self):
        print("Displaying Mac Button")
class MacCheckbox(Checkbox):
    def display(slef):
        print("Displaying Mac Checkbox")
#abstract Factory
class GUIFactory(ABC):
    @abstractmethod
    def create_button(self):
        pass
    @abstractmethod
    def create_checkbox(self):
        pass
#concrete factory - Windows
class WindowsFactory(GUIFactory):
    def create_button(self):
        return WindowsButton()
    def create_checkbox(self):
        return WindowsCheckbox()
#concrete factory - Mac
class MacFactory(GUIFactory):
    def create_button(self):
        return MacButton()
    def create_checkbox(self):
        return MacCheckbox()
#client side
def create_ui(factory):
    button = factory.create_button()
    checkbox = factory.create_checkbox()
    button.display()
    checkbox.display()
# Choose a factory
factory = WindowsFactory()
create_ui(factory)