from InvalidIndexException import InvalidIndexException


class ArrayList:
    def __init__(self, l=[]):
        if (l.__len__() == 0):
            self.array = []
            self.length = 0
        else:
            self.array = l
            self.length = 1.5 * l.__len__() + 1

    def extend_array(self):
        new_array = [None] * round(self.length * 1.5 + 1)
        for i in range(self.length):
            new_array[i] = self.array[i]
        self.array = new_array

    def add_item(self, item):
        if self.length == len(self.array):
            self.extend_array()
        self.array[self.length] = item
        self.length += 1

    def initialize_array_from_file(self, input_file):
        with open(input_file, 'r') as file:
            lines = file.readlines()
            for line in lines:
                element = line.strip()
                try:
                    element = int(element)
                    self.add_item(element)
                except ValueError:
                    print(f"Incorrect element format: {element}.")

    def save_to_file(self, output_file):
        with open(output_file, 'w') as file:
            for element in self.array:
                file.write(str(element) + '\n')
        print(f"The array is saved in the file: {output_file}")

    def __str__(self):
        result = '['
        for i in range(self.length):
            result += str(self.array[i]) + ','
        if (self.length):
            result = result[:-1]
        result += ']'
        return result


if __name__ == "__main__":
    input_file = "input.txt"
    output_file = "result.txt"

    my_array = ArrayList()
    my_array.initialize_array_from_file(input_file)
    print("list:", my_array)

    while True:
        new_element = input("Type a new item (or Enter to finish): ")
        if not new_element:
            break
        try:
            new_element = int(new_element)
            my_array.add_item(new_element)
        except ValueError:
            print("Incorrect element format. Please enter an integer.")

    my_array.save_to_file(output_file)
