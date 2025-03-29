import random
answer = ['ano', 'nie']


for _ in range(10):
    n = random.choice(answer)
    all_answers = []
    all_answers.append(n)

print(all_answers)