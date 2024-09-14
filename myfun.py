def isLeap(yy):
  if yy%400==0 or (yy%4==0 and yy%100!=0):
    return True
  else:
    return False
