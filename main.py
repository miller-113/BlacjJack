from Game import Game

if __name__ == '__main__':
    player_money, ask_start, temp = 1000, True, ''
    while player_money != 0:

        temp = Game()
        temp.start_game()
        print(f'Bank: {player_money + temp.player.money - 1000}')
        player_money += temp.player.money - 1000
        choice = input('Regame? (y/n)')
        if choice == 'n':
            break
