from SomeClass import SomeClass
from pyxtension.streams import stream

array = [SomeClass("Anya"), SomeClass("hello"), SomeClass("honey")]

test_stream = stream(array).map(lambda s : s.doSmth()).toList()

print(test_stream)
