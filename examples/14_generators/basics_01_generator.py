def generate_nums(number):
    print('Start')
    yield number
    print('Next number')
    yield number + 100
    print('The End')


