import tabulate
import inquirer
import random
import os ,time, sys
from time import sleep
import ruff


class Charcter:
    def __init__(self, gender, name, job, attack, defense, hp, mp, level, money):
        self.gender = gender
        self.name = name
        self.job = job
        self.attack = attack
        self.defense = defense
        self.hp = hp
        self.mp = mp
        self.level = level
        self.money = money


    def morelife(self):
        self.hp += 15

    def moremoney(self):
        self.money += 50

    def levelup(self):
        self.level += 1
        x = 10
        self.hp += x
        self.mp += x
        self.attack += x
        self.defense += x


class Monster:
    def __init__(self, name, attack, defense, hp, level):
        self.name = name
        self.attack = attack
        self.defense = defense
        self.hp = hp
        self.level = level

    def levelup(self ):
        self.hp += random.randint(5, 15)
        self.attack += random.randint(5, 15)
        self.defense += random.randint(5, 15)


New_Charc = Charcter('Male', 'Fighter', 1, 1, 1, 1, 1, 1, 1)
evilmon = Monster('full_name', random.randint(9, 15), random.randint(9, 15), random.randint(30, 50), 1)
evilmon2 = Monster('full_name', random.randint(15, 25), random.randint(15, 25), random.randint(50, 70), 2)
evilmon3 = Monster('full_name', random.randint(25, 30), random.randint(25, 30), random.randint(70, 90), 3)
evilmon4 = Monster('full_name', random.randint(30, 42), random.randint(30, 42), random.randint(100, 120), 4)


def Evilmon():
    first_names = (
    'colossal', 'gigantic', 'mountainous', 'cyclops', 'ogre', 'demon', 'devil', 'epic', 'hooligan', 'cyclops', 'vandal',
    'mammoth')
    last_names = (
    'Kali', 'Anubis', 'Diablo', 'Hannibal', 'Necro', 'Ravana', 'Yama', 'Raven', 'Reaper', 'marduk', 'thana', 'death')
    full_name = random.choice(first_names) + " " + random.choice(last_names)
    full_name2 = random.choice(first_names) + " " + random.choice(last_names)
    full_name3 = random.choice(first_names) + " " + random.choice(last_names)
    full_name4 = random.choice(first_names) + " " + random.choice(last_names)
    evilmon = Monster(full_name, random.randint(9, 15), random.randint(9, 15), random.randint(30, 50), 1)
    evilmon2 = Monster(full_name2, random.randint(15, 25), random.randint(15, 25), random.randint(50, 70), 2)
    evilmon3 = Monster(full_name3, random.randint(25, 30), random.randint(25, 30), random.randint(70, 90), 3)
    evilmon4 = Monster(full_name4, random.randint(30, 42), random.randint(30, 42), random.randint(100, 120), 4)
    f = open("evilmon.txt", "w")
    f.write(str(evilmon.__dict__))
    f.close()
    f = open("evilmon2.txt", "w")
    f.write(str(evilmon2.__dict__))
    f.close()
    f = open("evilmon3.txt", "w")
    f.write(str(evilmon3.__dict__))
    f.close()
    f = open("evilmon4.txt", "w")
    f.write(str(evilmon4.__dict__))
    f.close()

def typingPrint(text):
    for character in text:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.05)
typingPrint("...............")

def Shop():
    f = open("Charcter.txt")
    x = f.readline()
    New_Charc = eval(x)
    print("Welcome to the Shop. How can I help you?")
    questions = [
        inquirer.List('Shop',
                      message="What would you like to buy?",
                      choices=['Hp Booster (30$)', 'Mp Booster (30$)','Attack Booster (100$)', 'Golden Aura Booster (250$)', 'Go back'],
                      ),
    ]
    money = ("Money: " + str(New_Charc['money']))
    print(f'{money:_^20}')
    answers = inquirer.prompt(questions)
    action = answers.get('Shop')
    if action == 'Hp Booster (30$)' and New_Charc['money'] > 29:
        print(New_Charc['name'] + " has acquired Hp Booster")
        print("Hp:" + str(New_Charc['hp']))
        print("Drink")
        New_Charc['hp'] += 25
        print("Hp:" + str(New_Charc['hp']))
        New_Charc['money'] -= 30
        print("Thank you for the purchase")
        f = open("Charcter.txt", "w")
        f.write(str(New_Charc))
        f.close()
        Shop()
    elif action == 'Mp Booster (30$)' and New_Charc['money'] > 29:
        print(New_Charc['name'] + " has acquired Mp Booster")
        print("Mp:" + str(New_Charc['mp']))
        print("Drink")
        New_Charc['mp'] += 35
        print("Mp:" + str(New_Charc['mp']))
        New_Charc['money'] -=  30
        print("Thank you for the purchase")
        f = open("Charcter.txt", "w")
        f.write(str(New_Charc))
        f.close()
        Shop()
    elif action == 'Attack Booster (100$)' and New_Charc['money'] > 99:
        print(New_Charc['name'] + " has acquired Attack Booster")
        print("Attack:" + str(New_Charc['attack']))
        print("Drink")
        New_Charc['attack'] += 20
        print("Attack:" + str(New_Charc['attack']))
        New_Charc['money'] -=  100
        print("Thank you for the purchase")
        f = open("Charcter.txt", "w")
        f.write(str(New_Charc))
        f.close()
        Shop()
    elif action == 'Golden Aura Booster (250$)' and New_Charc['money'] > 249:
        print(New_Charc['name'] + " has acquired Golden Aura Booster")
        print("Attack:" + str(New_Charc['attack']))
        print("Mp:" + str(New_Charc['mp']))
        print("Hp:" + str(New_Charc['hp']))
        print("Drink")
        New_Charc['attack'] += 40
        New_Charc['hp'] += 40
        New_Charc['mp'] += 40
        print("Attack:" + str(New_Charc['attack']))
        print("Hp:" + str(New_Charc['hp']))
        print("Mp:" + str(New_Charc['mp']))
        New_Charc['money'] -= 250
        print("Thank you for the purchase")
        f = open("Charcter.txt", "w")
        f.write(str(New_Charc))
        f.close()
        Shop()
    elif action == 'Go back':
        idle()
    else:
        print("Not enough money")
        Shop()


def lose():
    f = open("Charcter.txt")
    x = f.readline()
    New_Charc = eval(x)
    Score = int(New_Charc['attack']) + int(New_Charc['defense']) * int(New_Charc['level'])
    f = open("Score.txt", "w")
    f.write(str(Score))
    f.close()




def idle():
    Evilmon()
    questions = [
        inquirer.List('option2',
                      message="What would you like to do?",
                      choices=['㊝ Enter the Dungeon', '➹ Shop', '◕ Save Game', '♞ Stats','◀ Back to the main menu'],
                      ),
    ]
    answers = inquirer.prompt(questions)
    option2 = answers.get('option2')
    if option2 == '➹ Shop':
        Shop()
    elif option2 == '◕ Save Game':
        saveCharcter()
    elif option2 == '♞ Stats':
        charcterStats()
    elif option2 == '㊝ Enter the Dungeon':
        Fight()
    elif option2 == '◀ Back to the main menu':
        welcome()
    else:
        error()


def backtoidle():
    questions = [
        inquirer.List('option3',
                      message="Go back?",
                      choices=['Yes', 'No'],
                      ),
    ]
    answers = inquirer.prompt(questions)
    option3 = answers.get('option3')
    if option3 == 'Yes':
        idle()
    elif option3 == 'No':
        backtoidle()
    else:
        error()


def error():
    print("Error 01")
    welcome()


def cls():
    sleep(3)
    os.system('cls' if os.name=='nt' else 'clear')


def creatcharcter():
    questions = [
        inquirer.List('Gender',
                      message="What is your Gender?",
                      choices=['Male', 'Female', 'Other'],
                      ),
        inquirer.Text('Name', message="What's your name?"),
        inquirer.List('Job',
                      message="Choose your Job:",
                      choices=["Fighter", "Archer", "Mage"],
                      ),
    ]
    answers = inquirer.prompt(questions)
    g = answers.get('Gender')
    n = answers.get('Name')
    r = answers.get('Job')
    a = random.randint(9, 21)
    d = random.randint(9, 21)
    h = 100
    m = 100
    l = 1
    c = 100
    if r == "Fighter":
        a += 5
    elif r == "Archer":
        d += 5
    elif r == "Mage":
        m = 200


    New_Charc = Charcter(g, n, r, a, d, h, m, l, c)
    f = open("Charcter.txt", "w")
    f.write(str(New_Charc.__dict__))
    f.close()
    cls()
    idle()


def saveCharcter():
    f = open("Charcter.txt")
    New_Charc = f.readline()
    f.close()
    f = open("Charcter.txt", "w")
    f.write(str(New_Charc))
    f.close()
    cls()
    idle()


def loadCharacter():
    f = open("Charcter.txt")
    x = f.readline()
    C = eval(x)
    New_Charc = Charcter(C['gender'],C['name'],C['job'],C['attack'],C['defense'],C['hp'],C['mp'],C['level'],C['money'],)
    idle()


def charcterStats():
    f = open("Charcter.txt")
    x = f.readline()
    New_Charc = eval(x)
    dataset = [New_Charc]
    header = dataset[0].keys()
    rows = [x.values() for x in dataset]
    print(tabulate.tabulate(rows, header, tablefmt='grid'))
    backtoidle()


def charcterStatsuser():
    f = open("Charcter.txt")
    x = f.readline()
    New_Charc = eval(x)
    dataset = [New_Charc]
    header = dataset[0].keys()
    rows = [x.values() for x in dataset]
    print(tabulate.tabulate(rows, header, tablefmt='grid'))


def welcome():
    print('''
█▀▄▀█ █ █▄░█ █   █▀█ █▀█ █▀▀
█░▀░█ █ █░▀█ █   █▀▄ █▀▀ █▄█
    ''')
    questions = [
        inquirer.List('options',
                      message="Welcome to Mini-Rpg choose an option",
                      choices=['Start Game', 'Load Game', 'Exit Game'],
                      ),
    ]
    answers = inquirer.prompt(questions)
    option = answers.get('options')
    if option == 'Start Game':
        creatcharcter()
    elif option == 'Load Game':
        loadCharacter()
    elif option == 'Exit Game':
        exit()
    else:
        error()


# welcome()




def Evilstats():
    f = open("evilmon.txt")
    x = f.readline()
    evilmon = eval(x)
    dataset = [evilmon]
    header = dataset[0].keys()
    rows = [x.values() for x in dataset]
    print(tabulate.tabulate(rows, header, tablefmt='grid'))

def Evilstats2():
    f = open("evilmon2.txt")
    x = f.readline()
    evilmon2 = eval(x)
    dataset = [evilmon2]
    header = dataset[0].keys()
    rows = [x.values() for x in dataset]
    print(tabulate.tabulate(rows, header, tablefmt='grid'))

def Evilstats3():
    f = open("evilmon3.txt")
    x = f.readline()
    evilmon3 = eval(x)
    dataset = [evilmon3]
    header = dataset[0].keys()
    rows = [x.values() for x in dataset]
    print(tabulate.tabulate(rows, header, tablefmt='grid'))

def Evilstats4():
    f = open("evilmon4.txt")
    x = f.readline()
    evilmon4 = eval(x)
    dataset = [evilmon4]
    header = dataset[0].keys()
    rows = [x.values() for x in dataset]
    print(tabulate.tabulate(rows, header, tablefmt='grid'))


def Fight4():
    f = open("evilmon4.txt")
    x = f.readline()
    evilmon4 = eval(x)
    f = open("Charcter.txt")
    x = f.readline()
    New_Charc = eval(x)

    def monattack():
        typingPrint(" ★ ★ ★ ★ ★ ")
        print(" ")
        print(evilmon4['name'] + " Attack!")
        print(New_Charc['name'] + " Hp: " + str(New_Charc['hp']))
        print("SLASHHH")
        New_Charc['hp'] -= evilmon4['attack']
        print(New_Charc['name'] + " Hp: " + str(New_Charc['hp']))
        print("--------------------------------------------------------")
        f = open("Charcter.txt", "w")
        f.write(str(New_Charc))
        f.close()
        f = open("evilmon4.txt", "w")
        f.write(str(evilmon4))
        f.close()
        cls()

    def monpoison():
        typingPrint(" ★ ★ ★ ★ ★ ")
        print(" ")
        print(evilmon4['name'] + " Attack!")
        print("Hp: " + str(New_Charc['hp']))
        print("SLASHHH")
        New_Charc['hp'] -= evilmon4['attack']
        print("Hp: " + str(New_Charc['hp']))
        print(evilmon4['name'] + " has been poisoned!")
        print(evilmon4['name'] + " HP:" + str(evilmon4['hp']))
        evilmon4['hp'] =- 15
        print(evilmon4['name'] + " HP:" + str(evilmon4['hp']))
        print("--------------------------------------------------------")
        f = open("Charcter.txt", "w")
        f.write(str(New_Charc))
        f.close()
        f = open("evilmon4.txt", "w")
        f.write(str(evilmon4))
        f.close()
        cls()

    print(New_Charc['name'] +" VS "+ evilmon4['name'])
    questions = [
        inquirer.List('Action',
                      message="What are you going to do?",
                      choices=['Attack', 'Defend','Skill', 'Potion'],
                      ),
    ]
    answers = inquirer.prompt(questions)
    action = answers.get('Action')

    if action == 'Attack':
        print(New_Charc['name'] +" Attack!")
        print(evilmon4['name'] + " Hp: " + str(evilmon4['hp']))
        print("SLASHHH")
        evilmon4['hp'] -= New_Charc['attack']
        print(evilmon4['name'] + " Hp: " + str(evilmon4['hp']))
        print("--------------------------------------------------------")
        f = open("Charcter.txt", "w")
        f.write(str(New_Charc))
        f.close()
        f = open("evilmon4.txt", "w")
        f.write(str(evilmon4))
        f.close()
        monattack()

    elif action == 'Defend':
        print(New_Charc['name'] +" Defend!")
        print("Defence is up")
        print(evilmon4['name'] +" Is about to attack")
        print(New_Charc['name'] + " Hp: " + str(New_Charc['hp']))
        print("SLASHHH")
        defence = evilmon4['attack'] - New_Charc['defense']
        New_Charc['hp'] -= defence
        print(New_Charc['name'] + " Hp: " + str(New_Charc['hp']))
        print("--------------------------------------------------------")
        f = open("Charcter.txt", "w")
        f.write(str(New_Charc))
        f.close()
        f = open("evilmon4.txt", "w")
        f.write(str(evilmon4))
        f.close()

    elif action == 'Skill' and New_Charc['job'] == 'Fighter':
        questions = [
            inquirer.List('Skill',
                          message="Skills",
                          choices=['Super Slice (10 MP)', 'Triple Chop (15 MP)', 'Go Back'],
                          ),
        ]
        answers = inquirer.prompt(questions)
        Skills = answers.get('Skill')
        if Skills == 'Super Slice (10 MP)' and New_Charc['mp'] > 10:
            print(New_Charc['name'] + " Super Slice!")
            print(New_Charc['name'] + " MP:" + str(New_Charc['mp']))
            print(New_Charc['name'] + " Gained Attack boost")
            New_Charc['mp'] -= 10
            print(New_Charc['name'] + " MP:" + str(New_Charc['mp']))
            print(evilmon4['name'] + " Hp: " + str(evilmon4['hp']))
            print("Suuppperr Sllliiiceee!")
            evilmon4['hp'] -= New_Charc['attack'] + 15
            print(evilmon4['name'] + " Hp: " + str(evilmon4['hp']))
            print("--------------------------------------------------------")
            f = open("Charcter.txt", "w")
            f.write(str(New_Charc))
            f.close()
            f = open("evilmon4.txt", "w")
            f.write(str(evilmon4))
            f.close()
            monattack()
        elif Skills == 'Triple Chop (15 MP)' and New_Charc['mp'] > 15:
            print(New_Charc['name'] + " MP:" + str(New_Charc['mp']))
            New_Charc['mp'] -= 15
            print(New_Charc['name'] + " MP:" + str(New_Charc['mp']))
            print("Tttrrrriiipppllleee Ccchhhhoooopppp!")
            print("First Chop!")
            evilmon4['hp'] -= New_Charc['attack'] - 15
            print(evilmon4['name'] + " Hp: " + str(evilmon4['hp']))
            print("Second Chop!")
            evilmon4['hp'] -= New_Charc['attack'] - 10
            print(evilmon4['name'] + " Hp: " + str(evilmon4['hp']))
            print("Last Chop!")
            evilmon4['hp'] -= New_Charc['attack'] - 5
            print(evilmon4['name'] + " Hp: " + str(evilmon4['hp']))
            print("--------------------------------------------------------")
            f = open("Charcter.txt", "w")
            f.write(str(New_Charc))
            f.close()
            f = open("evilmon4.txt", "w")
            f.write(str(evilmon4))
            f.close()
            monattack()
        elif Skills == 'Go Back':
            Fight4()
        else:
            print("Error")

    elif action == 'Skill' and New_Charc['job'] == 'Archer':
        questions = [
            inquirer.List('Skill',
                          message="Skills",
                          choices=['Poison Arrow (10 MP)', 'Charged Shot (15 MP)', 'Go Back'],
                          ),
        ]
        answers = inquirer.prompt(questions)
        Skills = answers.get('Skill')
        if Skills == 'Poison Arrow (10 MP)' and New_Charc['mp'] > 10:
            print(New_Charc['name'] + " Poison Arrow!")
            print(New_Charc['name'] + " MP:" + str(New_Charc['mp']))
            New_Charc['mp'] -= 10
            print(New_Charc['name'] + " MP:" + str(New_Charc['mp']))
            print(evilmon4['name'] + " Hp: " + str(evilmon4['hp']))
            evilmon4['hp'] -= New_Charc['attack'] - 10
            print(evilmon4['name'] + " Hp: " + str(evilmon4['hp']))
            print(evilmon4['name'] + " has been poisoned")
            print("--------------------------------------------------------")
            f = open("Charcter.txt", "w")
            f.write(str(New_Charc))
            f.close()
            f = open("evilmon4.txt", "w")
            f.write(str(evilmon4))
            f.close()
            monpoison()
        elif Skills == 'Charged Shot (15 MP)' and New_Charc['mp'] > 15:
            print(New_Charc['name'] + " MP:" + str(New_Charc['mp']))
            New_Charc['mp'] -= 15
            print(New_Charc['name'] + " MP:" + str(New_Charc['mp']))
            print("Chaaaaaaaaarged Shot!")
            print(New_Charc['name'] + "Has started to charge")
            print("--------------------------------------------------------")
            monattack()
            print("Chaaaaaaaaarged Shot!")
            print(evilmon4['name'] + " Hp: " + str(evilmon4['hp']))
            evilmon4['hp'] -= New_Charc['attack'] + 20
            print(evilmon4['name'] + " Hp: " + str(evilmon4['hp']))
            print("--------------------------------------------------------")
            f = open("Charcter.txt", "w")
            f.write(str(New_Charc))
            f.close()
            f = open("evilmon4.txt", "w")
            f.write(str(evilmon4))
            f.close()
            monattack()
        elif Skills == 'Go Back':
            Fight4()
        else:
            print("Error")


    elif action == 'Skill' and New_Charc['job'] == 'Mage':
        questions = [
            inquirer.List('Skill',
                          message="Skills",
                          choices=['Fireball (10 MP)', 'Ice Dragon (30 MP)', 'Go Back'],
                          ),
        ]
        answers = inquirer.prompt(questions)
        Skills = answers.get('Skill')
        if Skills == 'Fireball (10 MP)' and New_Charc['mp'] > 10:
            print(New_Charc['name'] + " Fireball!")
            print(New_Charc['name'] + " MP:" + str(New_Charc['mp']))
            New_Charc['mp'] -= 10
            print(New_Charc['name'] + " MP:" + str(New_Charc['mp']))
            print(evilmon4['name'] + " Hp: " + str(evilmon4['hp']))
            evilmon4['hp'] -= New_Charc['attack'] + 15
            print(evilmon4['name'] + " Hp: " + str(evilmon4['hp']))
            print("--------------------------------------------------------")
            f = open("Charcter.txt", "w")
            f.write(str(New_Charc))
            f.close()
            f = open("evilmon4.txt", "w")
            f.write(str(evilmon4))
            f.close()
            monattack()
        elif Skills == 'Ice Dragon (30 MP)' and New_Charc['mp'] > 30:
            print(New_Charc['name'] + " MP:" + str(New_Charc['mp']))
            New_Charc['mp'] -= 30
            print(New_Charc['name'] + " MP:" + str(New_Charc['mp']))
            print("Iccccceeeeee DDDDDDrrrrraggooonnn!")
            print(evilmon4['name'] + " Hp: " + str(evilmon4['hp']))
            evilmon4['hp'] -= New_Charc['attack'] + 30
            print(evilmon4['name'] + " Hp: " + str(evilmon4['hp']))
            print("--------------------------------------------------------")
            f = open("Charcter.txt", "w")
            f.write(str(New_Charc))
            f.close()
            f = open("evilmon4.txt", "w")
            f.write(str(evilmon4))
            f.close()
            monattack()
        elif Skills == 'Go Back':
            Fight4()
        else:
            print("Error")

    elif action == 'Potion':
        print(New_Charc['name'] +" Potion!")
        print(New_Charc['name'] + "Hp: " + str(New_Charc['hp']))
        print(New_Charc['name'] + "Mp: " + str(New_Charc['mp']))
        print("Drink")
        print("HP = +15")
        print("MP = +15")
        New_Charc['hp'] += 15
        New_Charc['mp'] += 15
        print(New_Charc['name'] + "Hp: " + str(New_Charc['hp']))
        print(New_Charc['name'] + "Mp: " + str(New_Charc['mp']))
        print("--------------------------------------------------------")
        f = open("Charcter.txt", "w")
        f.write(str(New_Charc))
        f.close()
        f = open("evilmon4.txt", "w")
        f.write(str(evilmon4))
        f.close()
        monattack()
    else:
        print("Error")

    if New_Charc['hp'] < 1:
        print("You lose...")
        lose()
    elif evilmon4['hp'] < 1:
        print("You won!")
        print(New_Charc['name'] +" Leveled up!")
        New_Charc['hp'] += 10
        New_Charc['mp'] += 25
        New_Charc['attack'] += 10
        New_Charc['defense'] += 10
        New_Charc['money'] += 50
        New_Charc['level'] += 1
        print("hp +10, mp +10, attack +10, defense +10, money +50, level +1.")
        f = open("Charcter.txt", "w")
        f.write(str(New_Charc))
        f.close()
        evilmon4['hp'] += 120
        evilmon4['attack'] += 25
        f = open("evilmon4.txt", "w")
        f.write(str(evilmon4))
        f.close()
        charcterStatsuser()
        print("")
        questions = [
            inquirer.List('Continue',
                          message="Continue?",
                          choices=['Yes', 'No'],
                          ),
        ]
        answers = inquirer.prompt(questions)
        action = answers.get('Continue')
        if action == 'Yes':
            Fight()
        elif action == 'No':
            idle()


    else:
        typingPrint("The Battle Continues...")
        print("")
        Fight4()

def Fight3():
    f = open("evilmon3.txt")
    x = f.readline()
    evilmon3 = eval(x)
    f = open("Charcter.txt")
    x = f.readline()
    New_Charc = eval(x)

    def monattack():
        typingPrint(" ★ ★ ★ ★ ★ ")
        print(" ")
        print(evilmon3['name'] + " Attack!")
        print(New_Charc['name'] + " Hp: " + str(New_Charc['hp']))
        print("SLASHHH")
        New_Charc['hp'] -= evilmon3['attack']
        print(New_Charc['name'] + " Hp: " + str(New_Charc['hp']))
        print("--------------------------------------------------------")
        f = open("Charcter.txt", "w")
        f.write(str(New_Charc))
        f.close()
        f = open("evilmon3.txt", "w")
        f.write(str(evilmon3))
        f.close()
        cls()

    def monpoison():
        typingPrint(" ★ ★ ★ ★ ★ ")
        print(" ")
        print(evilmon3['name'] + " Attack!")
        print("Hp: " + str(New_Charc['hp']))
        print("SLASHHH")
        New_Charc['hp'] -= evilmon3['attack']
        print("Hp: " + str(New_Charc['hp']))
        print(evilmon3['name'] + " has been poisoned!")
        print(evilmon3['name'] + " HP:" + str(evilmon3['hp']))
        evilmon3['hp'] =- 15
        print(evilmon3['name'] + " HP:" + str(evilmon3['hp']))
        print("--------------------------------------------------------")
        f = open("Charcter.txt", "w")
        f.write(str(New_Charc))
        f.close()
        f = open("evilmon3.txt", "w")
        f.write(str(evilmon3))
        f.close()
        cls()

    print(New_Charc['name'] +" VS "+ evilmon3['name'])
    questions = [
        inquirer.List('Action',
                      message="What are you going to do?",
                      choices=['Attack', 'Defend','Skill', 'Potion'],
                      ),
    ]
    answers = inquirer.prompt(questions)
    action = answers.get('Action')

    if action == 'Attack':
        print(New_Charc['name'] +" Attack!")
        print(evilmon3['name'] + " Hp: " + str(evilmon3['hp']))
        print("SLASHHH")
        evilmon3['hp'] -= New_Charc['attack']
        print(evilmon3['name'] + " Hp: " + str(evilmon3['hp']))
        print("--------------------------------------------------------")
        f = open("Charcter.txt", "w")
        f.write(str(New_Charc))
        f.close()
        f = open("evilmon3.txt", "w")
        f.write(str(evilmon3))
        f.close()
        monattack()

    elif action == 'Defend':
        print(New_Charc['name'] +" Defend!")
        print("Defence is up")
        print(evilmon3['name'] +" Is about to attack")
        print(New_Charc['name'] + " Hp: " + str(New_Charc['hp']))
        print("SLASHHH")
        defence = evilmon3['attack'] - New_Charc['defense']
        New_Charc['hp'] -= defence
        print(New_Charc['name'] + " Hp: " + str(New_Charc['hp']))
        print("--------------------------------------------------------")
        f = open("Charcter.txt", "w")
        f.write(str(New_Charc))
        f.close()
        f = open("evilmon3.txt", "w")
        f.write(str(evilmon3))
        f.close()

    elif action == 'Skill' and New_Charc['job'] == 'Fighter':
        questions = [
            inquirer.List('Skill',
                          message="Skills",
                          choices=['Super Slice (10 MP)', 'Triple Chop (15 MP)', 'Go Back'],
                          ),
        ]
        answers = inquirer.prompt(questions)
        Skills = answers.get('Skill')
        if Skills == 'Super Slice (10 MP)' and New_Charc['mp'] > 10:
            print(New_Charc['name'] + " Super Slice!")
            print(New_Charc['name'] + " MP:" + str(New_Charc['mp']))
            print(New_Charc['name'] + " Gained Attack boost")
            New_Charc['mp'] -= 10
            print(New_Charc['name'] + " MP:" + str(New_Charc['mp']))
            print(evilmon3['name'] + " Hp: " + str(evilmon3['hp']))
            print("Suuppperr Sllliiiceee!")
            evilmon3['hp'] -= New_Charc['attack'] + 15
            print(evilmon3['name'] + " Hp: " + str(evilmon3['hp']))
            print("--------------------------------------------------------")
            f = open("Charcter.txt", "w")
            f.write(str(New_Charc))
            f.close()
            f = open("evilmon3.txt", "w")
            f.write(str(evilmon3))
            f.close()
            monattack()
        elif Skills == 'Triple Chop (15 MP)' and New_Charc['mp'] > 15:
            print(New_Charc['name'] + " MP:" + str(New_Charc['mp']))
            New_Charc['mp'] -= 15
            print(New_Charc['name'] + " MP:" + str(New_Charc['mp']))
            print("Tttrrrriiipppllleee Ccchhhhoooopppp!")
            print("First Chop!")
            evilmon3['hp'] -= New_Charc['attack'] - 15
            print(evilmon3['name'] + " Hp: " + str(evilmon3['hp']))
            print("Second Chop!")
            evilmon3['hp'] -= New_Charc['attack'] - 10
            print(evilmon3['name'] + " Hp: " + str(evilmon3['hp']))
            print("Last Chop!")
            evilmon3['hp'] -= New_Charc['attack'] - 5
            print(evilmon3['name'] + " Hp: " + str(evilmon3['hp']))
            print("--------------------------------------------------------")
            f = open("Charcter.txt", "w")
            f.write(str(New_Charc))
            f.close()
            f = open("evilmon3.txt", "w")
            f.write(str(evilmon3))
            f.close()
            monattack()
        elif Skills == 'Go Back':
            Fight3()
        else:
            print("Error")

    elif action == 'Skill' and New_Charc['job'] == 'Archer':
        questions = [
            inquirer.List('Skill',
                          message="Skills",
                          choices=['Poison Arrow (10 MP)', 'Charged Shot (15 MP)', 'Go Back'],
                          ),
        ]
        answers = inquirer.prompt(questions)
        Skills = answers.get('Skill')
        if Skills == 'Poison Arrow (10 MP)' and New_Charc['mp'] > 10:
            print(New_Charc['name'] + " Poison Arrow!")
            print(New_Charc['name'] + " MP:" + str(New_Charc['mp']))
            New_Charc['mp'] -= 10
            print(New_Charc['name'] + " MP:" + str(New_Charc['mp']))
            print(evilmon3['name'] + " Hp: " + str(evilmon3['hp']))
            evilmon3['hp'] -= New_Charc['attack'] - 10
            print(evilmon3['name'] + " Hp: " + str(evilmon3['hp']))
            print(evilmon3['name'] + " has been poisoned")
            print("--------------------------------------------------------")
            f = open("Charcter.txt", "w")
            f.write(str(New_Charc))
            f.close()
            f = open("evilmon3.txt", "w")
            f.write(str(evilmon3))
            f.close()
            monpoison()
        elif Skills == 'Charged Shot (15 MP)' and New_Charc['mp'] > 15:
            print(New_Charc['name'] + " MP:" + str(New_Charc['mp']))
            New_Charc['mp'] -= 15
            print(New_Charc['name'] + " MP:" + str(New_Charc['mp']))
            print("Chaaaaaaaaarged Shot!")
            print(New_Charc['name'] + "Has started to charge")
            print("--------------------------------------------------------")
            monattack()
            print("Chaaaaaaaaarged Shot!")
            print(evilmon3['name'] + " Hp: " + str(evilmon3['hp']))
            evilmon3['hp'] -= New_Charc['attack'] + 20
            print(evilmon3['name'] + " Hp: " + str(evilmon3['hp']))
            print("--------------------------------------------------------")
            f = open("Charcter.txt", "w")
            f.write(str(New_Charc))
            f.close()
            f = open("evilmon3.txt", "w")
            f.write(str(evilmon3))
            f.close()
            monattack()
        elif Skills == 'Go Back':
            Fight3()
        else:
            print("Error")


    elif action == 'Skill' and New_Charc['job'] == 'Mage':
        questions = [
            inquirer.List('Skill',
                          message="Skills",
                          choices=['Fireball (10 MP)', 'Ice Dragon (30 MP)', 'Go Back'],
                          ),
        ]
        answers = inquirer.prompt(questions)
        Skills = answers.get('Skill')
        if Skills == 'Fireball (10 MP)' and New_Charc['mp'] > 10:
            print(New_Charc['name'] + " Fireball!")
            print(New_Charc['name'] + " MP:" + str(New_Charc['mp']))
            New_Charc['mp'] -= 10
            print(New_Charc['name'] + " MP:" + str(New_Charc['mp']))
            print(evilmon3['name'] + " Hp: " + str(evilmon3['hp']))
            evilmon3['hp'] -= New_Charc['attack'] + 15
            print(evilmon3['name'] + " Hp: " + str(evilmon3['hp']))
            print("--------------------------------------------------------")
            f = open("Charcter.txt", "w")
            f.write(str(New_Charc))
            f.close()
            f = open("evilmon3.txt", "w")
            f.write(str(evilmon3))
            f.close()
            monattack()
        elif Skills == 'Ice Dragon (30 MP)' and New_Charc['mp'] > 30:
            print(New_Charc['name'] + " MP:" + str(New_Charc['mp']))
            New_Charc['mp'] -= 30
            print(New_Charc['name'] + " MP:" + str(New_Charc['mp']))
            print("Iccccceeeeee DDDDDDrrrrraggooonnn!")
            print(evilmon3['name'] + " Hp: " + str(evilmon3['hp']))
            evilmon3['hp'] -= New_Charc['attack'] + 30
            print(evilmon3['name'] + " Hp: " + str(evilmon3['hp']))
            print("--------------------------------------------------------")
            f = open("Charcter.txt", "w")
            f.write(str(New_Charc))
            f.close()
            f = open("evilmon3.txt", "w")
            f.write(str(evilmon3))
            f.close()
            monattack()
        elif Skills == 'Go Back':
            Fight3()
        else:
            print("Error")

    elif action == 'Potion':
        print(New_Charc['name'] +" Potion!")
        print(New_Charc['name'] + "Hp: " + str(New_Charc['hp']))
        print(New_Charc['name'] + "Mp: " + str(New_Charc['mp']))
        print("Drink")
        print("HP = +15")
        print("MP = +15")
        New_Charc['hp'] += 15
        New_Charc['mp'] += 15
        print(New_Charc['name'] + "Hp: " + str(New_Charc['hp']))
        print(New_Charc['name'] + "Mp: " + str(New_Charc['mp']))
        print("--------------------------------------------------------")
        f = open("Charcter.txt", "w")
        f.write(str(New_Charc))
        f.close()
        f = open("evilmon3.txt", "w")
        f.write(str(evilmon3))
        f.close()
        monattack()
    else:
        print("Error")

    if New_Charc['hp'] < 1:
        print("You lose...")
        lose()
    elif evilmon3['hp'] < 1:
        print("You won!")
        print(New_Charc['name'] +" Leveled up!")
        New_Charc['hp'] += 10
        New_Charc['mp'] += 25
        New_Charc['attack'] += 10
        New_Charc['defense'] += 10
        New_Charc['money'] += 50
        New_Charc['level'] += 1
        print("hp +10, mp +10, attack +10, defense +10, money +50, level +1.")
        f = open("Charcter.txt", "w")
        f.write(str(New_Charc))
        f.close()
        evilmon3['hp'] += 110
        evilmon3['attack'] += 15
        f = open("evilmon3.txt", "w")
        f.write(str(evilmon3))
        f.close()
        charcterStatsuser()
        print("")
        questions = [
            inquirer.List('Continue',
                          message="Continue?",
                          choices=['Yes', 'No'],
                          ),
        ]
        answers = inquirer.prompt(questions)
        action = answers.get('Continue')
        if action == 'Yes':
            Fight4()
        elif action == 'No':
            idle()


    else:
        typingPrint("The Battle Continues...")
        print("")
        Fight3()



def Fight2():
    f = open("evilmon2.txt")
    x = f.readline()
    evilmon2 = eval(x)
    f = open("Charcter.txt")
    x = f.readline()
    New_Charc = eval(x)

    def monattack():
        typingPrint(" ★ ★ ★ ★ ★ ")
        print(" ")
        print(evilmon2['name'] + " Attack!")
        print(New_Charc['name'] + " Hp: " + str(New_Charc['hp']))
        print("SLASHHH")
        New_Charc['hp'] -= evilmon2['attack']
        print(New_Charc['name'] + " Hp: " + str(New_Charc['hp']))
        print("--------------------------------------------------------")
        f = open("Charcter.txt", "w")
        f.write(str(New_Charc))
        f.close()
        f = open("evilmon2.txt", "w")
        f.write(str(evilmon2))
        f.close()
        cls()

    def monpoison():
        typingPrint(" ★ ★ ★ ★ ★ ")
        print(" ")
        print(evilmon2['name'] + " Attack!")
        print("Hp: " + str(New_Charc['hp']))
        print("SLASHHH")
        New_Charc['hp'] -= evilmon2['attack']
        print("Hp: " + str(New_Charc['hp']))
        print(evilmon2['name'] + " has been poisoned!")
        print(evilmon2['name'] + " HP:" + str(evilmon2['hp']))
        evilmon2['hp'] =- 15
        print(evilmon2['name'] + " HP:" + str(evilmon2['hp']))
        print("--------------------------------------------------------")
        f = open("Charcter.txt", "w")
        f.write(str(New_Charc))
        f.close()
        f = open("evilmon2.txt", "w")
        f.write(str(evilmon2))
        f.close()
        cls()

    print(New_Charc['name'] +" VS "+ evilmon2['name'])
    questions = [
        inquirer.List('Action',
                      message="What are you going to do?",
                      choices=['Attack', 'Defend','Skill', 'Potion'],
                      ),
    ]
    answers = inquirer.prompt(questions)
    action = answers.get('Action')

    if action == 'Attack':
        print(New_Charc['name'] +" Attack!")
        print(evilmon2['name'] + " Hp: " + str(evilmon2['hp']))
        print("SLASHHH")
        evilmon2['hp'] -= New_Charc['attack']
        print(evilmon2['name'] + " Hp: " + str(evilmon2['hp']))
        print("--------------------------------------------------------")
        f = open("Charcter.txt", "w")
        f.write(str(New_Charc))
        f.close()
        f = open("evilmon2.txt", "w")
        f.write(str(evilmon2))
        f.close()
        monattack()

    elif action == 'Defend':
        print(New_Charc['name'] +" Defend!")
        print("Defence is up")
        print(evilmon2['name'] +" Is about to attack")
        print(New_Charc['name'] + " Hp: " + str(New_Charc['hp']))
        print("SLASHHH")
        defence = evilmon2['attack'] - New_Charc['defense']
        New_Charc['hp'] -= defence
        print(New_Charc['name'] + " Hp: " + str(New_Charc['hp']))
        print("--------------------------------------------------------")
        f = open("Charcter.txt", "w")
        f.write(str(New_Charc))
        f.close()
        f = open("evilmon2.txt", "w")
        f.write(str(evilmon2))
        f.close()

    elif action == 'Skill' and New_Charc['job'] == 'Fighter':
        questions = [
            inquirer.List('Skill',
                          message="Skills",
                          choices=['Super Slice (10 MP)', 'Triple Chop (15 MP)', 'Go Back'],
                          ),
        ]
        answers = inquirer.prompt(questions)
        Skills = answers.get('Skill')
        if Skills == 'Super Slice (10 MP)' and New_Charc['mp'] > 10:
            print(New_Charc['name'] + " Super Slice!")
            print(New_Charc['name'] + " MP:" + str(New_Charc['mp']))
            print(New_Charc['name'] + " Gained Attack boost")
            New_Charc['mp'] -= 10
            print(New_Charc['name'] + " MP:" + str(New_Charc['mp']))
            print(evilmon2['name'] + " Hp: " + str(evilmon2['hp']))
            print("Suuppperr Sllliiiceee!")
            evilmon2['hp'] -= New_Charc['attack'] + 15
            print(evilmon2['name'] + " Hp: " + str(evilmon2['hp']))
            print("--------------------------------------------------------")
            f = open("Charcter.txt", "w")
            f.write(str(New_Charc))
            f.close()
            f = open("evilmon2.txt", "w")
            f.write(str(evilmon2))
            f.close()
            monattack()
        elif Skills == 'Triple Chop (15 MP)' and New_Charc['mp'] > 15:
            print(New_Charc['name'] + " MP:" + str(New_Charc['mp']))
            New_Charc['mp'] -= 15
            print(New_Charc['name'] + " MP:" + str(New_Charc['mp']))
            print("Tttrrrriiipppllleee Ccchhhhoooopppp!")
            print("First Chop!")
            evilmon2['hp'] -= New_Charc['attack'] - 15
            print(evilmon2['name'] + " Hp: " + str(evilmon2['hp']))
            print("Second Chop!")
            evilmon2['hp'] -= New_Charc['attack'] - 10
            print(evilmon2['name'] + " Hp: " + str(evilmon2['hp']))
            print("Last Chop!")
            evilmon2['hp'] -= New_Charc['attack'] - 5
            print(evilmon2['name'] + " Hp: " + str(evilmon2['hp']))
            print("--------------------------------------------------------")
            f = open("Charcter.txt", "w")
            f.write(str(New_Charc))
            f.close()
            f = open("evilmon2.txt", "w")
            f.write(str(evilmon2))
            f.close()
            monattack()
        elif Skills == 'Go Back':
            Fight2()
        else:
            print("Error")

    elif action == 'Skill' and New_Charc['job'] == 'Archer':
        questions = [
            inquirer.List('Skill',
                          message="Skills",
                          choices=['Poison Arrow (10 MP)', 'Charged Shot (15 MP)', 'Go Back'],
                          ),
        ]
        answers = inquirer.prompt(questions)
        Skills = answers.get('Skill')
        if Skills == 'Poison Arrow (10 MP)' and New_Charc['mp'] > 10:
            print(New_Charc['name'] + " Poison Arrow!")
            print(New_Charc['name'] + " MP:" + str(New_Charc['mp']))
            New_Charc['mp'] -= 10
            print(New_Charc['name'] + " MP:" + str(New_Charc['mp']))
            print(evilmon2['name'] + " Hp: " + str(evilmon2['hp']))
            evilmon2['hp'] -= New_Charc['attack'] - 10
            print(evilmon2['name'] + " Hp: " + str(evilmon2['hp']))
            print(evilmon2['name'] + " has been poisoned")
            print("--------------------------------------------------------")
            f = open("Charcter.txt", "w")
            f.write(str(New_Charc))
            f.close()
            f = open("evilmon2.txt", "w")
            f.write(str(evilmon2))
            f.close()
            monpoison()
        elif Skills == 'Charged Shot (15 MP)' and New_Charc['mp'] > 15:
            print(New_Charc['name'] + " MP:" + str(New_Charc['mp']))
            New_Charc['mp'] -= 15
            print(New_Charc['name'] + " MP:" + str(New_Charc['mp']))
            print("Chaaaaaaaaarged Shot!")
            print(New_Charc['name'] + "Has started to charge")
            print("--------------------------------------------------------")
            monattack()
            print("Chaaaaaaaaarged Shot!")
            print(evilmon2['name'] + " Hp: " + str(evilmon2['hp']))
            evilmon2['hp'] -= New_Charc['attack'] + 20
            print(evilmon2['name'] + " Hp: " + str(evilmon2['hp']))
            print("--------------------------------------------------------")
            f = open("Charcter.txt", "w")
            f.write(str(New_Charc))
            f.close()
            f = open("evilmon2.txt", "w")
            f.write(str(evilmon2))
            f.close()
            monattack()
        elif Skills == 'Go Back':
            Fight2()
        else:
            print("Error")


    elif action == 'Skill' and New_Charc['job'] == 'Mage':
        questions = [
            inquirer.List('Skill',
                          message="Skills",
                          choices=['Fireball (10 MP)', 'Ice Dragon (30 MP)', 'Go Back'],
                          ),
        ]
        answers = inquirer.prompt(questions)
        Skills = answers.get('Skill')
        if Skills == 'Fireball (10 MP)' and New_Charc['mp'] > 10:
            print(New_Charc['name'] + " Fireball!")
            print(New_Charc['name'] + " MP:" + str(New_Charc['mp']))
            New_Charc['mp'] -= 10
            print(New_Charc['name'] + " MP:" + str(New_Charc['mp']))
            print(evilmon2['name'] + " Hp: " + str(evilmon2['hp']))
            evilmon2['hp'] -= New_Charc['attack'] + 15
            print(evilmon2['name'] + " Hp: " + str(evilmon2['hp']))
            print("--------------------------------------------------------")
            f = open("Charcter.txt", "w")
            f.write(str(New_Charc))
            f.close()
            f = open("evilmon2.txt", "w")
            f.write(str(evilmon2))
            f.close()
            monattack()
        elif Skills == 'Ice Dragon (30 MP)' and New_Charc['mp'] > 30:
            print(New_Charc['name'] + " MP:" + str(New_Charc['mp']))
            New_Charc['mp'] -= 30
            print(New_Charc['name'] + " MP:" + str(New_Charc['mp']))
            print("Iccccceeeeee DDDDDDrrrrraggooonnn!")
            print(evilmon2['name'] + " Hp: " + str(evilmon2['hp']))
            evilmon2['hp'] -= New_Charc['attack'] + 30
            print(evilmon2['name'] + " Hp: " + str(evilmon2['hp']))
            print("--------------------------------------------------------")
            f = open("Charcter.txt", "w")
            f.write(str(New_Charc))
            f.close()
            f = open("evilmon2.txt", "w")
            f.write(str(evilmon2))
            f.close()
            monattack()
        elif Skills == 'Go Back':
            Fight2()
        else:
            print("Error")

    elif action == 'Potion':
        print(New_Charc['name'] +" Potion!")
        print(New_Charc['name'] + "Hp: " + str(New_Charc['hp']))
        print(New_Charc['name'] + "Mp: " + str(New_Charc['mp']))
        print("Drink")
        print("HP = +15")
        print("MP = +15")
        New_Charc['hp'] += 15
        New_Charc['mp'] += 15
        print(New_Charc['name'] + "Hp: " + str(New_Charc['hp']))
        print(New_Charc['name'] + "Mp: " + str(New_Charc['mp']))
        print("--------------------------------------------------------")
        f = open("Charcter.txt", "w")
        f.write(str(New_Charc))
        f.close()
        f = open("evilmon2.txt", "w")
        f.write(str(evilmon2))
        f.close()
        monattack()
    else:
        print("Error")

    if New_Charc['hp'] < 1:
        print("You lose...")
        lose()
    elif evilmon2['hp'] < 1:
        print("You won!")
        print(New_Charc['name'] +" Leveled up!")
        New_Charc['hp'] += 10
        New_Charc['mp'] += 25
        New_Charc['attack'] += 10
        New_Charc['defense'] += 10
        New_Charc['money'] += 50
        New_Charc['level'] += 1
        print("hp +10, mp +10, attack +10, defense +10, money +50, level +1.")
        f = open("Charcter.txt", "w")
        f.write(str(New_Charc))
        f.close()
        evilmon2['hp'] += 100
        evilmon2['attack'] += 10
        f = open("evilmon2.txt", "w")
        f.write(str(evilmon2))
        f.close()
        charcterStatsuser()
        print("")
        questions = [
            inquirer.List('Continue',
                          message="Continue?",
                          choices=['Yes', 'No'],
                          ),
        ]
        answers = inquirer.prompt(questions)
        action = answers.get('Continue')
        if action == 'Yes':
            Fight3()
        elif action == 'No':
            idle()


    else:
        typingPrint("The Battle Continues...")
        print("")
        Fight2()


def Fight():
    f = open("evilmon.txt")
    x = f.readline()
    evilmon = eval(x)
    f = open("Charcter.txt")
    x = f.readline()
    New_Charc = eval(x)

    def monattack():
        typingPrint(" ★ ★ ★ ★ ★ ")
        print(" ")
        print(evilmon['name'] + " Attack!")
        print(New_Charc['name'] + " Hp: " + str(New_Charc['hp']))
        print("SLASHHH")
        New_Charc['hp'] -= evilmon['attack']
        print(New_Charc['name'] + " Hp: " + str(New_Charc['hp']))
        print("--------------------------------------------------------")
        f = open("Charcter.txt", "w")
        f.write(str(New_Charc))
        f.close()
        f = open("evilmon.txt", "w")
        f.write(str(evilmon))
        f.close()
        cls()

    def monpoison():
        typingPrint(" ★ ★ ★ ★ ★ ")
        print(" ")
        print(evilmon['name'] + " Attack!")
        print("Hp: " + str(New_Charc['hp']))
        print("SLASHHH")
        New_Charc['hp'] -= evilmon['attack']
        print("Hp: " + str(New_Charc['hp']))
        print(evilmon['name'] + " has been poisoned!")
        print(evilmon['name'] + " HP:" + str(evilmon['hp']))
        evilmon['hp'] =- 15
        print(evilmon['name'] + " HP:" + str(evilmon['hp']))
        print("--------------------------------------------------------")
        f = open("Charcter.txt", "w")
        f.write(str(New_Charc))
        f.close()
        f = open("evilmon.txt", "w")
        f.write(str(evilmon))
        f.close()
        cls()

    print(New_Charc['name'] +" VS "+ evilmon['name'])
    questions = [
        inquirer.List('Action',
                      message="What are you going to do?",
                      choices=['Attack', 'Defend','Skill', 'Potion'],
                      ),
    ]
    answers = inquirer.prompt(questions)
    action = answers.get('Action')

    if action == 'Attack':
        print(New_Charc['name'] +" Attack!")
        print(evilmon['name'] + " Hp: " + str(evilmon['hp']))
        print("SLASHHH")
        evilmon['hp'] -= New_Charc['attack']
        print(evilmon['name'] + " Hp: " + str(evilmon['hp']))
        print("--------------------------------------------------------")
        f = open("Charcter.txt", "w")
        f.write(str(New_Charc))
        f.close()
        f = open("evilmon.txt", "w")
        f.write(str(evilmon))
        f.close()
        monattack()

    elif action == 'Defend':
        print(New_Charc['name'] +" Defend!")
        print("Defence is up")
        print(evilmon['name'] +" Is about to attack")
        print(New_Charc['name'] + " Hp: " + str(New_Charc['hp']))
        print("SLASHHH")
        defence = evilmon['attack'] - New_Charc['defense']
        New_Charc['hp'] -= defence
        print(New_Charc['name'] + " Hp: " + str(New_Charc['hp']))
        print("--------------------------------------------------------")
        f = open("Charcter.txt", "w")
        f.write(str(New_Charc))
        f.close()
        f = open("evilmon.txt", "w")
        f.write(str(evilmon))
        f.close()

    elif action == 'Skill' and New_Charc['job'] == 'Fighter':
        questions = [
            inquirer.List('Skill',
                          message="Skills",
                          choices=['Super Slice (10 MP)', 'Triple Chop (15 MP)', 'Go Back'],
                          ),
        ]
        answers = inquirer.prompt(questions)
        Skills = answers.get('Skill')
        if Skills == 'Super Slice (10 MP)' and New_Charc['mp'] > 10:
            print(New_Charc['name'] + " Super Slice!")
            print(New_Charc['name'] + " MP:" + str(New_Charc['mp']))
            print(New_Charc['name'] + " Gained Attack boost")
            New_Charc['mp'] -= 10
            print(New_Charc['name'] + " MP:" + str(New_Charc['mp']))
            print(evilmon['name'] + " Hp: " + str(evilmon['hp']))
            print("Suuppperr Sllliiiceee!")
            evilmon['hp'] -= New_Charc['attack'] + 15
            print(evilmon['name'] + " Hp: " + str(evilmon['hp']))
            print("--------------------------------------------------------")
            f = open("Charcter.txt", "w")
            f.write(str(New_Charc))
            f.close()
            f = open("evilmon.txt", "w")
            f.write(str(evilmon))
            f.close()
            monattack()
        elif Skills == 'Triple Chop (15 MP)' and New_Charc['mp'] > 15:
            print(New_Charc['name'] + " MP:" + str(New_Charc['mp']))
            New_Charc['mp'] -= 15
            print(New_Charc['name'] + " MP:" + str(New_Charc['mp']))
            print("Tttrrrriiipppllleee Ccchhhhoooopppp!")
            print("First Chop!")
            evilmon['hp'] -= New_Charc['attack'] - 15
            print(evilmon['name'] + " Hp: " + str(evilmon['hp']))
            print("Second Chop!")
            evilmon['hp'] -= New_Charc['attack'] - 10
            print(evilmon['name'] + " Hp: " + str(evilmon['hp']))
            print("Last Chop!")
            evilmon['hp'] -= New_Charc['attack'] - 5
            print(evilmon['name'] + " Hp: " + str(evilmon['hp']))
            print("--------------------------------------------------------")
            f = open("Charcter.txt", "w")
            f.write(str(New_Charc))
            f.close()
            f = open("evilmon.txt", "w")
            f.write(str(evilmon))
            f.close()
            monattack()
        elif Skills == 'Go Back':
            Fight()
        else:
            print("Error")

    elif action == 'Skill' and New_Charc['job'] == 'Archer':
        questions = [
            inquirer.List('Skill',
                          message="Skills",
                          choices=['Poison Arrow (10 MP)', 'Charged Shot (15 MP)', 'Go Back'],
                          ),
        ]
        answers = inquirer.prompt(questions)
        Skills = answers.get('Skill')
        if Skills == 'Poison Arrow (10 MP)' and New_Charc['mp'] > 10:
            print(New_Charc['name'] + " Poison Arrow!")
            print(New_Charc['name'] + " MP:" + str(New_Charc['mp']))
            New_Charc['mp'] -= 10
            print(New_Charc['name'] + " MP:" + str(New_Charc['mp']))
            print(evilmon['name'] + " Hp: " + str(evilmon['hp']))
            evilmon['hp'] -= New_Charc['attack'] - 10
            print(evilmon['name'] + " Hp: " + str(evilmon['hp']))
            print(evilmon['name'] + " has been poisoned")
            print("--------------------------------------------------------")
            f = open("Charcter.txt", "w")
            f.write(str(New_Charc))
            f.close()
            f = open("evilmon.txt", "w")
            f.write(str(evilmon))
            f.close()
            monpoison()
        elif Skills == 'Charged Shot (15 MP)' and New_Charc['mp'] > 15:
            print(New_Charc['name'] + " MP:" + str(New_Charc['mp']))
            New_Charc['mp'] -= 15
            print(New_Charc['name'] + " MP:" + str(New_Charc['mp']))
            print("Chaaaaaaaaarged Shot!")
            print(New_Charc['name'] + "Has started to charge")
            print("--------------------------------------------------------")
            monattack()
            print("Chaaaaaaaaarged Shot!")
            print(evilmon['name'] + " Hp: " + str(evilmon['hp']))
            evilmon['hp'] -= New_Charc['attack'] + 20
            print(evilmon['name'] + " Hp: " + str(evilmon['hp']))
            print("--------------------------------------------------------")
            f = open("Charcter.txt", "w")
            f.write(str(New_Charc))
            f.close()
            f = open("evilmon.txt", "w")
            f.write(str(evilmon))
            f.close()
            monattack()
        elif Skills == 'Go Back':
            Fight()
        else:
            print("Error")


    elif action == 'Skill' and New_Charc['job'] == 'Mage':
        questions = [
            inquirer.List('Skill',
                          message="Skills",
                          choices=['Fireball (10 MP)', 'Ice Dragon (30 MP)', 'Go Back'],
                          ),
        ]
        answers = inquirer.prompt(questions)
        Skills = answers.get('Skill')
        if Skills == 'Fireball (10 MP)' and New_Charc['mp'] > 10:
            print(New_Charc['name'] + " Fireball!")
            print(New_Charc['name'] + " MP:" + str(New_Charc['mp']))
            New_Charc['mp'] -= 10
            print(New_Charc['name'] + " MP:" + str(New_Charc['mp']))
            print(evilmon['name'] + " Hp: " + str(evilmon['hp']))
            evilmon['hp'] -= New_Charc['attack'] + 15
            print(evilmon['name'] + " Hp: " + str(evilmon['hp']))
            print("--------------------------------------------------------")
            f = open("Charcter.txt", "w")
            f.write(str(New_Charc))
            f.close()
            f = open("evilmon.txt", "w")
            f.write(str(evilmon))
            f.close()
            monattack()
        elif Skills == 'Ice Dragon (30 MP)' and New_Charc['mp'] > 30:
            print(New_Charc['name'] + " MP:" + str(New_Charc['mp']))
            New_Charc['mp'] -= 30
            print(New_Charc['name'] + " MP:" + str(New_Charc['mp']))
            print("Iccccceeeeee DDDDDDrrrrraggooonnn!")
            print(evilmon['name'] + " Hp: " + str(evilmon['hp']))
            evilmon['hp'] -= New_Charc['attack'] + 30
            print(evilmon['name'] + " Hp: " + str(evilmon['hp']))
            print("--------------------------------------------------------")
            f = open("Charcter.txt", "w")
            f.write(str(New_Charc))
            f.close()
            f = open("evilmon.txt", "w")
            f.write(str(evilmon))
            f.close()
            monattack()
        elif Skills == 'Go Back':
            Fight()
        else:
            print("Error")

    elif action == 'Potion':
        print(New_Charc['name'] +" Potion!")
        print(New_Charc['name'] + "Hp: " + str(New_Charc['hp']))
        print(New_Charc['name'] + "Mp: " + str(New_Charc['mp']))
        print("Drink")
        print("HP = +15")
        print("MP = +15")
        New_Charc['hp'] += 15
        New_Charc['mp'] += 15
        print(New_Charc['name'] + "Hp: " + str(New_Charc['hp']))
        print(New_Charc['name'] + "Mp: " + str(New_Charc['mp']))
        print("--------------------------------------------------------")
        f = open("Charcter.txt", "w")
        f.write(str(New_Charc))
        f.close()
        f = open("evilmon.txt", "w")
        f.write(str(evilmon))
        f.close()
        monattack()
    else:
        print("Error")

    if New_Charc['hp'] < 1:
        print("You lose...")
        lose()
    elif evilmon['hp'] < 1:
        print("You won!")
        print(New_Charc['name'] +" Leveled up!")
        New_Charc['hp'] += 10
        New_Charc['mp'] += 25
        New_Charc['attack'] += 10
        New_Charc['defense'] += 10
        New_Charc['money'] += 50
        New_Charc['level'] += 1
        print("hp +10, mp +10, attack +10, defense +10, money +50, level +1.")
        f = open("Charcter.txt", "w")
        f.write(str(New_Charc))
        f.close()
        evilmon['hp'] += 100
        evilmon['attack'] += 10
        f = open("evilmon.txt", "w")
        f.write(str(evilmon))
        f.close()
        charcterStatsuser()
        print("")
        questions = [
            inquirer.List('Continue',
                          message="Continue?",
                          choices=['Yes', 'No'],
                          ),
        ]
        answers = inquirer.prompt(questions)
        action = answers.get('Continue')
        if action == 'Yes':
            Fight2()
        elif action == 'No':
            idle()


    else:
        typingPrint("The Battle Continues...")
        print("")
        Fight()


welcome()
# Evilmon()
# Fight()


