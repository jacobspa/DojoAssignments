def scores_Grades():
    import random
    random_num = random.random()*40+61
    print random_num
    if random_num < 70:
        return "Score "+ str(random_num) +"; Your grade is D"
    elif random_num < 80:
        return "Score "+ str(random_num) +"Your grade is C"
    elif random_num < 90:
        return "Score "+ str(random_num) + "Your grade is B"
    else:
        return "Score "+ str(random_num) +"Your grade is A"

print scores_Grades()
print "THESE PARENTHESES ARE MAKING ME SAD"
# ans = scores_Grades()
# print ans
