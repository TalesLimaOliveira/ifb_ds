def mario_pyramid(height):
    for i in range(1, height + 1):
        spaces = ' ' * (height - i)
        blocks = '#' * i
        print(spaces + blocks)

user_height = int(input("Tamanho: "))
mario_pyramid(user_height)