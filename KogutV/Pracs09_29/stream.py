from pyxtension.streams import stream

class Factory:
    def __init__(self, type):
        self.type = type

    def get_type(self):
        return self.type

my_list = (Factory("Glass"), Factory("Wood"), Factory("Iron"))
print("Default list:")
for item in my_list:
    print(item.get_type())

my_stream = (stream(my_list).map(lambda type: type.get_type()).filter(lambda type: type=="Glass").toList())
print("Filtered:") 
for item in my_stream:
    print(item)