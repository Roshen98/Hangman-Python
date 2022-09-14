import random

categoryList = ['fruit','food','sport','app','python']

fruit = ['Cherry','Banana','Apple','Orange', 'Grape','Peach','Tangerine',
'Lemon','Tomato','Watermelon','Melon','Kiwi','Mango','Pineapple','Avacado',
'Star Fruit', 'Lychee','Strawberry','Blackberry','Blueberry','Rasberry',
'Grapefruit', 'Plum','Dragonfruit','Pomegranate',
'Lime','Apricot','Papaya','Coconut','Guava','Cranberry','Passion Fruit']


food = ['Pizza','Hamburger','Beef','Chicken Wing','Lamb','BBQ',
'Taco','French Fries','Chicken Nuggets','Cup Noodle AKA ramen',
'Dumpling','Sushi','Sashimi','Pork Chop','Egg','Bacon',
'Turkey','Mashed Potato','Fried Rice','Salmon','Fish',
'Pancake','Spaghetti','Waffle','Pasta','Salad','Bread',
'Cheese','Donut','Cookie','Muffins']

sport = ['Football','Basketball','Soccer','Ping Pong AKA table tennis','Badminton',
'Tennis', 'Ice Hockey','Baseball','Golf','Swimming','Fishing',
'Volleyball','Boxing','Bowling','Skateboard','Biking',
'Running','Jump Roping','Marathon','Cricket','Shooting','Archery',
'Boating','Hiking','Rock Climbing','Skiing','Roller Skating',
'Surfing','Horse Racing','Karate','Kong Fu']

app = ['Roblox','Minecraft','YouTube','App Store','Mblock',
'Zoom','Setting','Pokemon Go','Tiktok','Crossy Road','We Chat',
'FaceBook','Among Us','Angry Bird','Survior.io','Plants vs Zombies 2',
'Wordscape','Fruit Ninja','Super Mario Run','Tetris','Candy Crush',
'Netflix','DisneyPlus','Temple Run','Pac Man','Google Chrome',
'Calculator','Clock','Duolingo','Monopoly','Uber','UberEats','DoorDash',
'Dragon City','Rage Shadow Legend','WildRift','Monster Legends',
'Mobile Legend','Uno','Starbucks','Genshin Impact','Popeyes',
'Dragon Ball Legend','Lyft','Google Map','Venmo','Spotify','Photos',
'Discord','Pokemon United','Instalgram','Safari','Mc Donald','KFC']

python = ['coding','typing','print','return','if','else','elif',
'and','or','comma','parenthesis','def','colon','characters','data type',
'strings','equal','list','array','integer','float','boolean','true',
'false','while true','import','__init__','self','value error','try',
'except','input','name error','continue','for loop','concatenation',
'super','parameter','variables','programming langugage','class',
'function','method','recursion']

def welcomeMessage():
    # beginning messages
    numbering = 1
    print('Hello, welcome to Hangeman')
    print('Choose a category:')
    for each_type in categoryList:
        print(str(numbering) + '. ' + each_type)  # string concatenation
        numbering+=1    # increment
    
   
def dead():
    print('''
                -------|
                |      |
                |      |       
                o      |
               /|\     |
               / \     |
                       |
                       |
                       |
                       |
                       |
            ___________|
    ''')
    
def emptyPole():
    print('''
                -------|
                |      |
                |      |       
                       |
                       |
                       |
                       |
                       |
                       |
                       |
                       |
            ___________|
    ''')
    
def headPole():
    print('''
                -------|
                |      |
                |      |       
                o      |
                       |
                       |
                       |
                       |
                       |
                       |
                       |
            ___________|
    ''')
    
def bodyPole():
    print('''
                -------|
                |      |
                |      |       
                o      |
                |      |
                       |
                       |
                       |
                       |
                       |
                       |
            ___________|
    ''')
    
def leftArmPole():
    print('''
                -------|
                |      |
                |      |       
                o      |
               /|      |
                       |
                       |
                       |
                       |
                       |
                       |
            ___________|
    ''')
    
def rightArmPole():
    print('''
                -------|
                |      |
                |      |       
                o      |
               /|\     |
                       |
                       |
                       |
                       |
                       |
                       |
            ___________|
    ''')
    
def leftLegPole():
    
    print('''
                -------|
                |      |
                |      |       
                o      |
               /|\     |
               /       |
                       |
                       |
                       |
                       |
                       |
            ___________|
    ''')

def getCategory(category):
    # recursive function that returns the category the user chooses
    for each_option in range(1,6):
        if category == str(each_option):
            return category
            
    category = input('Option: ')
    return getCategory(category)

def getCategoryList(category):
    # returns the respective category list given the category number chosen
    categoryIndex = int(category) - 1
    
    if(categoryList[categoryIndex] == 'fruit'):
        return fruit
    
    elif(categoryList[categoryIndex] == 'food'):
        return food
    
    elif(categoryList[categoryIndex] == 'sport'):
        return sport
    
    elif(categoryList[categoryIndex] == 'app'):
        return app
        
    else:
        return python

def blankSpacesDisplay(updatedWord):
    # prints the letters based on what the user chooses
    for each_letter in updatedWord:
        print(each_letter, end = ' ')
    
def randomWord(category_list):
    # returns the random word in the chosen category list
    sizeOfList = len(category_list)
    randomIndex =  random.randint(0, sizeOfList - 1)
    return category_list[randomIndex]
    
def pickLetter(letterList):
    # ask the user to pick a letter and check if the letter is repeated or not
    while True:
        chosenLetter = input('\nPick a letter: ')
        if chosenLetter not in letterList:
            letterList.append(chosenLetter)
            return letterList
        else:
            print('Letter already picked! Please try another one!')
        
    
def play(category):
    # start the game
    letterList = []
    life = 6
    updatedWord = ""
    sameWord = ""
    print(category)
    category_list = getCategoryList(category)
    emptyPole()
    word = randomWord(category_list)
    updatedWord += "_"*len(word)
    
    while True:
        blankSpacesDisplay(updatedWord)
        letterList = pickLetter(letterList)
        chosenLetter = letterList[len(letterList)-1]
        sameWord = updatedWord
        updatedWord = checkLetter(chosenLetter,word,updatedWord)
        if updatedWord == word:
            print('Congratulations! The word is:', word)
            return 
        if updatedWord == sameWord:
            life -= 1
        showPole(life)
        if life == 0:
            print('Game Over! You Lost!')
            break
        
def showPole(lives):
    if lives == 6:
        emptyPole()
        
    elif lives == 5:
        headPole()
    
    elif lives == 4:
        bodyPole()
        
    elif lives == 3:
        leftArmPole()

    elif lives == 2:
        rightArmPole()

    elif lives == 1:
        leftLegPole()

    else:
        dead()
    
def checkLetter(chosenLetter,word,updatedWord):
    # return the updated word with the chosen letters
    lowerCaseLetter = chosenLetter.lower()
    upperCaseLetter = chosenLetter.upper()
    while True:
        if lowerCaseLetter in word:
            index = word.index(lowerCaseLetter)
            word = word.replace(lowerCaseLetter,'_',1)
            updatedWord = assignLetter(index,lowerCaseLetter,updatedWord)
            if lowerCaseLetter in word:
                updatedWord = assignLetter(index,lowerCaseLetter,updatedWord)
            else:
                return assignLetter(index,lowerCaseLetter,updatedWord)
            
        elif upperCaseLetter in word:
            index = word.index(upperCaseLetter)
            word = word.replace(upperCaseLetter,'_',1)
            if upperCaseLetter in word:
                updatedWord = assignLetter(index,upperCaseLetter,updatedWord)
            else:
                return assignLetter(index,upperCaseLetter,updatedWord)
                
        else:
            return updatedWord

def assignLetter(index,chosenLetter,updatedWord):
    # returns the updated word based on the letter index
    newWord = ""
    wordIndex = 0
    for each in updatedWord :
        if(wordIndex == index):
            newWord += chosenLetter
            
        else:
            newWord += each
            
        wordIndex += 1
        
    return newWord
            
def menu():
    # platform for the menu options
    category = None
    welcomeMessage()
    category = getCategory(category)
    play(category)

if __name__ == '__main__':
    # main function
    menu()















