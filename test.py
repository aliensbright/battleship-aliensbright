

map1=['..........','..........','..........','..........','..........','..........','..........','..........','..........','..........']
occupied=[[0, 0], [1, 0], [8, 6], [8, 7], [8, 8], [7, 5], [7, 6], [7, 7], [1, 1], [1, 2], [1, 3], [1, 4], [0, 6], [1, 6], [2, 6], [3, 6], [4, 6]]
occupied.sort(reverse=True)
print(occupied)
def Coords(ocCoord):
    x=(ocCoord[0])+1
    y=(ocCoord[1])*(-1)+9
    xycoord = [x,y]
    return xycoord

def Gameboard(a,b):
    #a is the x value (row)
    #b is the y value (column)
    map1[b] = map1[b].replace('.','x',a)
    map1[b] = map1[b].replace('x','.',(a-1))
    return map1[b]


for m in occupied:
    x = Coords(m)[0] #the row
    y = Coords(m)[1] #the column
    map1[y] = Gameboard(x,y)

for i in map1:
    print(i)