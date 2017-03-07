str = "If monkeys like bananas, then I must be a monkey!"
a = str.find("monkey")
print a
b = str.replace("monkey", "alligator")
print b

x = [2,54,-2, 7, 12, 98]
print min(x)
print max(x)

x = ["hello", 2, 54,-2,7,12,98, "world"]
print x[0:1]
print x[len(x)-1:len(x)]
z = [x[0:1],x[len(x)-1:len(x)]]
print z

x = [19,2,54,-2,7,12,98,32,10,-3,6]
x.sort()
print x
z = x[0:len(x)/2]
print z
y = x[(len(x)/2):len(x)]
print y
y.insert(0 , z)
print y
