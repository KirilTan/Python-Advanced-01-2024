def team_lineup(*football_players: tuple):
    # Organizing players by their countries
    football_players_sorted_by_country = {}
    for player_name, player_country in football_players:
        if player_country not in football_players_sorted_by_country:
            football_players_sorted_by_country[player_country] = [player_name]
        else:
            football_players_sorted_by_country[player_country].append(player_name)

    # Sorting the dictionary by the number of players per country (descending) and then country name (alphabetically)
    sorted_countries = sorted(football_players_sorted_by_country.items(), key=lambda x: (-len(x[1]), x[0]))

    # Formatting and returning the sorted information
    result = []
    for country, players in sorted_countries:
        result.append(f'{country}:')
        for player in players:
            result.append(f'  -{player}')

    return '\n'.join(result)


# Test the function with your given calls
print(team_lineup(
   ("Harry Kane", "England"),
   ("Manuel Neuer", "Germany"),
   ("Raheem Sterling", "England"),
   ("Toni Kroos", "Germany"),
   ("Cristiano Ronaldo", "Portugal"),
   ("Thomas Muller", "Germany")))

print()

print(team_lineup(
   ("Lionel Messi", "Argentina"),
   ("Neymar", "Brazil"),
   ("Cristiano Ronaldo", "Portugal"),
   ("Harry Kane", "England"),
   ("Kylian Mbappe", "France"),
   ("Raheem Sterling", "England")))

print()

print(team_lineup(
   ("Harry Kane", "England"),
   ("Manuel Neuer", "Germany"),
   ("Raheem Sterling", "England"),
   ("Toni Kroos", "Germany"),
   ("Cristiano Ronaldo", "Portugal"),
   ("Thomas Muller", "Germany"),
   ("Bruno Fernandes", "Portugal"),
   ("Bernardo Silva", "Portugal"),
   ("Harry Maguire", "England")))
