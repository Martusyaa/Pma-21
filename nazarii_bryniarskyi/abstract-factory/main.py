from Factory import MacFactory, WindowsFactory


def main():

    button_mac = MacFactory.createButton()
    button_windows = WindowsFactory.createButton()

    print(button_mac.press())
    print(button_windows.press())


main()
