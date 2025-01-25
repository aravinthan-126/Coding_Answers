flames = ['F', 'L', 'A', 'M', 'E', 'S']
a=list(input("Enter the first name : ").lower())
b=list(input("Enter the second name : ").lower())
for i in range(len(a)-1,-1,-1):
    for j in range(len(b)-1,-1,-1):
        if a[i]==b[j]:
            a.pop(i)
            b.pop(j)
            break
c=len(a)+len(b)
while len(flames) > 1:
    index = (c % len(flames)) - 1
    if index >= 0:
        right = flames[index + 1:]
        left = flames[:index]
        flames = right + left
    else:
        flames = flames[:len(flames) - 1]
relationships = {'F': 'Friends','L': 'Lovers','A': 'Affection','M': 'Marriage','E': 'Enemies','S': 'Siblings'}
print(f"The relationship is: {relationships[flames[0]]}") 