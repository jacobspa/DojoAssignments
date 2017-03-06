# This is for part 1
for count in range(1, 1001):
    if count % 2 == 1:
        print "looping -", count

#This is for part 2
for count in range(1, 1000001):
    if count % 5 == 0:
        print "looping -", count

#This is for Sum List
a = [1,2,5,10,255,3]
ans = 0
for count in a:
    ans = ans + count
    print ans

#this is for Average List
ans = 0
for count in a:
    ans = ans + count
ans = ans/len(a)
print ans
