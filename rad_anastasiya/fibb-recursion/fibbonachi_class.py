from constants import *


class Fibbonachi:
    def __init__(self, input_data: list, stop_criteria: float):
        self.input_data = input_data
        self.stop_criteria = stop_criteria

    def fibbonachi_algorithm(self, output: list) -> list:
        if (len(output) == 0):
            output = [i for i in self.input_data]
        next_one = 0
        try:
            next_one = output[-1] + output[-2]
        except IndexError:
            print(NOT_ENOUGH_DATA)
            exit(-1)
        if next_one < self.stop_criteria:
            output.append(next_one)
            return self.fibbonachi_algorithm(output)
        else:
            return output
