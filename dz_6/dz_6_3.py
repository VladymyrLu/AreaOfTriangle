height = int(input('ширина треугольника   '))
width = 0
while width <= height:
    print((' ' * width) + ((height - width) * '*'))
    width += 1
