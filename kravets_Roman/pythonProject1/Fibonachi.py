try:
    with open("readme.txt") as f:
        numbers = f.readline().strip().split()
        first_num, second_num = map (int, numbers)
except FileNotFoundError:
    print("The file 'readme.txt' does not exist.")
    exit(-1)
except Exception as e:
    print(f"An error occurred: ")
    exit(-1)

while True:
    try:
        nterms = int(input("How many terms? "))
        if nterms <= 0:
            raise ValueError("Please enter a positive integer")
        break
    except ValueError as ve:
        print(f"Invalid input:")

print(f"Starting with {first_num} and {second_num}")
count = 0

print("Fibonacci sequence:")
while count < nterms:
    print(first_num)
    nth_num = first_num + second_num
    first_num = second_num
    second_num = nth_num
    count += 1
