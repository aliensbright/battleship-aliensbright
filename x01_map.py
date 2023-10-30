#! python3

"""
* Take a list of coordinates and draw a map showing occupied squares
* The map is a 10x10 grid
* (0,0) is the coordinate in the bottom left (like a regular (x,y) grid system)

```
Sample Data1:
"""
#occupied = [[1, 1], [2, 1], [4, 0], [5, 0], [6, 0], [0, 1], [0, 2], [0, 3], [1, 8], [2, 8], [3, 8], [4, 8], [4, 3], [4, 4], [4, 5], [4, 6], [4, 7]]
"""
Suggested Output:
..........
.xxxx.....
....x.....
....x.....
....x.....
....x.....
x...x.....
x.........
xxx.......
....xxx...

Sample Data2:
"""
#occupied=[[0, 0], [1, 0], [8, 6], [8, 7], [8, 8], [7, 5], [7, 6], [7, 7], [1, 1], [1, 2], [1, 3], [1, 4], [0, 6], [1, 6], [2, 6], [3, 6], [4, 6]]
"""
..........
........x.
.......xx.
xxxxx..xx.
.......x..
.x........
.x........
.x........
.x........
xx........
```
"""
#List of variables: occupied, map1, Coords(), ocCoord, x, y, xycoord, a, b, m, i 

occupied = [[1, 1], [2, 1], [4, 0], [5, 0], [6, 0], [0, 1], [0, 2], [0, 3], [1, 8], [2, 8], [3, 8], [4, 8], [4, 3], [4, 4], [4, 5], [4, 6], [4, 7]]


map1=['..........','..........','..........','..........','..........','..........','..........','..........','..........','..........']

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