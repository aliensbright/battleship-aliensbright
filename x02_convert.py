#!python3
"""
Given a string literal convert it to a list that contains the coordinate. Your string literal should be able to remove whitespace and work with both lower and upper case values. "B3", "b3" , "B 3" and "b 3" should all correspond to the list item [1,2]
"""

def convertLet(letter):
  letList=('a','b','c','d','e','f','g','h','i','k')
  for i in range(10):
    if letter==letList[i]:
      return i

def convert(coordinate):
  """
  input: coordinate is a string literal 
    examples: "B 3" "B3" "b3"
  return value: list containing 2 integers
  """
  q = coordinate.replace(' ','')
  if len(q)>3 or len(q)<0:
    return None
  q = q.lower()
  let = q[0]

  if len(q)==3: #Number
    num=int(q[1]+q[2])-1
  else:
    num=int(q[1])-1

  let = convertLet(let)
  
  coordNumNum = [let,num]
  print(coordNumNum)
  return coordNumNum

'''
coordsLetNum = str(input('Coords: letter, number:'))
convert(coordsLetNum)
'''
if __name__ == "__main__":
  assert convert("B3") == [1,2]
  assert convert("A10") == [0,9]
  assert convert("d 4") == [3,3]
  


