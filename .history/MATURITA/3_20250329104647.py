import random
answer = ['ano', 'nie']
all_answers = []

for _ in range(10):
    n = random.choice(answer)
    all_answers.append(n)

print(all_answers)
in_row = '\n'.join(all_answers)
print(in_row)