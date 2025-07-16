input=list(map(int,input("Enter the input:").split()))
sequence=input[1::3]
reversed=sequence[::-1]
output=""
for num in reversed:
    output+=chr(num)
print(output)