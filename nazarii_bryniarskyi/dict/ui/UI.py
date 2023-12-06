from nazarii_bryniarskyi.dict.bl.UserStack import UserStack, User


if __name__ == '__main__':
    stack = UserStack()

    stack.add(User('username1', 'name1', 'surname1', 32))
    stack.add(User('username2', 'name2', 'surname2', 5))
    stack.add(User('username3', 'name3', 'surname3', 33))

    stack.update('username1', name='name11')
    stack.remove('username3')

    print(stack)
