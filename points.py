def points(games):
    total_point = 0
    for i in range(len(games)):
        if games[i][0] > games[i][2]:
            total_point += 3
        elif games[i][0] == games[i][2]:
            total_point += 1
        else:
            total_point += 0
    return total_point
print(points(['0:1','0:2','0:3','0:4','1:2','1:3','1:4','2:3','2:4','3:4']))