#Part 1
def stars(x):
    for i in x:
        star = ""
        for count in range (0, i):
            star = star + "*"
        print star
stars([4,6,1,3,5,7,25])

#Part2
def mod_stars(a):
    for i in a:
        star = ""
        letter = ""
        if type(i) is type(1):
            for count in range (0, i):
                star +=  "*"
            print star
        else:
            for count in range (0, len(i)):
                letter += i[0]
            print letter
a = [1,5,"hello", 7, "yesterday", "hi", 9]
mod_stars(a)
