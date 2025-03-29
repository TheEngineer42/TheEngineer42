import random

def creating_votes():
    global responses_as_string
    global votes
    response_choice = ['ano', 'nie']
    amount_of_voters = int(input('enter how many people voted: '))
    votes = []

    for _ in range(amount_of_voters):
        response = random.choice(response_choice)
        votes.append(response)

    print(votes)
    responses_as_string = '\n'.join(votes)
    print(responses_as_string)
    print("==================")

def file_with_votes():
    with open('spokojnost.txt', 'w') as file:
        file.write(responses_as_string)

    with open('spokojnost.txt', 'r') as file:
        content = file.read()
        print(content)

def count():
    global amount_ano
    global amount_nie
    global amount_total
    amount_ano = votes.count('ano')
    amount_nie = votes.count('nie')
    amount_total = len(votes)

    print(amount_ano)
    print(amount_nie)
    print(amount_total)
    


creating_votes()
file_with_votes()
count()