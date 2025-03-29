import random
response_choice = ['ano', 'nie']
votes = []

for _ in range(10):
    response = random.choice(response_choice)
    votes.append(response)

print(votes)
responses_as_string = '\n'.join(votes)
print(responses_as_string)
print("==================")

with open('spokojnost.txt', 'w') as file:
    file.write(responses_as_string)

with open('spokojnost.txt', 'r') as file:
    content = file.read()
    print(content)