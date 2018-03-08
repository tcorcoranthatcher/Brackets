import operator

master = [1, 4, 5, 8, 10, 11, 13, 15, 17, 19, 22, 23, 26, 27, 30, 31, 33, 36, 37, 39, 41, 44, 45, 47, 49, 52, 54, 55,
          58, 59, 62, 64, 1, 5, 11, 15, 17, 23, 27, 31, 33, 37, 41, 45, 49, 55, 58, 62, 1, 15, 17, 31, 0, 0, 0, 0, 0, 0,
          0, 0, 0, 0, 0]


class bracket:
    def __init__(self, name, bracket, points, wins, chances):
        self.name = name
        self.bracket = bracket
        self.points = points
        self.wins = wins
        self.chances = float(wins / 32768)


def check(master, check):
    for i in range(1, 64):
        if i <= 32:
            if master[i - 1] == check.bracket[i - 1]:
                check.points += 1
        if i > 32 and i <= 48:
            if master[i - 1] == check.bracket[i - 1]:
                check.points += 2
        if i > 48 and i <= 56:
            if master[i - 1] == check.bracket[i - 1]:
                check.points += 4
        if i > 56 and i <= 60:
            if master[i - 1] == check.bracket[i - 1]:
                check.points += 8
        if i > 60 and i <= 62:
            if master[i - 1] == check.bracket[i - 1]:
                check.points += 16
        if i > 62 and i <= 63:
            if master[i - 1] == check.bracket[i - 1]:
                check.points += 32
    return (check.name, check.points)


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
Krysta, Don, Barb, Darci, Noel, Violet, Tommy, Rebecca, John, Gary, Beau, Ben, Harry, Michael, Anna, Andy, Zack, Kyle,
Deb, Kelsey, Jason, Jim, Maurice, Greg, Humbert, Steve, Tim, Brandon, Joanne, Jean, Griffin)


def iterator():
    iterator_dict = {}
    for i in range(2048, 4096):
        holder = []
        binary_conversion = bin(i)
        string_conversion = str(binary_conversion)
        for j in range(3, 14):
            if string_conversion[j] == "1":
                int_conversion = 1
            else:
                int_conversion = 0
            holder.append(int_conversion)
        iterator_dict[i - 2047] = holder

    return iterator_dict


def chances(iterator_dict, master, pool):
    # UPDATE FOR J IN RANGE
    for i in range(1, 2049):
        # 129
        master_change = master
        elite_eight_dict = {1: 1, 2: 15, 3: 17, 4: 31}
        final_four_dict = {}
        champ_game_dict = {}
        for j in range(11):
            if j == 0:
                if iterator_dict[i][j] == 0:
                    master_change[52 + j] = 33
                    elite_eight_dict[5] = 33
                else:
                    master_change[52 + j] = 37
                    elite_eight_dict[5] = 37
            if j == 1:
                if iterator_dict[i][j] == 0:
                    master_change[52 + j] = 41
                    elite_eight_dict[6] = 41
                else:
                    master_change[52 + j] = 45
                    elite_eight_dict[6] = 45
            if j == 2:
                if iterator_dict[i][j] == 0:
                    master_change[52 + j] = 49
                    elite_eight_dict[7] = 49
                else:
                    master_change[52 + j] = 55
                    elite_eight_dict[7] = 55
            if j == 3:
                if iterator_dict[i][j] == 0:
                    master_change[52 + j] = 58
                    elite_eight_dict[8] = 58
                else:
                    master_change[52 + j] = 62
                    elite_eight_dict[8] = 62
            if j == 4:
                if iterator_dict[i][j] == 0:
                    master_change[52 + j] = elite_eight_dict[1]
                    final_four_dict[1] = elite_eight_dict[1]
                else:
                    master_change[52 + j] = elite_eight_dict[2]
                    final_four_dict[1] = elite_eight_dict[2]
            if j == 5:
                if iterator_dict[i][j] == 0:
                    master_change[52 + j] = elite_eight_dict[3]
                    final_four_dict[2] = elite_eight_dict[3]
                else:
                    master_change[52 + j] = elite_eight_dict[4]
                    final_four_dict[2] = elite_eight_dict[4]
            if j == 6:
                if iterator_dict[i][j] == 0:
                    master_change[52 + j] = elite_eight_dict[5]
                    final_four_dict[3] = elite_eight_dict[5]
                else:
                    master_change[52 + j] = elite_eight_dict[6]
                    final_four_dict[3] = elite_eight_dict[6]
            if j == 7:
                if iterator_dict[i][j] == 0:
                    master_change[52 + j] = elite_eight_dict[7]
                    final_four_dict[4] = elite_eight_dict[7]
                else:
                    master_change[52 + j] = elite_eight_dict[8]
                    final_four_dict[4] = elite_eight_dict[8]
            if j == 8:
                if iterator_dict[i][j] == 0:
                    master_change[52 + j] = final_four_dict[1]
                    champ_game_dict[1] = final_four_dict[1]
                else:
                    master_change[52 + j] = final_four_dict[2]
                    champ_game_dict[1] = final_four_dict[2]
            if j == 9:
                if iterator_dict[i][j] == 0:
                    master_change[52 + j] = final_four_dict[3]
                    champ_game_dict[2] = final_four_dict[3]
                else:
                    master_change[52 + j] = final_four_dict[4]
                    champ_game_dict[2] = final_four_dict[4]
            if j == 10:
                if iterator_dict[i][j] == 0:
                    master_change[52 + j] = champ_game_dict[1]
                else:
                    master_change[52 + j] = champ_game_dict[2]
        iteration_outcome = checkprint(master_change, pool)
        for k in range(31):
            if pool[k].name == iteration_outcome[0][0]:
                pool[k].wins += 1
        for l in range(1, 31):
            if iteration_outcome[l][1] == iteration_outcome[0][1]:
                for m in range(31):
                    if pool[m].name == iteration_outcome[l][0]:
                        pool[m].wins += 1

    print("Krysta has a " + str(Krysta.wins) + "chance to win")
    print("Don has a " + str(Don.wins) + " chance to win")
    print("Barb has a " + str(Barb.wins) + " chance to win")
    print("Darci has a " + str(Darci.wins) + " chance to win")
    print("Noel has a " + str(Noel.wins) + " chance to win")
    print("Violet has a " + str(Violet.wins) + " chance to win")
    print("Tommy has a " + str(Tommy.wins) + " chance to win")
    print("Rebecca has a " + str(Rebecca.wins) + " chance to win")
    print("John has a " + str(John.wins) + " chance to win")
    print("Gary has a " + str(Gary.wins) + " chance to win")
    print("Beau has a " + str(Beau.wins) + " chance to win")
    print("Ben has a " + str(Ben.wins) + " chance to win")
    print("Harry has a " + str(Harry.wins) + " chance to win")
    print("Michael has a " + str(Michael.wins) + " chance to win")
    print("Anna has a " + str(Anna.wins) + " chance to win")
    print("Andy has a " + str(Andy.wins) + " chance to win")
    print("Zack has a " + str(Zack.wins) + " chance to win")
    print("Kyle has a " + str(Kyle.wins) + " chance to win")
    print("Deb has a " + str(Deb.wins) + " chance to win")
    print("Kelsey has a " + str(Kelsey.wins) + " chance to win")
    print("Jason has a " + str(Jason.wins) + " chance to win")
    print("Jim has a " + str(Jim.wins) + " chance to win")
    print("Maurice has a " + str(Maurice.wins) + " chance to win")
    print("Greg has a " + str(Greg.wins) + " chance to win")
    print("Humbert has a " + str(Humbert.wins) + " chance to win")
    print("Steve has a " + str(Steve.wins) + " chance to win")
    print("Tim has a " + str(Tim.wins) + " chance to win")
    print("Brandon has a " + str(Brandon.wins) + " chance to win")
    print("Joanne has a " + str(Joanne.wins) + " chance to win")
    print("Jean has a " + str(Jean.wins) + " chance to win")
    print("Griffin has a " + str(Griffin.wins) + " chance to win")


iteration = iterator()
chances(iteration, master, pool)

print(checkprint(master, pool))
print(iteration)
