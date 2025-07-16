input=list(map(int,input("Enter the input:").split()))
sequence=input[::2]
reversed=sequence[::-1]
print(reversed)
output=""
for num in reversed:
    output+=chr(num)
print(output)