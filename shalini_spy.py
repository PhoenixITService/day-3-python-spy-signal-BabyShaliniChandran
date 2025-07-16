input=input().split()
input=list(input)
sequence=input[1::3]
reversed=sequence[::-1]
output=""
for num in reversed:
    output+=chr(int(num))
print(output)