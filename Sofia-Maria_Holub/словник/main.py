football_players = {
    'Messi': {'team': 'Barcelona', 'position': 'forward', 'goals': 700},
    'Ronaldo': {'team': 'Manchester United', 'position': 'forward', 'goals': 680},
    'Neymar': {'team': 'Paris Saint-Germain', 'position': 'forward', 'goals': 150}
}

def display_players():
    print("Footballers:")
    for player, info in football_players.items():
        print(f"{player}: {info}")


def add_player(name, team, position, goals):
    football_players[name] = {'team': team, 'position': position, 'goals': goals}
    print(f"{name} added.")

def remove_player(name):
    if name in football_players:
        del football_players[name]
        print(f"{name} removed.")
    else:
        print(f"{name} not in list.")

def update_player(name, team=None, position=None, goals=None):
    if name in football_players:
        player = football_players[name]
        if team is not None:
            player['team'] = team
        if position is not None:
            player['position'] = position
        if goals is not None:
            player['goals'] = goals
        print(f"Info about  {name} updated.")
    else:
        print(f"{name} not in list.")

display_players()

add_player('Mbappe', 'Paris Saint-Germain', 'forward', 120)
#display_players()

remove_player('Neymar')
#display_players()

update_player('Messi', goals=710)
display_players()
