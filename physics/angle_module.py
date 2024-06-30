import math
class Angles:
  def GetAngle(point1, point2, degrees = False):
    result = math.atan2(point2[1]-point1[1], point2[0]-point1[0])
    if degrees:
      result *= 180/math.pi
    return result
  
  
    
    
