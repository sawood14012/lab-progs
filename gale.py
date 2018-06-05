#preferred_rankings_men={}
#preferred_rankings_women={}

n = int(input("enter the no of men and woman"))
preferred_rankings_men = {}
for i in range(n):
    man = input("enter the man ")
    lis1 = []
    for j in range(n):
        woman = input("enter the woman ")
        lis1.append(woman)
        preferred_rankings_men[man] = lis1

print(preferred_rankings_men)


#n = int(input("enter the no of men"))
preferred_rankings_women = {}
for i in range(n):
    woman = input("enter the woman ")
    lis2 = []
    for j in range(n):
        man = input("enter the man ")
        lis2.append(man)
        preferred_rankings_women[woman] = lis2

print(preferred_rankings_women)


tentative_engagements = []

# Men who still need to propose and get accepted successfully
free_men = []


def init_free_men():
    for man in preferred_rankings_men.keys():
        free_men.append(man)


def beginmatching(man):
    print("Dealing with %s" % (man))
    for woman in preferred_rankings_men[man]:
        takenmatch = [couple for couple in tentative_engagements if woman in couple]

        if (len(takenmatch) == 0):
            tentative_engagements.append([man, woman])
            free_men.remove(man)
            print("%s is now engaged with %s" % (man, woman))
            break


        elif (len(takenmatch) > 0):
            print(" %s is alreadey enggaged " %(woman))
            currentguy = preferred_rankings_women[woman].index(takenmatch[0][0])
            potentialguy = preferred_rankings_women[woman].index(man)

            if (currentguy < potentialguy):
                print("she is not satisfied with %s" %(man))

            else:
                print("%s is better than %s" %(man, takenmatch[0][0]))
                print('Making %s free again.. and tentatively engaging %s and %s' % (takenmatch[0][0], man, woman))
                free_men.remove(man)
                free_men.append(takenmatch[0][0])
                takenmatch[0][0] = man
                break


def stablematching():
    while len(free_men) > 0:
        for man in free_men:
            beginmatching(man)


def main():
    init_free_men()
    print(free_men)
    stablematching()
    print(tentative_engagements)


main()