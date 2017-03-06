#Odd/Even
def odd_even():
    for count in range(1, 2001):
        if count % 2 == 0:
            print "Number is", count,"This is an even number"
        elif count % 2 == 1:
            print "Number is", count,"This an odd number"
odd_even()

#Multiply
a = [2,4,10,16]
def multiply(a, num):
    for index, count in enumerate(a):
        # print count
        # print a.index(count)
        a[index] = count * num
    return a

print multiply(a,5)
# print b
