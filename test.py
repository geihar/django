a = [2, 1, 4, 5, 3, 7, 8]

def sort(li):
    n = len(li)
    print(n)
    for i in range(1, n):

        while i > 0 and li[i - 1] > li[i]:
            li[i], li[i - 1] = li[i - 1], li[i]
            i-=1

    print(li)



def sort2(li):
    n = len(li)
    print(n)
    for i in range(1, n):

        while i > 0 and li[i - 1] > li[i]:
            li[i], li[i - 1] = li[i - 1], li[i]
            i-=1

    print(li)

b = [2, 1, 4, 5, 3, 7, 8]

c = [2, 1, 4, 5, 3, 7, 8]
sort(a)


# mkdir project
# cd project
# python -m venv venv
#
# venv\Scripts\activate.bat