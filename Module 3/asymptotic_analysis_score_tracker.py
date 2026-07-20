player_names = ["Aarav", "Priya", "Dev", "Meera", "Kabir"]
player_scores = [90, 75, 88, 62, 95]

total_players = len(player_scores)

print("=== Score Tracker (n =", total_players, "players) ===")

for index in range(total_players):
    print(index + 1, ". ", player_names[index],
          " : ", player_scores[index], sep="")

print()

step_count = 1

print("Score at index 0 :",
      player_scores[0], "| steps =", step_count, "| Theta(1) - tight bound")
print()

search_name = "Aarav"
step_count = 0

for current_name in player_names:
    step_count += 1
    if current_name == search_name:
        break

print("Search for", search_name, "| steps =",
      step_count, "| Omega(1) - best case lower bound")

search_name = "Kabir"
step_count = 0

for current_name in player_names:
    step_count += 1
    if current_name == search_name:
        break

print("Search for", search_name, "| steps =", step_count,
      "| O(n) =", total_players, "- worst case upper bound")
print()

comparison_steps = 0
required_total = 150

print("Pairs with total score =", required_total, ":")

for first_player in range(total_players):
    for second_player in range(first_player + 1, total_players):
        comparison_steps += 1
        if player_scores[first_player] + player_scores[second_player] == required_total:
            print(" ", player_names[first_player], "+", player_names[second_player],
                  "=", player_scores[first_player] + player_scores[second_player])

print("Total comparisons :", comparison_steps,
      "| O(n²) - drop constants, keep n²")
print()

print("=== Asymptotic Summary ===")
print("Theta(1) : index access - always 1 step, tight bound")
print("Omega(1) : best case    - found in 1 step, lower bound")
print("O(n)     : worst case   - found after n =",
      total_players, "steps, upper bound")
print("O(n²)    : pair check   - n*(n-1)/2 =",
      total_players * (total_players - 1) // 2, "comparisons")
print()
print("Drop constants. Keep the dominant term. That is asymptotic analysis!")
