
def stract_significant_value(number: float) -> int:
    int_number = 0
    characters_list = []
    if abs(number) < 1:
        while True:
            print(number)
            if abs(number) < 1:
                number = number*10
                print(characters_list)
                print(number)

            if abs(number) <= 10:
                characters_list.append(int(number))
                print(number)
                number = (number -int(number))*10
                print(number)

            print(characters_list)
            if number//10 == 0:
                break

    for i in range(len(characters_list)):
        int_number = characters_list[i]*(10**i)

    return int_number


def exact_sumation(a, b):
    # extract significant values

    # sum both as int

    # divide the result

    return a+b


if __name__ == "__main__":
    res = exact_sumation(1/10, 2/10)
    print(res)
    print(res == 3/10)
    print(stract_significant_value(0.12))