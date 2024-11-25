users: list = [
    {'name': 'Dominik', 'posts': 1, 'city': 'Warszawa'},
    {'name': 'Dominik', 'posts': 3, 'city': 'Katowice'},
    {'name': 'Szymon z wąsem', 'posts': 5, 'city': 'Siemiatycze'},
    {'name': 'Szymon', 'posts': 7, 'city': 'Kielce'},
    {'name': 'Patryk', 'posts': 9, 'city': 'Łódź'},

]
print(f'Witaj {users[0]['name']}!!')

for user in users[1:]:
    print(f'Twój znajomy  {user['name']},z miasta {user['city']} opublikował {user['posts']} postów')
# for idx, _ in enumerate(users[0:]):
#     print(f'Twój znajony {users[idx]}, opublikował {postow[idx]} postów')
