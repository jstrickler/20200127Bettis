#!/usr/bin/env python


try:
    with open('DATA/wombat_fantasy.txt') as wf_in:
        pass

except FileNotFoundError as err:
    print(type(err))
    print(err)

data = ['a', 'b', 'c']
try:
    print(data[42])
except IndexError as err:
    print(err)


values = 5, 6.9, 0, 7.1, '123', 8

for v in values:
    try:
        result = 22 / v
    except ZeroDivisionError as err:
        print(err)
        exit()
    except TypeError as err:
        print(err)
    except Exception as err:
        print("Huh.", err)
    else:
        print(result)
    finally:
        print("AAA")

    print("BBB")

