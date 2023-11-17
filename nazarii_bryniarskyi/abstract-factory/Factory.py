from Button import WindowsButton, MacButton


class Factory:

    def createButton(self):
        pass


class MacFactory(Factory):

    def createButton(self=None):
        return MacButton


class WindowsFactory(Factory):

    def createButton(self=None):
        return WindowsButton


