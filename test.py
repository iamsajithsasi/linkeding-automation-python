condition = True
while condition:
    link = [1, 2, 3]
    index = 1
    for el in link:
        print(link)
    try:
        print('Try block')
        condition = False
    except:
        print('Except block')
        condition = False
