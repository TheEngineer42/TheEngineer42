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

    
    responses_as_string = '\n'.join(votes)
    print(responses_as_string)
    print("==================\n")
    

def file_with_votes():
    print("=========Subor Spokojnost.txt=========")
    with open('spokojnost.txt', 'w') as file:
        file.write(responses_as_string)

    with open('spokojnost.txt', 'r') as file:
        content = file.read()
        print(content)
    print("=====================================\n")

def count():
    global amount_ano
    global amount_nie
    global amount_total
    amount_ano = votes.count('ano')
    amount_nie = votes.count('nie')
    amount_total = len(votes) # or amount_ano + amount_nie

    print(f"amount of satisfied visitors: {amount_ano}")
    print(f"amount of dissatisfied visitors: {amount_nie}")
    print(f"amount of dissatisfied visitors: {amount_total}")
    
    


creating_votes()
file_with_votes()
count()