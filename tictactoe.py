class TicTacToe:
    field_size = 9
    player_numbers1 = []
    player_numbers2 = []

    combination_win = [
        [1, 2, 3], [4, 5, 6], [7, 8, 9],
        [1, 4, 7], [2, 5, 8], [3, 6, 9],
        [3, 5, 7], [1, 5, 9]
    ]

    def get_field_size(self):
        return self.field_size

    def check_win_combination(self, player_numbers):
        result = False

        if len(player_numbers) < 3:
            return result

        for numbers in self.combination_win:
            win = []
            for number in numbers:
                if number in player_numbers:
                    win.append(number)
            if len(win) == 3:
                result = True
                break

        return result

    def player1_hit(self, number):
        self.player_numbers1.append(number);
        return self.check_win_combination(self.player_numbers1)

    def player2_hit(self, number):
        self.player_numbers2.append(number);
        return self.check_win_combination(self.player_numbers2)


# application
game = TicTacToe()
print('player 1 hit')
print(game.player1_hit(1))
print('player 2 hit')
print(game.player2_hit(2))
print('player 1 hit')
print(game.player1_hit(3))
print('player 2 hit')
print(game.player2_hit(4))
print('player 1 hit')
print(game.player1_hit(5))
print('player 2 hit')
print(game.player2_hit(6))
print('player 1 hit')
print(game.player1_hit(7))
