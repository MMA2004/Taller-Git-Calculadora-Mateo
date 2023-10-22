from operations import add, rest
def game():
    score = 0
    while True:
        print('======== Menu ========'
              '\n1. Add'
              '\n2. Rest'
              '\n0. Exit')
        option = int(input('\nChoice an option: '))
        if option == 0:
            break
        num_1 = input('Enter first number: ')
        num_2 = input('Enter second number: ')
        answer = int(input('Enter you answer: '))

        if option == 1:
            result = add(num_1, num_2)
            if result == answer:
                score += 1
                print('Correct!!')
            else:
                print('Incorrect')
        if option == 2:
            result = rest(num_1, num_2)
            if result == answer:
                score += 1
                print('Correct!!')
            else:
                print('Incorrect')
        
    print(f'======== Game Over ========'
          f'\nYou score is {score}'
          '\nKeep going!')
game()
