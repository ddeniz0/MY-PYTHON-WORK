def mükemmelsayı(sayı):
    toplam = 0

    for i in (1, sayı):

        if (sayı % i == 0):
            toplam += i

    return toplam == sayı


for i in range(1, 1001):

    if (mükemmelsayı(i)):
        print("sayı mükemmel sayı: ", i)
