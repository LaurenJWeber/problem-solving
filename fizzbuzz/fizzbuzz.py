name = "fizzbuzz"


def fizz_buzz(test_integer: int) -> str:
    if(test_integer % 3 == 0) and (test_integer % 5 == 0):
        return "fizzbuzz"
    elif test_integer % 3 == 0:
        return "fizz"
    elif test_integer % 5 == 0:
        return "buzz"
    else:
        return str(test_integer)


for i in range(1, 6):
    result = fizz_buzz(i)
    print(result)
