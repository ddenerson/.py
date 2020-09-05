from random import choice

user_info = dict(name= "Denerson",notes=["10","20","30"],date="09/04/2020")
print(user_info["name"])

print("################################################") 

artist = dict(first="Neil",last="Young")

full_name = artist["first"] + " " + artist["last"]
print(full_name)

print("################################################")

donations = dict(sam=25.0,lena=88.99,chuck=13.0,linus=99.5,stan=150.0,lisa=50.25,harrison=10.0)
total_donations = 0;


for key,value in donations.items():
   print(key,value)

print("################################################")

for value in donations.values():
    print(value)
   
print("################################################")

for v in donations.values():
    total_donations += v;
print(total_donations)    
    
print("################################################")

food = choice(["cheese pizza", "quiche","morning bun","gummy bear","tea cake"])

bakery_stock = {
    "almond croissant" : 12,
    "toffee cookie": 3,
    "morning bun": 1,
    "chocolate chunk cookie": 9,
    "tea cake": 25
}

value = bakery_stock.get(food)

if value:
    print("{} - {}" .format(value,food))
else:
    print("We don't make that")

print("################################################")

game_properties = ["current_score", "high_score", "number_of_lives", "items_in_inventory", "power_ups", "ammo", "enemies_on_screen", "enemy_kills", "enemy_kill_streaks", "minutes_played", "notifications", "achievements"]
v = 0

initial_game_state = dict.fromkeys(game_properties,v)

print(initial_game_state)

print("################################################")

inventory = {'croissant': 19, 'bagel': 4, 'muffin': 8, 'cake': 1}

stock_list = inventory.copy()
stock_list.update({'cookie':18})

print(stock_list)

stock_list.pop('cake')
print(stock_list)

print("################################################")

total_lenght = 0


playlist = {
    'title' : 'patagonia bus',
    'author' : 'colt steele',
    'songs' :[{'title': 'song1', 'artist': ['blue'], 'duration': 2.5},
              {'title': 'song2','artist' : ['Kitty','djcat'], 'duration':5.25},
              {'title': 'meowmeow','artist': ['garfield'],'duration':2.0}]
}

for song in playlist['songs']:
    total_lenght += song['duration']

print(total_lenght)


print("################################################")










