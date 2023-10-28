from main import Vector

v = Vector()
v.read("vector1.txt")
u = Vector()
u.read("vector2.txt")
try:
    sum_result = v.addvector(u)
    multiplication_result = v.multiplication(u)
    sub_result = v.substructvector(u)
    division_result = v.division(u)

    v.write("results.txt", sum_result, multiplication_result, sub_result, division_result)

except ValueError as f:
    print(str(f))