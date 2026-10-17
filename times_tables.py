number = int(input("what number do you want the table for?"))
print("")
for i in range(1,11):
    result=number * i
    print(f"{number} x {i} = {result}")
    