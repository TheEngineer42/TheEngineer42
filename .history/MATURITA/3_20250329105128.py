import random
answer = ['ano', 'nie']
all_answers = []

for _ in range(10):
    n = random.choice(answer)
    all_answers.append(n)

print(all_answers)
in_row = '\n'.join(all_answers)
print(in_row)


with open('spokojnost.txt', 'w') as file:
    file.write(in_row)

with open('spokojnost.txt', 'r') as file:
    content = file.read()
    print(content)