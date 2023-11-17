


class Button:

    def press(self):
        pass


class MacButton(Button):

    def press(self=None):
        return "Mac button pressed"


class WindowsButton(Button):

    def press(self=None):
        return "Windows button pressed"
