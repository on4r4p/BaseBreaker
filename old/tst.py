output = []

code_input = str(input("Enter your cipher here: "))
split_code = code_input.split(",")

split_code = [int(i) for i in split_code]

print(split_code)

for i in split_code:
    output.append(i)
    print(i)

