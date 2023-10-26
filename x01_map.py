#! python3

"""
* Take a list of coordinates and draw a map showing occupied squares
* The map is a 10x10 grid
* (0,0) is the coordinate in the bottom left (like a regular (x,y) grid system)

```
Sample Data1:
[[1, 1], [2, 1], [4, 0], [5, 0], [6, 0], [0, 1], [0, 2], [0, 3], [1, 8], [2, 8], [3, 8], [4, 8], [4, 3], [4, 4], [4, 5], [4, 6], [4, 7]]

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
occupied=[[0, 0], [1, 0], [8, 6], [8, 7], [8, 8], [7, 5], [7, 6], [7, 7], [1, 1], [1, 2], [1, 3], [1, 4], [0, 6], [1, 6], [2, 6], [3, 6], [4, 6]]
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
n=0
m=0
#occupied = [[1, 1], [2, 1], [4, 0], [5, 0], [6, 0], [0, 1], [0, 2], [0, 3], [1, 8], [2, 8], [3, 8], [4, 8], [4, 3], [4, 4], [4, 5], [4, 6], [4, 7]]
def Gameboard():
    map1=['..........','..........','..........','..........','..........','..........','..........','..........','..........','..........']
    x=(i[m])
    y=(i[m+1])
    z=map1[y].replace('.','x',(x+1))
    z=z.replace('x','.',(x))
    map1[y]=z
def mapping():
    print(map1)
for i in occupied:
    Gameboard()
mapping()