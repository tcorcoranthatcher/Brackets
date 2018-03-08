import operator

master = [1, 4, 5, 8, 10, 11, 13, 15, 17, 19, 22, 23, 26, 27, 30, 31, 33, 36, 37, 39, 41, 44, 45, 47, 49, 52, 54, 55,
          58, 59, 62, 64, 1, 5, 11, 15, 17, 23, 27, 31, 33, 37, 41, 45, 49, 55, 58, 62, 1, 11, 17, 27, 33, 41, 49, 58, 1, 17,
          33, 49, 0, 0, 0]


class bracket:
    def __init__(self, name, bracket, points, wins, chances):
        self.name = name
        self.bracket = bracket
        self.points = points
        self.wins = wins


def check(master, check):
    for i in range(1, 64):
        if i <= 32:
            if master[i - 1] == check.bracket[i - 1]:
                check.points += 1
        if 32 < i <= 48:
            if master[i - 1] == check.bracket[i - 1]:
                check.points += 2
        if 48 < i <= 56:
            if master[i - 1] == check.bracket[i - 1]:
                check.points += 4
        if 56 < i <= 60:
            if master[i - 1] == check.bracket[i - 1]:
                check.points += 8
        if 60 < i <= 62:
            if master[i - 1] == check.bracket[i - 1]:
                check.points += 16
        if 62 < i <= 63:
            if master[i - 1] == check.bracket[i - 1]:
                check.points += 32
    return check.name, check.points


def checkprint(master, pool):
    leaderboard = []
    for i in pool:
        reset = i.points
        checked = check(master, i)
        leaderboard.append(checked)
        i.points = reset

    def getKey(item):
        return item[1]

    return sorted(leaderboard, key=getKey, reverse=True)


def chance_after_first_weekend(master, pool):
    iterator_dict = {}
    for i in range(32768, 65536):
        holder = []
        binary_conversion = bin(i)
        string_conversion = str(binary_conversion)
        for j in range(3, len(string_conversion)):
            if string_conversion[j] == "1":
                int_conversion = 1
            else:
                int_conversion = 0
            holder.append(int_conversion)
        iterator_dict[i - 32767] = holder

    for i in range(1, len(iterator_dict)+1):
        master_check = master
        iteration = iterator_dict[i]
        for j in range(8):
            if iteration[14-j] == 0:
                master_check[48+j] = master_check[32 + 2*j]
            else:
                master_check[48+j] = master_check[32 + 2*j + 1]
        for j in range(4):
            if iteration[6-j] == 0:
                master_check[56+j] = master_check[48 + 2*j]
            else:
                master_check[56+j] = master_check[48 + 2*j + 1]
        for j in range(2):
            if iteration[2-j] == 0:
                master_check[60+j] = master_check[56 + 2*j]
            else:
                master_check[60+j] = master_check[56 + 2*j + 1]
        if iteration[0] == 0:
            master_check[62] = master_check[60]
        else:
            master_check[62] = master_check[61]
        iteration_outcome = checkprint(master_check, pool)

        for k in range(len(pool)):
            if pool[k].name == iteration_outcome[0][0]:
                pool[k].wins += 1
                for l in range(1, len(iteration_outcome)):
                    if iteration_outcome[l][1] == iteration_outcome[0][1]:
                        for m in range(31):
                            if pool[m].name == iteration_outcome[l][0]:
                                pool[m].wins += 1
                    else:
                        break
    for j in range(len(pool)):
        print(str(pool[j].name)+" has a " + str(round(float(100*pool[j].wins/32768), 2)) + "% chance to win the pool")


def chance_after_second_weekend(master, pool):
    iterator_dict = {}
    for i in range(8, 16):
        holder = []
        binary_conversion = bin(i)
        string_conversion = str(binary_conversion)
        for j in range(3, len(string_conversion)):
            if string_conversion[j] == "1":
                int_conversion = 1
            else:
                int_conversion = 0
            holder.append(int_conversion)
        iterator_dict[i - 7] = holder

    for i in range(1, len(iterator_dict)+1):
        master_check = master
        iteration = iterator_dict[i]
        for j in range(2):
            if iteration[2-j] == 0:
                master_check[60+j] = master_check[56 + 2*j]
            else:
                master_check[60+j] = master_check[56 + 2*j + 1]
        if iteration[0] == 0:
            master_check[62] = master_check[60]
        else:
            master_check[62] = master_check[61]
        iteration_outcome = checkprint(master_check, pool)

        for k in range(len(pool)):
            if pool[k].name == iteration_outcome[0][0]:
                pool[k].wins += 1
                for l in range(1, len(iteration_outcome)):
                    if iteration_outcome[l][1] == iteration_outcome[0][1]:
                        for m in range(31):
                            if pool[m].name == iteration_outcome[l][0]:
                                pool[m].wins += 1
                    else:
                        break

    for j in range(len(pool)):
        print(str(pool[j].name)+" has a " + str(round(float(100*pool[j].wins/8), 2)) + "% chance to win the pool")


Krysta = bracket("Krysta",
                 [1, 3, 6, 8, 9, 11, 13, 15, 17, 19, 22, 24, 26, 27, 30, 31, 33, 36, 37, 40, 41, 44, 46, 47, 49, 52, 54,
                  55, 58, 59, 61, 63, 1, 8, 11, 15, 19, 24, 27, 30, 33, 40, 44, 47, 49, 54, 59, 63, 1, 11, 19, 27, 40,
                  47, 54, 63, 1, 27, 47, 54, 1, 54, 1], 0, 0, 0)
Don = bracket("Don",
              [1, 3, 5, 7, 9, 11, 14, 15, 17, 19, 21, 23, 25, 27, 30, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49, 51, 53,
               55, 57, 59, 61, 63, 1, 7, 9, 15, 19, 23, 25, 31, 33, 39, 43, 47, 49, 53, 57, 63, 1, 9, 23, 31, 33, 47,
               53, 63, 1, 31, 33, 53, 1, 33, 33], 0, 0, 0)
Barb = bracket("Barb",
               [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 30, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49, 51, 53,
                55, 57, 59, 61, 63, 1, 7, 11, 15, 17, 23, 25, 31, 33, 39, 43, 47, 49, 53, 57, 63, 1, 15, 17, 31, 33, 47,
                49, 63, 1, 31, 33, 63, 1, 33, 1], 0, 0, 0)
Darci = bracket("Darci",
                [1, 3, 5, 8, 9, 11, 13, 15, 17, 19, 22, 23, 25, 27, 30, 31, 33, 36, 37, 39, 42, 43, 46, 47, 49, 51, 54,
                 55, 58, 60, 61, 63, 1, 8, 11, 15, 17, 23, 27, 31, 33, 37, 43, 47, 49, 55, 60, 63, 1, 11, 17, 31, 33,
                 43, 49, 63, 1, 31, 43, 63, 31, 43, 43], 0, 0, 0)
Noel = bracket("Noel",
               [1, 3, 5, 8, 9, 11, 14, 15, 17, 20, 22, 23, 26, 27, 30, 31, 33, 36, 37, 39, 42, 43, 45, 47, 49, 52, 53,
                56, 57, 60, 62, 63, 1, 5, 9, 15, 17, 23, 27, 31, 33, 37, 43, 47, 49, 53, 57, 63, 5, 15, 17, 27, 37, 43,
                49, 63, 5, 17, 43, 63, 5, 63, 63], 0, 0, 0)
Violet = bracket("Violet",
                 [1, 4, 6, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 30, 31, 33, 36, 37, 39, 42, 43, 45, 47, 49, 51, 53,
                  55, 57, 59, 61, 63, 1, 7, 11, 15, 17, 23, 27, 31, 33, 39, 43, 47, 49, 55, 59, 63, 1, 11, 23, 31, 33,
                  47, 49, 63, 1, 31, 33, 63, 1, 33, 1], 0, 0, 0)
Tommy = bracket("Tommy",
                [1, 4, 6, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 42, 43, 45, 47, 49, 52, 53,
                 55, 57, 60, 61, 63, 1, 7, 11, 15, 17, 23, 27, 31, 33, 37, 43, 47, 49, 55, 60, 63, 1, 11, 23, 27, 33,
                 43, 49, 63, 11, 27, 33, 49, 27, 33, 33], 0, 0, 0)
Rebecca = bracket("Rebecca",
                  [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 30, 31, 33, 35, 37, 39, 41, 43, 46, 47, 49, 52,
                   53, 55, 58, 59, 100, 63, 1, 7, 11, 15, 17, 23, 25, 31, 33, 39, 43, 47, 49, 53, 59, 63, 1, 11, 23, 31,
                   33, 47, 53, 63, 1, 23, 33, 53, 1, 33, 1], 0, 0, 0)
John = bracket("John",
               [1, 3, 5, 7, 10, 11, 13, 15, 17, 20, 21, 23, 25, 27, 30, 31, 33, 35, 37, 39, 42, 43, 100, 47, 49, 52, 53,
                55, 57, 59, 61, 63, 1, 5, 11, 15, 17, 23, 27, 31, 33, 37, 43, 47, 49, 53, 57, 63, 1, 11, 23, 27, 33, 47,
                49, 63, 1, 23, 33, 63, 1, 63, 1], 0, 0, 0)
Gary = bracket("Gary",
               [1, 4, 5, 7, 9, 11, 14, 15, 17, 20, 21, 23, 25, 27, 30, 31, 33, 36, 37, 39, 41, 43, 45, 47, 49, 52, 53,
                55, 57, 60, 62, 63, 1, 5, 9, 15, 20, 23, 25, 31, 33, 39, 43, 47, 49, 53, 57, 63, 1, 15, 20, 31, 33, 43,
                49, 63, 1, 31, 43, 63, 1, 63, 1], 0, 0, 0)
Beau = bracket("Beau",
               [1, 4, 5, 7, 10, 11, 13, 15, 17, 20, 21, 23, 25, 27, 30, 31, 33, 36, 37, 39, 41, 43, 45, 47, 49, 52, 53,
                55, 58, 59, 61, 63, 1, 5, 11, 15, 17, 21, 27, 31, 33, 39, 41, 47, 49, 53, 59, 63, 1, 15, 17, 31, 33, 47,
                49, 63, 15, 17, 33, 63, 15, 63, 15], 0, 0, 0)
Ben = bracket("Ben",
              [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49, 52, 53,
               55, 57, 59, 61, 63, 1, 5, 11, 15, 17, 23, 27, 31, 33, 37, 43, 47, 49, 55, 59, 63, 1, 11, 17, 31, 33, 47,
               49, 63, 1, 17, 33, 63, 1, 63, 1], 0, 0, 0)
Harry = bracket("Harry",
                [1, 4, 5, 7, 9, 11, 13, 15, 17, 19, 22, 23, 25, 27, 30, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49, 52, 53,
                 55, 57, 59, 61, 63, 1, 5, 9, 15, 17, 23, 27, 31, 33, 37, 43, 47, 49, 53, 57, 63, 1, 9, 23, 27, 33, 47,
                 49, 63, 1, 27, 33, 63, 1, 33, 1], 0, 0, 0)
Michael = bracket("Michael",
                  [1, 3, 5, 7, 9, 11, 13, 15, 17, 20, 22, 23, 25, 27, 30, 31, 33, 36, 37, 39, 41, 43, 45, 47, 49, 52,
                   53, 55, 58, 59, 62, 63, 1, 5, 11, 15, 17, 23, 27, 31, 33, 39, 43, 47, 49, 53, 58, 63, 1, 15, 17, 31,
                   39, 43, 49, 63, 1, 31, 39, 63, 1, 63, 63], 0, 0, 0)
Anna = bracket("Anna",
               [1, 4, 5, 8, 9, 11, 13, 15, 17, 20, 21, 23, 25, 27, 30, 31, 33, 36, 37, 39, 41, 43, 46, 47, 49, 52, 53,
                55, 57, 59, 62, 63, 1, 5, 11, 15, 17, 23, 27, 31, 33, 39, 43, 47, 49, 53, 59, 63, 1, 15, 23, 27, 33, 43,
                49, 63, 1, 27, 33, 63, 1, 33, 1], 0, 0, 0)
Andy = bracket("Andy",
               [1, 4, 5, 7, 9, 11, 14, 15, 17, 20, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49, 52, 53,
                55, 58, 59, 62, 63, 1, 7, 9, 15, 17, 23, 25, 31, 33, 37, 43, 45, 49, 53, 59, 63, 7, 15, 17, 31, 33, 43,
                49, 59, 15, 17, 33, 49, 15, 49, 15], 0, 0, 0)
Zack = bracket("Zack",
               [1, 4, 5, 8, 9, 11, 14, 15, 17, 20, 21, 23, 25, 27, 29, 31, 33, 36, 37, 39, 41, 43, 45, 47, 49, 52, 53,
                55, 57, 59, 62, 63, 1, 8, 11, 15, 17, 23, 25, 31, 33, 37, 43, 45, 49, 53, 59, 63, 1, 15, 23, 31, 33, 45,
                53, 63, 15, 23, 33, 53, 15, 33, 15], 0, 0, 0)
Kyle = bracket("Kyle",
               [1, 3, 5, 7, 10, 11, 14, 15, 17, 19, 21, 23, 26, 27, 30, 31, 33, 36, 37, 39, 42, 43, 45, 47, 49, 52, 53,
                55, 58, 60, 61, 63, 1, 5, 10, 15, 17, 23, 26, 31, 33, 39, 42, 45, 49, 55, 60, 63, 1, 15, 23, 31, 39, 42,
                55, 63, 1, 23, 39, 55, 23, 39, 39], 0, 0, 0)
Deb = bracket("Deb",
              [1, 4, 6, 7, 10, 11, 14, 15, 17, 19, 21, 23, 26, 27, 30, 31, 33, 36, 38, 39, 41, 43, 45, 47, 49, 52, 54,
               55, 57, 59, 62, 63, 1, 7, 10, 15, 17, 21, 25, 31, 33, 39, 43, 47, 49, 54, 59, 63, 1, 10, 17, 31, 33, 47,
               49, 63, 1, 17, 33, 63, 1, 63, 1], 0, 0, 0)
Kelsey = bracket("Kelsey",
                 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                  0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 11, 23, 31, 33, 47, 49, 63, 1, 23, 33, 63, 1, 63, 63],
                 51, 0, 0)
Jason = bracket("Jason",
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 15, 23, 31, 33, 47, 55, 63, 1, 23, 33, 63, 1, 63, 1], 45,
                0, 0)
Jim = bracket("Jim",
              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
               0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 15, 21, 31, 33, 47, 49, 63, 1, 31, 47, 63, 31, 63, 63], 44, 0,
              0)
Maurice = bracket("Maurice",
                  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                   0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 15, 17, 27, 33, 47, 49, 63, 15, 17, 33, 63, 15, 63, 63],
                  47, 0, 0)
Greg = bracket("Greg",
               [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 15, 17, 31, 39, 47, 49, 63, 1, 31, 39, 63, 1, 39, 1], 41, 0,
               0)
Humbert = bracket("Humbert",
                  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                   0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 13, 23, 31, 33, 43, 49, 63, 1, 31, 33, 63, 31, 63, 63],
                  45, 0, 0)
Steve = bracket("Steve",
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 11, 17, 31, 33, 43, 53, 63, 11, 31, 43, 63, 11, 63, 63],
                45, 0, 0)
Tim = bracket("Tim",
              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
               0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 15, 23, 27, 33, 41, 53, 63, 1, 27, 33, 63, 1, 33, 33], 44, 0,
              0)
Brandon = bracket("Brandon",
                  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                   0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 15, 17, 27, 37, 47, 49, 63, 1, 27, 37, 63, 1, 63, 63],
                  43, 0, 0)
Joanne = bracket("Joanne",
                 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                  0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 11, 17, 31, 37, 47, 49, 63, 1, 17, 33, 49, 1, 33, 33],
                 41, 0, 0)
Jean = bracket("Jean",
               [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 9, 17, 27, 33, 43, 53, 63, 1, 27, 33, 63, 1, 63, 1], 42, 0, 0)
Griffin = bracket("Griffin",
                  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                   0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 9, 17, 31, 33, 43, 53, 59, 1, 17, 33, 53, 17, 33, 17],
                  35, 0, 0)

pool = (
    Krysta, Don, Barb, Darci, Noel, Violet, Tommy, Rebecca, John, Gary, Beau, Ben, Harry, Michael, Anna, Andy, Zack,
    Kyle,
    Deb, Kelsey, Jason, Jim, Maurice, Greg, Humbert, Steve, Tim, Brandon, Joanne, Jean, Griffin)

chances = chance_after_first_weekend(master, pool)


