# - get(key: int) -> int:
# - delete(key: int) -> None:
# - put(key: int, value: int) -> None:
#
#

l1 = {}


def put(key, value):
    try:
        l1[key] = value
    except BaseException as e:
        print(e.args)
        print("something wrong")


def delete(key):
    try:
        del l1[key]
    except BaseException as e:
        print(e.args)
        print("something wrong")


def get(key):
    try:
        return l1[key]
    except BaseException as e:
        print(e.args)
        print("something wrong")


put(1, '2')
put('2', '3')
delete('9')
print(l1)
