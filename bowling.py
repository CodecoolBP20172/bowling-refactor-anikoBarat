import string


def score(game):
    result = 0
    frame = 1
    first_try = True
    for i in range(len(game)):
        if game[i] == '/':
            result += 10 - last
        else:
            result += get_points(game[i])
        if frame < 10 and get_points(game[i]) == 10:
            if game[i] == '/' or game[i].lower() == 'x':
                result += get_points(game[i + 1])
            if game[i].lower() == 'x':
                if game[i + 2] == '/':
                    result += 10 - get_points(game[i + 1])
                else:
                    result += get_points(game[i + 2])
        last = get_points(game[i])
        if not first_try or game[i].lower() == 'x':
            first_try = True
            frame += 1
        else:
            first_try = False
    return result


def get_points(char):
    if char in string.digits:
        return int(char)
    elif char.lower() == 'x':
        return 10
    elif char == '/':
        return 10
    elif char == '-':
        return 0
    else:
        raise ValueError()