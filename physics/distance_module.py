import math

class Distance:
  def GetDistance(point1, point2):
    x_d = point2[0] - point1[0]
    y_d = point2[1] - point1[1]
    total_distance = (x_d**2 + y_d**2)**0.5
    
    return total_distance