import sys


def binary_search(int_list, target):
    low = 0
    high = len(int_list)
    steps = 0

    while low <= high:
        mid = (low + high) // 2
        steps += 1

        if (int_list[mid] == target):
            print(f'Target Value Found in List in {steps} iteration(s)!')
            return target
        elif (int_list[mid] < target):
            low = mid + 1
        else:
            high = mid - 1

    reload_flg = input(
        'Target Value Not Found in List :(\nTry a Different Integer? [y/n]')
    reload(reload_flg.lower(), int_list)
    return -1


def options(int_list):
    target = input(
        f'\n{int_list}\n\nWelcome to BinarySearch Algorithm.\nFrom the intlist of sorted intergers provided above, please enter the target value: ')
    return int(target)


def reload(reload_flg, int_list):
    match reload_flg:
        case 'y':
            target = options(int_list)
            binary_search(int_list, target)
        case 'n':
            sys.exit()
        case _:
            print('Invalid Option :(\nPlease try again.')
            options()


sorted_list = [1, 5, 7, 9, 14, 19, 22, 27, 32, 41]

target = options(sorted_list)
result = binary_search(sorted_list, int(target))
