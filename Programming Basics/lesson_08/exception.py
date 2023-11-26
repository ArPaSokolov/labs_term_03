# try:
#     a = int(input())
#     print(a ** 2)
# except Exception as e:
#     print(e)
#
# print("End")

class TooFewApples(Exception):
    pass

def devider(apples, friends):
    if apples >= friends:
        return apples // friends
    else:
        raise TooFewApples("Слишком мало яблок - давай мясо!")
try:
    print(devider(1, 3))
except Exception as e:
    print(e)
