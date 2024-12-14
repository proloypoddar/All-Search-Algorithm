
# #PART 1



# import random

# def alpha_beta(node, depth, alpha, beta, max_play):
#     if depth == 0 or isinstance(node, int): 
#         return node

#     if max_play:
#         max_evo = float('-inf')
#         for child in node:

#             eval = alpha_beta(child, depth - 1, alpha, beta, False)

#             max_evo = max(max_evo, eval)
#             alpha = max(alpha, eval)
#             if beta <= alpha:
#                 break  
#         return max_evo

#     else: 
#         min_evo = float('inf')
#         for child in node:

#             eval = alpha_beta(child, depth - 1, alpha, beta, True)
            
#             min_evo = min(min_evo, eval)
#             beta = min(beta, eval)
#             if beta <= alpha:
#                 break  
#         return min_evo

# def simu_game(player):

#     round_rslt = []
#     depth = 5 
#     t_round = 3
#     curr_player = player  

#     for i in range(1, t_round + 1):
       
#         tree_game = [random.choice([-1, 1]) for _ in range(2 ** depth)]

#         tree_str = game_tree(tree_game, depth)

        
#         winner = alpha_beta(tree_str, depth, float('-inf'), float('inf'), curr_player == 1)
#         round_winner = "Sub-Zero" if winner == 1 else "Scorpion"
#         round_rslt.append(round_winner)

        
#         curr_player = 1 - curr_player

#     scorpion_wins = round_rslt.count("Scorpion")

#     sub_zero_wins = round_rslt.count("Sub-Zero")

#     game_winner = "Scorpion" if scorpion_wins > sub_zero_wins else "Sub-Zero"

#     return game_winner, t_round, round_rslt

# def game_tree(leaf_data, depth):

#     while depth > 1:
#         leaf_data = [leaf_data[i:i + 2] for i in range(0, len(leaf_data), 2)]
#         depth -= 1
#     return leaf_data

# def mortal_kombat():
#     try:
#         player = int(input("Enter the sing player (0 for Scorpion, 1 for Sub-Zero): "))
#         if player not in [0, 1]:

#             raise ValueError("Invalid input! Enter 0 for Scorpion or 1 for Sub-Zero.")
#     except ValueError as e:
#         print(e)
#         return

#     game_winner, t_round, round_rslt = simu_game(player)

#     print(f"\nGame Winner: {game_winner}")

#     print(f"Total Rounds Played: {t_round}")

#     for i, winner in enumerate(round_rslt, s=1):
#         print(f"Winner of Round {i}: {winner}")

# mortal_kombat()
# 



#######################################################################################################





# # #PART 2


# def pacman_game(c):

#     leaf_data = [3, 6, 2, 3, 7, 1, 2, 0]

    
#     def mini_max(s, end, max_chk):

#         if s == end:  
            
#             return leaf_data[s]
#         mid = (s + end) // 2

#         if max_chk:

#             return max(mini_max(s, mid, False), mini_max(mid + 1, end, False))
#         else:
#             return min(mini_max(s, mid, True), mini_max(mid + 1, end, True))

#     no_magic_value = mini_max(0, len(leaf_data) - 1, True)

#     left_max = max(leaf_data[:4]) - c

#     right_max = max(leaf_data[4:]) - c

#     magic_value = max(left_max, right_max)

#     if magic_value > no_magic_value:

#         direction = "left" if left_max > right_max else "right"

#         print(f"The new mini_max value is {magic_value}. Pacman goes {direction} and uses dark magic.")

#     else:
#         print(f"The mini_max value is {no_magic_value}. Pacman does not use dark magic.")



#     def alpha_beta(s, end, alpha, beta, max_chk):
#         if s == end: 
#             return leaf_data[s]
#         mid = (s + end) // 2

#         if max_chk:

#             value = float('-inf')
#             value = max(value, alpha_beta(s, mid, alpha, beta, False))

#             alpha = max(alpha, value)
#             if alpha >= beta:

#                 return value
            
#             value = max(value, alpha_beta(mid + 1, end, alpha, beta, False))
#             return value
#         else:
#             value = float('inf')

#             value = min(value, alpha_beta(s, mid, alpha, beta, True))


#             beta = min(beta, value)

#             if alpha >= beta:

#                 return value
            
#             value = min(value, alpha_beta(mid + 1, end, alpha, beta, True))
#             return value


#     alpha_beta_value = alpha_beta(0, len(leaf_data) - 1, float('-inf'), float('inf'), True)

#     print(f"Final alpha-beta pruning is {alpha_beta_value}.")

# pacman_game(2)
# pacman_game(5)

###################################################################################################
# PART 3

# Is the first player always a maximizer node? Yes

#Can alpha-beta pruning handle stochastic environments? It is not designed to handel stochastic environments effectively.