import operator

master = [0, 0, 0, 0, 0, 11, 0, 0, 0, 0, 0, 23, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 49, 0, 0, 0, 0, 0, 61, 0,
          0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
          0, 0, 0, 0, 0, 0, 0, 0,
          0, 0, 0, 0,
          0, 0,
          0]

blank_bracket = []
for i in range(63):
    blank_bracket.append(-1)

class bracket:
    def __init__(self, name, bracket, points, wins):
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


Rob_1 = bracket("Rob H. - 1",
                [1, 3, 5, 7, 10, 11, 13, 15, 17, 19, 21, 23, 25, 27, 30, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49, 51, 53, 55, 58, 59, 62, 63,
                 1, 7, 10, 15, 17, 23, 27, 31, 33, 39, 43, 47, 49, 55, 59, 63,
                 1, 15, 17, 31, 33, 43, 49, 63,
                 15, 17, 33, 49,
                 17, 33,
                 17],
                0, 0)
Rob_2 = bracket("Rob H. - 2",
                [1, 3, 5, 7, 9, 11, 14, 15, 17, 20, 21, 23, 26, 27, 30, 31, 33, 35, 37, 39, 41, 43, 46, 47, 49, 51, 53, 55, 57, 59, 61, 63,
                 1, 5, 11, 15, 17, 23, 27, 31, 33, 37, 43, 47, 49, 53, 59, 63,
                 1, 11, 23, 27, 33, 47, 49, 59,
                 1, 23, 33, 59,
                 1, 33,
                 33],
                0, 0)
Rob_3 = bracket("Rob H. - 3",
                [1, 4, 5, 7, 10, 11, 14, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 36, 37, 39, 41, 43, 46, 47, 49, 51, 53, 55, 57, 59, 62, 63,
                 1, 7, 10, 15, 17, 23, 27, 31, 33, 37, 43, 47, 49, 55, 59, 63,
                 1, 15, 17, 31, 33, 47, 49, 63,
                 1, 17, 33, 49,
                 1, 49,
                 1],
                0, 0)
Sam = bracket("Sam Cooper",
              [1, 3, 5, 7, 9, 11, 14, 15, 17, 20, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 46, 47, 49, 52, 53, 55, 57, 59, 62, 63,
               1, 5, 9, 15, 17, 23, 27, 31, 33, 37, 41, 47, 49, 53, 59, 63,
               5, 15, 23, 31, 33, 41, 49, 63,
               5, 31, 33, 63,
               5, 63,
               63],
              0, 0)
Deb = bracket("Deb Cooper",
              [1, 4, 5, 7, 10, 11, 14, 15, 17, 19, 21, 23, 25, 27, 30, 31, 33, 36, 37, 40, 41, 43, 46, 47, 49, 52, 53, 55, 57, 59, 62, 63,
               1, 5, 11, 15, 17, 21, 27, 31, 36, 37, 41, 47, 49, 53, 59, 63,
               1, 11, 21, 27, 37, 47, 49, 59,
               11, 27, 47, 49,
               27, 49,
               49],
              0, 0)
Cooper_kids = bracket("Cooper Kids",
              [1, 4, 5, 7, 10, 11, 14, 15, 17, 20, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 46, 47, 49, 52, 54, 55, 58, 59, 62, 63,
               1, 7, 11, 15, 17, 23, 27, 31, 33, 37, 43, 47, 49, 55, 59, 63,
               1, 15, 17, 31, 33, 47, 49, 59,
               1, 31, 33, 59,
               1, 59,
               59],
              0, 0)
Kyle_and_Greg = bracket("Kyle and Greg",
              [1, 3, 5, 7, 10, 11, 14, 15, 17, 19, 21, 23, 25, 27, 30, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49, 51, 54, 55, 57, 59, 61, 63,
               1, 7, 11, 15, 17, 23, 27, 31, 33, 37, 43, 47, 49, 54, 59, 63,
               7, 15, 23, 27, 33, 47, 49, 63,
               7, 27, 33, 63,
               27, 33,
               27],
              0, 0)
Kyle = bracket("Kyle",
              [1, 3, 6, 7, 10, 11, 14, 15, 17, 20, 21, 23, 26, 27, 30, 31, 33, 35, 37, 39, 41, 43, 46, 47, 49, 51, 54, 55, 57, 59, 61, 63,
               1, 6, 10, 15, 20, 23, 26, 30, 33, 39, 43, 47, 51, 54, 59, 61,
               1, 15, 23, 30, 33, 43, 51, 59,
               1, 23, 33, 59,
               23, 33,
               33],
              0, 0)
Team_Tim = bracket("Team Tim",
              [1, 4, 5, 7, 9, 11, 13, 15, 17, 20, 21, 23, 25, 27, 29, 31, 33, 36, 37, 39, 41, 43, 46, 47, 49, 52, 53, 55, 57, 59, 61, 63,
               1, 5, 11, 15, 17, 23, 27, 31, 33, 37, 43, 47, 49, 55, 59, 63,
               1, 11, 17, 27, 33, 47, 49, 63,
               1, 27, 47, 49,
               27, 47,
               47],
              0, 0)
Barb = bracket("Bark Baker",
              [1, 3, 5, 7, 9, 11, 13, 15, 17, 20, 21, 23, 25, 27, 29, 31, 33, 36, 37, 39, 41, 43, 45, 47, 49, 51, 53, 55, 57, 59, 61, 63,
               1, 5, 11, 15, 17, 23, 27, 31, 33, 37, 43, 47, 49, 53, 59, 63,
               1, 11, 17, 27, 33, 47, 49, 59,
               1, 23, 33, 59,
               23, 33,
               33],
              0, 0)
Don = bracket("Don Baker",
              [1, 3, 5, 7, 10, 11, 13, 15, 17, 19, 22, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49, 51, 53, 55, 57, 59, 61, 63,
               1, 7, 11, 15, 17, 23, 27, 31, 33, 39, 41, 47, 49, 55, 59, 63,
               1, 15, 17, 27, 33, 47, 49, 63,
               1, 17, 47, 63,
               1, 47,
               47],
              0, 0)
Ben = bracket("Ben Milbrath",
              [1, 3, 5, 7, 10, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 46, 47, 49, 51, 53, 55, 57, 59, 62, 63,
               1, 5, 11, 15, 17, 23, 27, 31, 33, 39, 43, 46, 49, 55, 59, 63,
               1, 15, 17, 27, 33, 43, 49, 63,
               1, 17, 33, 49,
               1, 33,
               33],
              0, 0)
Gary = bracket("Gary Rose",
              [1, 3, 5, 7, 9, 11, 13, 15, 17, 20, 21, 23, 25, 27, 30, 31, 33, 35, 37, 39, 41, 43, 46, 47, 49, 51, 53, 55, 58, 59, 61, 63,
               1, 5, 11, 15, 17, 23, 27, 31, 33, 37, 41, 47, 51, 55, 59, 63,
               1, 15, 17, 27, 33, 47, 51, 59,
               1, 27, 33, 59,
               27, 33,
               27],
              0, 0)
Jason = bracket("Jason Cooper",
              [1, 4, 5, 7, 9, 11, 14, 15, 17, 19, 21, 23, 25, 27, 30, 31, 33, 35, 38, 39, 42, 43, 45, 47, 49, 52, 53, 55, 57, 59, 62, 63,
               1, 5, 11, 15, 17, 23, 27, 31, 33, 39, 42, 47, 49, 53, 57, 62,
               5, 15, 17, 31, 33, 47, 49, 57,
               5, 17, 47, 49,
               17, 49,
               49],
              0, 0)
Mrs_Outlaw = bracket("Mrs. Outlaw",
              [1, 3, 5, 7, 10, 11, 13, 15, 17, 19, 21, 23, 25, 27, 30, 31, 33, 36, 37, 39, 41, 43, 46, 47, 49, 51, 54, 56, 57, 59, 61, 63,
               1, 5, 10, 15, 17, 23, 27, 31, 33, 37, 41, 47, 49, 54, 59, 63,
               1, 15, 23, 31, 33, 47, 49, 59,
               1, 31, 33, 59,
               1, 33,
               1],
              0, 0)
Mr_Outlaw = bracket("Mr. Outlaw",
              [1, 4, 5, 7, 10, 11, 14, 15, 17, 19, 21, 24, 25, 27, 30, 31, 33, 35, 37, 39, 42, 43, 45, 47, 49, 52, 53, 55, 57, 59, 62, 63,
               1, 5, 10, 15, 17, 21, 27, 31, 33, 37, 43, 47, 49, 55, 59, 63,
               1, 15, 21, 27, 33, 47, 49, 63,
               1, 27, 33, 49,
               27, 49,
               49],
              0, 0)

Chris = bracket("Weeick",
              [1, 4, 5, 8, 10, 11, 14, 16, 17, 20, 21, 23, 26, 27, 29, 31, 33, 35, 37, 39, 41, 44, 46, 47, 49, 52, 53, 55, 57, 59, 62, 63,
               4, 5, 11, 16, 17, 23, 27, 31, 33, 39, 41, 46, 49, 55, 59, 63,
               4, 11, 23, 31, 33, 46, 49, 63,
               11, 31, 33, 63,
               31, 63,
               31],
              0, 0)
Fanny_1 = bracket("FanMartin",
                  [1, 4, 5, 7, 10, 11, 14, 15, 17, 19, 21, 23, 25, 27, 30, 31, 33, 36, 37, 39, 41, 43, 46, 47, 49, 52, 53, 55, 57, 59, 62, 63,
                   1, 5, 11, 15, 17, 23, 27, 31, 33, 37, 43, 47, 49, 55, 59, 63,
                   1, 15, 23, 31, 33, 47, 55, 63,
                   1, 31, 33, 63,
                   1, 33,
                   1],
                  0, 0)
Fanny_2 = bracket("Fanny8588 2",
                  [1, 3, 5, 7, 10, 11, 14, 15, 17, 19, 22, 23, 26, 27, 30, 31, 33, 36, 37, 39, 41, 44, 46, 47, 49, 52, 54, 55, 57, 59, 61, 63,
                   1, 7, 11, 15, 17, 22, 27, 31, 33, 39, 44, 46, 49, 55, 59, 63,
                   7, 15, 22, 27, 33, 46, 49, 63,
                   7, 27, 33, 63,
                   7, 33,
                   7],
                  0, 0)
Brandon_1 = bracket("BH1",
                    [1, 3, 5, 7, 9, 11, 14, 15, 17, 20, 21, 23, 26, 27, 29, 31, 33, 35, 37, 39, 41, 43, 46, 47, 49, 52, 53, 55, 57, 59, 62, 63,
                     1, 5, 11, 15, 17, 23, 27, 31, 33, 37, 41, 47, 49, 55, 59, 63,
                     5, 15, 17, 31, 33, 47, 49, 63,
                     5, 17, 47, 63,
                     17, 47,
                     47],
                    0, 0)
Brandon_2 = bracket("BH2",
                    [1, 3, 5, 7, 9, 11, 14, 15, 17, 20, 21, 23, 25, 27, 29, 31, 33, 36, 37, 39, 41, 44, 46, 47, 49, 51, 54, 55, 57, 59, 61, 63,
                     1, 7, 9, 15, 20, 23, 27, 31, 33, 37, 41, 47, 49, 55, 59, 63,
                     7, 15, 23, 31, 33, 47, 55, 63,
                     7, 31, 47, 63,
                     31, 47,
                     31],
                    0, 0)
Jean = bracket("JJ",
                    [1, 4, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49, 51, 53, 55, 57, 59, 61, 63,
                     1, 5, 11, 15, 17, 23, 27, 31, 33, 39, 43, 47, 49, 55, 59, 63,
                     1, 15, 17, 31, 33, 47, 49, 63,
                     1, 17, 31, 49,
                     1, 49,
                     1],
               0, 0)
Greg_1 = bracket("GregO my Eggo",
                    [1, 4, 6, 7, 9, 11, 14, 15, 17, 19, 21, 23, 26, 27, 29, 31, 33, 36, 37, 39, 41, 43, 46, 47, 49, 52, 53, 55, 58, 59, 61, 63,
                     1, 7, 9, 15, 17, 21, 27, 31, 33, 37, 43, 47, 49, 55, 59, 63,
                     7, 15, 17, 27, 33, 47, 55, 63,
                     15, 27, 33, 63,
                     27, 33,
                     33],
                 0, 0)
Kelsey = bracket("wilkels04",
                    [1, 3, 5, 7, 10, 11, 14, 15, 17, 20, 22, 23, 26, 27, 29, 31, 33, 35, 37, 39, 41, 44, 46, 47, 49, 51, 54, 56, 58, 59, 62, 63,
                     1, 5, 11, 15, 17, 23, 27, 31, 33, 39, 41, 46, 49, 54, 59, 63,
                     1, 15, 23, 31, 33, 41, 49, 59,
                     1, 31, 33, 59,
                     1, 33,
                     1],
                 0, 0)
Greg_2 = bracket("Mascot Battles",
                    [1, 4, 6, 8, 9, 12, 13, 16, 17, 19, 21, 24, 25, 28, 29, 32, 34, 36, 37, 39, 41, 43, 45, 48, 50, 51, 53, 55, 58, 59, 62, 63,
                     1, 8, 9, 13, 17, 24, 28, 32, 34, 39, 43, 48, 51, 55, 59, 63,
                     8, 9, 17, 28, 34, 48, 55, 63,
                     9, 28, 48, 63,
                     9, 48,
                     48],
                 0, 0)
Zack = bracket("ZackTheBaker",
                    [1, 4, 5, 7, 10, 11, 14, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 46, 47, 49, 51, 53, 55, 57, 59, 62, 63,
                     1, 5, 11, 15, 17, 21, 27, 31, 33, 37, 41, 47, 49, 55, 59, 63,
                     1, 11, 17, 27, 33, 47, 49, 63,
                     1, 27, 47, 52,
                     1, 47,
                     47],
                 0, 0)
Steve = bracket("Steve M.",
              [1, 4, 5, 7, 10, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 36, 37, 39, 41, 43, 46, 47, 49, 52, 53, 55, 57, 59, 62, 63,
               1, 7, 10, 15, 17, 23, 27, 31, 33, 37, 41, 47, 49, 55, 59, 63,
               1, 10, 17, 27, 33, 47, 49, 59,
               1, 27, 47, 49,
               1, 47,
               47],
              0, 0)
cubsfan = bracket("cubsfan",
              [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 26, 27, 30, 31, 33, 35, 37, 39, 41, 43, 46, 47, 49, 52, 54, 55, 57, 59, 61, 63,
               1, 5, 11, 15, 17, 23, 27, 31, 33, 37, 43, 47, 49, 55, 59, 63,
               1, 15, 23, 31, 33, 43, 49, 59,
               1, 31, 33, 49,
               1, 33,
               1],
              0, 0)
Andy = bracket("Andy P.",
              [1, 3, 5, 7, 9, 11, 14, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 46, 47, 49, 52, 53, 55, 57, 59, 62, 63,
               1, 7, 11, 15, 17, 21, 27, 29, 33, 39, 43, 47, 49, 55, 59, 63,
               1, 15, 17, 27, 33, 47, 49, 63,
               1, 17, 33, 63,
               1, 33,
               1],
              0, 0)
Allen_1 = bracket("Pull The Goalie",
              [1, 4, 6, 7, 10, 11, 14, 15, 17, 20, 21, 23, 25, 27, 30, 31, 33, 36, 37, 39, 42, 43, 46, 47, 49, 52, 53, 55, 57, 59, 62, 63,
               1, 7, 11, 15, 17, 23, 27, 31, 33, 37, 43, 47, 49, 55, 59, 63,
               1, 11, 23, 27, 33, 47, 49, 59,
               1, 23, 47, 59,
               23, 47,
               47],
              0, 0)
Allen_2 = bracket("Victorious Secret",
                  [1, 4, 5, 7, 10, 11, 14, 15, 17, 20, 22, 23, 26, 27, 30, 31, 33, 36, 37, 39, 41, 43, 46, 47, 49, 51, 53, 55, 57, 59, 62, 63,
                   1, 5, 11, 15, 17, 23, 27, 31, 33, 39, 43, 47, 49, 53, 59, 63,
                   1, 11, 17, 27, 33, 43, 49, 59,
                   11, 27, 43, 59,
                   27, 59,
                   59],
                  0, 0)
Harry = bracket("Harry Wysockey",
              [1, 4, 6, 7, 9, 11, 14, 15, 17, 20, 21, 23, 25, 27, 30, 31, 33, 35, 37, 39, 42, 43, 45, 47, 49, 52, 53, 55, 58, 59, 61, 63,
               1, 7, 9, 15, 17, 23, 25, 31, 33, 37, 42, 47, 49, 55, 59, 63,
               7, 15, 23, 31, 33, 47, 49, 59,
               15, 23, 33, 59,
               15, 59,
               59],
              0, 0)
John = bracket("Nothin but Net",
              [1, 3, 5, 7, 10, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49, 51, 54, 55, 57, 59, 61, 63,
               1, 5, 11, 15, 17, 23, 27, 31, 33, 37, 43, 47, 49, 55, 59, 63,
               1, 15, 17, 31, 33, 47, 49, 63,
               15, 17, 47, 63,
               17, 47,
               47],
              0, 0)
Tim = bracket("Krysta's Bracket",
              [1, 3, 5, 7, 9, 11, 13, 15, 17, 20, 22, 23, 26, 27, 29, 31, 33, 36, 37, 39, 42, 43, 46, 47, 49, 51, 53, 55, 58, 59, 62, 63,
               1, 7, 9, 15, 17, 23, 28, 31, 33, 39, 43, 47, 49, 53, 59, 63,
               1, 15, 17, 31, 33, 47, 49, 59,
               15, 17, 33, 63,
               17, 63,
               17],
              0, 0)
Grave_diggers = bracket("Team Grave Diggers",
              [1, 4, 5, 7, 9, 11, 13, 15, 17, 20, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49, 51, 53, 55, 57, 59, 61, 63,
               1, 5, 11, 15, 17, 23, 27, 31, 33, 39, 43, 47, 49, 55, 59, 63,
               1, 15, 17, 27, 33, 47, 49, 63,
               1, 17, 47, 49,
               17, 49,
               49],
              0, 0)
Team_Inventory = bracket("Team Inventory",
              [1, 4, 5, 7, 9, 11, 14, 15, 17, 20, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49, 52, 53, 55, 57, 59, 62, 63,
               1, 5, 11, 15, 17, 23, 27, 31, 33, 39, 43, 47, 49, 55, 59, 63,
               1, 11, 17, 27, 33, 47, 49, 59,
               11, 17, 47, 59,
               17, 59,
               59],
              0, 0)
auditor_1 = bracket("The Auditor (Mr. Mike)",
              [1, 4, 5, 7, 9, 11, 13, 15, 17, 20, 21, 23, 25, 27, 29, 31, 33, 36, 37, 39, 41, 43, 45, 47, 49, 52, 53, 56, 57, 59, 62, 63,
               4, 7, 9, 15, 17, 23, 27, 31, 33, 39, 41, 47, 49, 53, 57, 63,
               7, 15, 17, 27, 33, 47, 53, 63,
               15, 17, 47, 63,
               15, 63,
               63],
              0, 0)
auditor_2 = bracket("The Auditor (Mr. Mark)",
              [1, 4, 5, 7, 9, 12, 14, 15, 17, 20, 21, 23, 25, 27, 30, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49, 51, 53, 55, 57, 59, 62, 63,
               1, 5, 9, 15, 17, 21, 27, 31, 33, 37, 41, 47, 49, 53, 59, 63,
               1, 15, 21, 27, 37, 47, 49, 63,
               15, 21, 47, 49,
               15, 49,
               15],
              0, 0)
Maurice = bracket("Mighty Sharks",
              [1, 3, 6, 7, 9, 11, 14, 15, 17, 20, 21, 23, 25, 27, 29, 31, 33, 36, 37, 39, 41, 43, 46, 47, 49, 51, 53, 55, 58, 59, 62, 63,
               1, 6, 11, 15, 17, 23, 27, 31, 33, 39, 43, 47, 49, 55, 59, 63,
               1, 15, 17, 31, 33, 47, 49, 59,
               1, 17, 47, 49,
               1, 49,
               49],
              0, 0)
Tim_2 = bracket("Chalk Bracket",
              [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49, 51, 53, 55, 57, 59, 61, 63,
               1, 7, 11, 15, 17, 23, 27, 31, 33, 39, 43, 47, 49, 55, 59, 63,
               1, 15, 17, 31, 33, 47, 49, 63,
               1, 17, 33, 49,
               1, 33,
               1],
              0, 0)
Beau = bracket("Beau",
              [1, 3, 5, 7, 10, 11, 14, 15, 17, 20, 21, 23, 25, 27, 30, 31, 33, 36, 37, 39, 41, 43, 46, 47, 49, 52, 53, 56, 58, 59, 62, 63,
               1, 7, 10, 15, 17, 21, 27, 31, 33, 37, 43, 47, 49, 53, 59, 63,
               1, 15, 21, 31, 33, 43, 49, 59,
               1, 21, 33, 59,
               21, 33,
               33],
              0, 0)
Livy = bracket("Livy Wysockey",
              [1, 3, 5, 7, 9, 11, 14, 15, 17, 20, 21, 23, 25, 27, 30, 31, 33, 36, 37, 39, 41, 43, 46, 47, 49, 52, 53, 55, 58, 59, 62, 63,
               1, 7, 11, 15, 17, 21, 27, 31, 33, 37, 43, 47, 49, 53, 59, 63,
               7, 15, 17, 27, 33, 43, 49, 59,
               7, 27, 33, 59,
               27, 59,
               27],
              0, 0)
Suzy = bracket("suzy",
              [1, 3, 5, 7, 10, 11, 14, 15, 17, 20, 21, 23, 26, 27, 30, 31, 33, 36, 37, 39, 41, 43, 46, 47, 49, 52, 53, 55, 58, 59, 62, 63,
               1, 5, 11, 15, 17, 23, 27, 31, 33, 37, 41, 47, 49, 53, 59, 63,
               5, 11, 17, 31, 33, 47, 49, 63,
               11, 17, 33, 63,
               17, 33,
               17],
              0, 0)
MHW = bracket("Michael",
              [1, 4, 5, 7, 10, 11, 14, 15, 17, 19, 21, 23, 26, 27, 30, 31, 33, 36, 37, 39, 41, 43, 46, 47, 49, 51, 54, 55, 58, 59, 62, 63,
               1, 7, 11, 15, 17, 23, 27, 31, 33, 37, 43, 47, 49, 55, 59, 63,
               1, 11, 23, 27, 33, 43, 49, 59,
               1, 23, 33, 59,
               1, 59,
               59],
              0, 0)

pool = [Rob_1, Rob_2, Rob_3, Sam, Deb, Cooper_kids, Kyle_and_Greg, Kyle, Team_Tim, Barb, Don, Ben, Gary, Jason,
        Mrs_Outlaw, Mr_Outlaw, Chris, Fanny_1, Fanny_2, Brandon_1, Brandon_2, Jean, Greg_1, Kelsey, Greg_2, Zack,
        Steve, cubsfan, Andy, Allen_1, Allen_2, Harry, John, Tim, Grave_diggers, Team_Inventory, auditor_1, auditor_2,
        Maurice, Tim_2, Beau, Livy, Suzy, MHW]



standings = checkprint(master, pool)
for i in range(len(standings)): print(standings[i])



