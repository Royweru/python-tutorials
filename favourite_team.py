import json

def get_favourite_team () :
    filename = 'textfiles/favorite_team.json'
    try :
        with open(filename) as f:
            favorite_team = json.load(f)
    except FileNotFoundError :
        favorite_team= input("What is your favorite team ? ")
        with open(filename,'w',encoding='utf-8') as f :
            json.dump(favorite_team,f)
            print (f"We will be sure to remember your favorite team, {favorite_team}")
    else :
        print(f"Guess what we know your favorite team , it is {favorite_team}")

get_favourite_team()