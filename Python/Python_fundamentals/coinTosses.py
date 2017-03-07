def toss():
    heads = 0
    tails = 0
    for count in range(0, 5000):
        import random
        num = random.random()
        num_rounded = round(num)
        if num_rounded == 0:
            heads = heads + 1
            print "Attempt # " + str(count) +": Throwing a coin... It's a head! ... Got " + str(heads) + " head(s) so far and "+ str(tails) + "tails so far"
        elif num_rounded ==1:
            tails = tails + 1
            print "Attempt # " + str(count) +": Throwing a coin... It's a tail! ... Got " + str(heads) + " head(s) so far and "+ str(tails) + "tail(s) so far"
toss()
