import random
from tkinter import*
root = Tk()
root.geometry('500x500')

canvas = Canvas(root,height = 500, width = 500,  bg ='white')
canvas.pack()

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
    print(f"tottal amount of visitors: {amount_total}")

def percentage():
    global percentage_ano
    global percentage_nie
    percentage_ano = round((amount_ano*100)/amount_total,2) #round('some number', places)
    percentage_nie = round((amount_nie*100)/amount_total,2)
    print(f"ano = {percentage_ano}%")
    print(f"nie = {percentage_nie}%")



creating_votes()
file_with_votes()
count()
percentage()

canvas.create_text(250,50,text = f"amount of voters:{amount_total }", font = 'Calibri, 18')
canvas.create_rectangle(10,100,3*percentage_ano,150, fill = 'green')
canvas.create_rectangle(10,200,3*percentage_nie,250, fill = 'red')

canvas.create_text(310,125, text = f"{percentage_ano}%" , font = 'Calibri, 18')
canvas.create_text(310,225, text = f"{percentage_nie}%", font = 'Calibri, 18')

def vysledky():
    print("\n=========Subor vysledky.txt=========")
    with open('vysledky.txt', 'w') as file:
        file.write(f"celkovy pocet hlasujucich: {amount_total}\npocet spokojnych: {percentage_ano}\npocet nespokojnych: {percentage_nie}")

    with open("vysledky.txt", 'r') as file:
        content = file.read()
        print(content)
    print("==================\n")



root.mainloop()
