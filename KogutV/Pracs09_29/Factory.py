from abc import ABC, abstractmethod

class OS(ABC):
    @abstractmethod
    def name(self):
        pass

    @abstractmethod
    def update(self):
        pass

class App(ABC):
    @abstractmethod
    def version(self):
        pass

    @abstractmethod
    def size(self):
        pass

class AbstractFactory(ABC):
    @abstractmethod
    def create_OS(self) -> OS:
        pass

    @abstractmethod
    def create_App(self) -> App:
        pass

class macOS(OS):
    def name(self):
        print("Ventura")

    def update(self):
        print("Sonoma")

class WindowsOS(OS):
    def name(self):
        print("Windows 10")

    def update(self):
        print("Windows 11")

class Pixelmator_Pro(App):
    def version(self):
        print("10.6.9")

    def size(self):
        print("350mb")

class Photoshop(App):
    def version(self):
        print("25.0")

    def size(self):
        print("500mb")

class macOSFactory(AbstractFactory):
    def create_OS(self) -> OS:
        return macOS()

    def create_App(self) -> App:
        return Pixelmator_Pro()

class WindowsFactory(AbstractFactory):
    def create_OS(self) -> OS:
        return WindowsOS()

    def create_App(self) -> App:
        return Photoshop()

macos_factory = macOSFactory()
macos_os = macos_factory.create_OS()
macos_app = macos_factory.create_App()

windows_factory = WindowsFactory()
windows_os = windows_factory.create_OS()
windows_app = windows_factory.create_App()

macos_os.name()
macos_os.update()
macos_app.version()
macos_app.size()

windows_os.name()
windows_os.update()
windows_app.version()
windows_app.size()
