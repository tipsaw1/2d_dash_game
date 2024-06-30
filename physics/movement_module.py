import math

class Movement:
  def AngledVelocity(angle, distance):
    dx = distance * math.cos(angle)
    dy = distance*math.cos(angle)
    return (dx, dy)