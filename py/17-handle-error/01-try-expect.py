while True:
    try:
        x = int(input('please enter a number: '))
        print(x)
        break
    except ValueError:
        print('You enter not a number, please return enter!')