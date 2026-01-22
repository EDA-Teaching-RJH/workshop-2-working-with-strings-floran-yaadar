import math  

def main():
#TO DO  
  A = int(input("value for side A="))
  B = int(input("Value for side B="))
  Answer = pythag(A,B)
  print(Answer)
def pythag(A,B):
#TO DO  
  As = (A ** 2)
  Bs = (B ** 2)
  d = (As + Bs)
  df = math.sqrt(d)
  return df
main()
