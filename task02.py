# Вы когда-нибудь играли в игру "Крестики-нолики"? 
# Попробуйте создать её, причем чтобы сыграть в нее можно было в одиночку. 

# print("*" * 10, " Игра Крестики-нолики для двух игроков ", "*" * 10)

# board = list(range(1,10))

# def draw_board(board):
#    print("-" * 13)
#    for i in range(3):
#       print("|", board[0+i*3], "|", board[1+i*3], "|", board[2+i*3], "|")
#       print("-" * 13)

# def take_input(player_token):
#    valid = False
#    while not valid:
#       player_answer = input("Куда поставим " + player_token+"? ")
#       try:
#          player_answer = int(player_answer)
#       except:
#          print("Некорректный ввод. Вы уверены, что ввели число?")
#          continue
#       if player_answer >= 1 and player_answer <= 9:
#          if(str(board[player_answer-1]) not in "XO"):
#             board[player_answer-1] = player_token
#             valid = True
#          else:
#             print("Эта клетка уже занята!")
#       else:
#         print("Некорректный ввод. Введите число от 1 до 9.")

# def check_win(board):
#    win_coord = ((0,1,2), (3,4,5), (6,7,8), (0,3,6), (1,4,7), (2,5,8), (0,4,8), (2,4,6))
#    for each in win_coord:
#        if board[each[0]] == board[each[1]] == board[each[2]]:
#           return board[each[0]]
#    return False

# def main(board):
#     counter = 0
#     win = False
#     while not win:
#         draw_board(board)
#         if counter % 2 == 0:
#            take_input("X")
#         else:
#            take_input("O")
#         counter += 1
#         if counter > 4:
#            tmp = check_win(board)
#            if tmp:
#               print(tmp, "выиграл!")
#               win = True
#               break
#         if counter == 9:
#             print("Ничья!")
#             break
#     draw_board(board)
# main(board)

# input("Нажмите Enter для выхода!")




# ========================================

# Хранить все будем в одномерном массиве
field = '123456789'

def PrintField(local_field):
    print('-' * 13)
    for i in range(3):
        print(f'| {local_field[i*3]} | {local_field[i*3 + 1]} | {local_field[i*3 + 2]} |')
        print('-' * 13)

def MyInput(local_field):
    num = int(input('Введите позию, куда хотите сходить 1..9: '))
    #not_ok_input = False
    while True: #not_ok_input:
        if not ((0 < num) and (num < 10)):
            print('Ввели неправильное место на поле')
        elif not(local_field[num-1] in '123456789'):
            print('Это поле уже занято')
        else: return str(num)
        num = int(input('Введите позию, куда хотите сходить 1..9: '))

def MyCheckGame(local_field):
    win_patterns = ((0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6))
    if len(local_field.replace('X','').replace('O','')) == 0: return 'Победила дружба! Ничья!'
    return 'None'

print(' Крестики - нолики (без ИИ, играют только человеки)')
game_result = 'None'
x_turn = True # Х - ходят первые


while game_result == 'None':
    PrintField(field)
    if x_turn: 
        print('Ходят X')
        field = field.replace(MyInput(field),'X')
    else: 
        print('Ходят O')
        field = field.replace(MyInput(field),'O')
    game_result = MyCheckGame(field)
    x_turn = not x_turn

print('Игра окончена')
print(game_result)

