a = 123
TOTAL_LIVES = 10


def damage(current_lives) -> int:
    return current_lives - 5


def print_remaining_lives(func):
    print(func)
    print(f"you have {func(20)} remaining")


print_remaining_lives(damage)

