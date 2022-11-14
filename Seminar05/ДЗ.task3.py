#########################################################################
#  Создайте программу для игры в ""Крестики-нолики"".
#########################################################################

# empty_field = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]


# def print_field(field):
#     print("┌───┬───┬───┐")
#     print("│ "+" │ ".join(field[0])+" │")
#     print("├───┼───┼───┤")
#     print("│ "+" │ ".join(field[1])+" │")
#     print("├───┼───┼───┤")
#     print("│ "+" │ ".join(field[2])+" │")
#     print("└───┴───┴───┘")


# def make_move(field, move, symbol):
#     result = field.copy()
#     move = move.split()
#     [x, y] = list(map(int, move))
#     if (3 > x >= 0) and (3 > y >= 0) and result[y][x] == " ":
#         result[y][x] = symbol
#     else:
#         new_attempt = input("Неправильный ход, повторите ввод: ")
#         result = make_move(field, new_attempt, symbol)
#     return result


# def check_win(field):
#     # проверка ряда
#     for row in field:
#         if row[0] == "X" and row[1] == "X" and row[2] == "X":
#             return "X"
#         if row[0] == "0" and row[1] == "0" and row[2] == "0":
#             return "0"
#     # проверка колонки
#     for col in range(3):
#         if field[0][col] == "X" and field[1][col] == "X" and field[2][col] == "X":
#             return "X"
#         if field[0][col] == "0" and field[1][col] == "0" and field[2][col] == "0":
#             return "0"
#     # проверка диагонали
#     if field[0][0] == "X" and field[1][1] == "X" and field[2][2] == "X":
#         return "X"
#     if field[0][2] == "X" and field[1][1] == "X" and field[2][0] == "X":
#         return "X"
#     if field[0][0] == "0" and field[1][1] == "0" and field[2][0] == "0":
#         return "0"
#     if field[0][2] == "0" and field[1][1] == "0" and field[2][0] == "0":
#         return "0"
#     return None

# field = empty_field
# moves_count = 0
# is_X_move = True
# print("Добро пожаловать в игру X-0. В свой ход вводите координаты, разделенные пробелом.")
# while check_win(field) == None and moves_count < 9:
#     current_player = "X" if is_X_move else "0"
#     field = make_move(field, input(
#         f"Ход игрока {current_player}: "), current_player)
#     print_field(field)
#     is_X_move = not is_X_move
#     moves_count += 1
# print("Игра окончена")
# result = check_win(field)
# if result == None:
#     print("Ничья")
# else:
#     print(f"Победитель: игрок {result}")

###################################################################################################


# def create_field():
#     return[
#         [0, 0, 0],
#         [0, 0, 0],
#         [0, 0, 0]
#     ]
# def get_user_name(message:str, users: dict):
#     while(True):
#         name = input(message)
#         if name in users:
#             print('Имя уже занято, введите псевдоним!')
#         else:
#             users[name] = list()
#             break

# def is_win(field: list):
#     sum_to_win = 3
#     row_sum = 0
#     column_sum = 0
#     dioganal_left_sum = 0
#     dioganal_right_sum = 0
#     is_not_empty = True

#     for i in range(len(field)):
#         for j in range(len(field[i])):
#             row_sum += field[i][j]
#             column_sum += field[j][i]

#             if(field[i][j]) == 0:
#                 is_not_empty = False
#             if i == j:
#                 dioganal_left_sum += field[i][j]
#             if len(field[i]) -1 -i == j:
#                 dioganal_right_sum += field[i][j]
#         if abs(row_sum) == sum_to_win or abs(column_sum) == sum_to_win:
#             return 1
#         else:
#             row_sum = 0
#             column_sum = 0

#     if abs(dioganal_left_sum) == sum_to_win or abs(dioganal_right_sum) == sum_to_win:
#         return 1

#     if is_not_empty:
#         return -1

#     return 0

# def get_mark(val: int):
#     marks = {
#         -1: '0',
#         1: 'X'
#     }

#     if val in marks:
#         return marks[val]
#     else:
#         return' '

# def print_field(field: dict):
#     count = 1

#     for i in range(len(field)):
#         print()
#         for j in range(len(field[i])):
#             if 0 == j or j == len(field[i]):
#                 print('', end='')
#             else:
#                 print('|', end='')
#             print(f'  {get_mark(field[i][j])}  ', end='')
#             count += 1
#         print('\n')                             
#         for c in range(count - len(field), count):
#             print(f'---{c}---', end='')
#         print()

# def handle_user_input(field: list, sign: int, name: str, users: dict):
#     max_number = len(field) * len(field[0])
#     while(True):
#         try:
#             cell_number = int(input(f'{name} укажите номер ячейки: '))
#             cell_number = cell_number - 1
#             if 0 <= cell_number < max_number:
#                change_cell(cell_number, sign, field)
#                users[name].append(cell_number)
#                return cell_number
#             else:
#                raise ValueError('Wrong number')
#         except:
#             print('Не допустимое значение, повторите ввод!')
#             continue

# def change_cell(cell_number: int, sign: int, field: list):
#     row = cell_number // 3
#     col = cell_number % 3

#     if(field[row][col] != 0):
#         raise ValueError('Не пустое поле!')

#     field[row][col] = sign

# def tik_tak_game():
#     users = dict()
#     get_user_name('Введите имя первого игрока: ',  users)
#     get_user_name('Введите имя второго игрока: ',  users)

#     field = create_field()
#     game = is_win(field)
#     print_field(field)
#     while(game == 0):
#         sign = 1
#         for name, _ in users.items():
#             handle_user_input(field, sign, name, users)
#             print_field(field)
#             game = is_win(field)
#             if game == 1:
#                 print(f'Выиграл игрок {name}')
#                 return
#             elif game == -1:
#                 print('Ничья')
#                 return
#             sign *= -1
 
# tik_tak_game()

###################################################################################

# def field(moves):
#     y0 = f"    X1    X2   X3  "
#     y1 = f"Y1  {moves['y1']['x1']}  |  {moves['y1']['x2']}  | {moves['y1']['x3']}  "
#     y1_1 = "  -----+-----+-----"
#     y2 = f"Y2  {moves['y2']['x1']}  |  {moves['y2']['x2']}  | {moves['y2']['x3']}  "
#     y1_1 = "  -----+-----+-----"
#     y3 = f"Y3  {moves['y3']['x1']}  |  {moves['y3']['x2']}  | {moves['y3']['x3']}  "
#     print(y0)
#     print(y1)
#     print(y1_1)
#     print(y2)
#     print(y1_1)
#     print(y3)


# def check(move, moves):
#     if len(move) == 4:
#         if move[0].lower() == 'y' and move[2].lower() == 'x':
#             if move[1] in '123' and move[-1] in '123':
#                 if moves[move[:2]][move[-2:]] == ' ':
#                     return True
#                 else:
#                     print('Данная клетка уже занята.')
#             else:
#                 print('Введены недопустимые значения координат.')
#         else:
#             print('Вы ввели не допустимые оси координат')
#     else:
#         print('Введено недопустимое количество символов.')
#     print('Попробуйте ещё раз!')
#     return False


# def wins(moves):
#     if ((moves['y1']['x1'] == moves['y1']['x2'] == moves['y1']['x3']
#             or moves['y1']['x1'] == moves['y2']['x1'] == moves['y3']['x1']
#             or moves['y1']['x1'] == moves['y2']['x2'] == moves['y3']['x3'])
#             and moves['y1']['x1'] != ' '):
#         return moves['y1']['x1']
#     elif ((moves['y2']['x1'] == moves['y2']['x2'] == moves['y2']['x3']
#            or moves['y1']['x2'] == moves['y2']['x2'] == moves['y3']['x2']
#            or moves['y1']['x3'] == moves['y2']['x2'] == moves['y3']['x1'])
#           and moves['y2']['x2'] != ' '):
#         return moves['y2']['x2']
#     elif ((moves['y3']['x1'] == moves['y3']['x2'] == moves['y3']['x3']
#            or moves['y1']['x3'] == moves['y2']['x3'] == moves['y3']['x3'])
#           and moves['y3']['x3'] != ' '):
#         return moves['y3']['x3']
#     return False


# def move(symbol, moves, player):
#     print('Текущий ход y{}x{}'.format(player[1], player[-1]))
#     if player[1] == '1':
#         if player[-1] == '1':
#             moves['y1']['x1'] = symbol
#         elif player[-1] == '2':
#             moves['y1']['x2'] = symbol
#         else:
#             moves['y1']['x3'] = symbol
#     elif player[1] == '2':
#         if player[-1] == '1':
#             moves['y2']['x1'] = symbol
#         elif player[-1] == '2':
#             moves['y2']['x2'] = symbol
#         else:
#             moves['y2']['x3'] = symbol
#     else:
#         if player[-1] == '1':
#             moves['y3']['x1'] = symbol
#         elif player[-1] == '2':
#             moves['y3']['x2'] = symbol
#         else:
#             moves['y3']['x3'] = symbol
#     return moves


# moves_out = {
#     'y1': {'x1': ' ', 'x2': ' ', 'x3': ' '},
#     'y2': {'x1': ' ', 'x2': ' ', 'x3': ' '},
#     'y3': {'x1': ' ', 'x2': ' ', 'x3': ' '}
# }

# field(moves_out)

# number_players = int(input('Введите количество игроков (1/2): '))
# count_move = 0

# if number_players == 2:
#     win = False
#     while not win and count_move < 9:
#         count_move += 1
#         player_out = input('Введите координаты хода(пример - y2x3): ')
#         while not check(player_out, moves_out):
#             player_out = input('Введите координаты хода(пример - y2x3): ')
#         if count_move % 2:
#             symbol_out = 'X'
#         else:
#             symbol_out = 'O'
#         moves_out = move(symbol_out, moves_out, player_out)

#         field(moves_out)
#         win = wins(moves_out)
#     if count_move == 9:
#         print('Ничья!')
#     else:
#         print(f'На {count_move} ходу победили "{win}"')


########################################################################################

import os
import random


#  Function check winner after every turn
def winner_check(board):
    winner = ""
    # check rows
    if board[0] == board[1] ==board[2]: winner = board[0]
    elif board[3] == board[4] ==board[5]: winner = board[3]
    elif board[6] == board[7] ==board[8]: winner = board[6]
    # check colums
    if board[0] == board[3] ==board[6]: winner = board[0]
    elif board[1] == board[4] ==board[7]: winner = board[1]
    elif board[2] == board[5] ==board[8]: winner = board[2]
    # check diagonals
    if board[0] == board[4] ==board[8]: winner = board[0]
    elif board[2] == board[4] ==board[6]: winner = board[2]
    return winner
#  Function check man turn
def man_turn(board):
    clean_list = ([x for x in board if x.isdigit()])
    choose = input("Your turn, enter cell number: ")
    while choose not in clean_list:
        fresh_screen(board)
        print('{choose} is invalid: ')
        choose = input("Your turn, enter cell number: ")
    for num, x in enumerate(board):
        if x == choose:
            board[num] = "0"
    return board
#  Function make random Bot turn
def bot_turn(board):
    clean_list = ([x for x in board if x.isdigit()])
    choose = random.choice(list(map(int, clean_list)))
    for num, x in enumerate(board):
        board[choose-1] = "X"
    return board
#  Function cliar screen and draw board
def fresh_screen(board):
    os.system('cls')
    for num, x in enumerate(board):
        print(*x, end = " ")
        if (num + 1)%3 == 0:
            print()
    return board
# Play board
board = \
[
"1","2","3",
"4","5","6",
"7","8","9"
]
# bot name< could be changer
bot = "Bot"
fresh_screen(board)
man = input("Enter your name: ")
# First player random choise
lot = random.choice([man, bot])
if lot == bot:
    fresh_screen(board)
    print(f'{lot} is first with eXes.', end="")
    input("Press inter to start!")
else:
    fresh_screen(board)
    print(f"{man} is first with zerOs. ", end="")
# Game core
count = 0
while count < 9:
    if lot == bot:
        board = bot_turn(board)
        fresh_screen(board)
        lot = man
    else:
        board = man_turn(board)
        fresh_screen(board)
        lot = bot
    if winner_check(board) == "0":
        print(f'The winner is {man}')
        exit()
    elif winner_check(board) == "X":
        print(f'The winner is {bot}')
    exit()
    count += 1
print("Nobody wins")
exit()


    


