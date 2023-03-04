import base64


def base64ToString(b):
    return base64.b64decode(b).decode('utf-8')


def stringTobase64(s):
    return base64.b64encode(s.encode('utf-8'))

s = input("string: ")
b = input("base64: ")
print(stringTobase64(s))
print(base64ToString(b))


