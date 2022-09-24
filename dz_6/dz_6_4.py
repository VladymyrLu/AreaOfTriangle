height = int(input('ширина треугольника   '))
width = 1
while width <= height:
    print((' ' * (height - width))+('*' * width))
    width += 1



