def card_name(suit: int) -> str:
        return ['пики', 'трефы', 'бубны', 'червы'][suit - 1] \
            if 1 <= suit <= 4 else 'Неизвестно'
print(card_name(int(input('Масть: '))))