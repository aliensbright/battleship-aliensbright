
m=0

map1=['..........','..........','..........','..........','..........','..........','..........','..........','..........','..........']

occupied=[[0, 0], [1, 0], [8, 6], [8, 7], [8, 8], [7, 5], [7, 6], [7, 7], [1, 1], [1, 2], [1, 3], [1, 4], [0, 6], [1, 6], [2, 6], [3, 6], [4, 6]]

def Coords(i): #Assign Coord Values to variables x and y
    x=(i[m])+1 #X is horizontal from 1-10 left to right indicating which collumn it is in.
    y=(i[m+1])*(-1)+9 #Y is vertical from 0-9 bottom to top indicating which row it is in. 
    return x,y

def Gameboard(a,b): #Use x and y coords to change a '.' to a 'x'
    n =
    return n
def main():
    for coordinates in occupied:
        Coords(coordinates)
        Gameboard(x,y)
for a in range(10):
    print(map1[a])
main()