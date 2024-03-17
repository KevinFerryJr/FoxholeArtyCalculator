import math

# Dist to GUN
DistGun = 10
# Dist to TARGET
DistTarg = 10
# Angle to GUN
AngleGun = 90
# Angle to Target
AngleTarg = 0
# Horizantal Adjustment
HorizAdjust = 1

def lawOfCos(distA,distB,distC):
    resA = distB**2 - (distC**2 + distA**2)
    resB = 2 * distC * distA
    cosB = resA / resB
    angleB = math.degrees(math.acos(cosB))
    #print(f"Firing Azim: {angleB}")
    return angleB
    
def calculateLegs(hypotenuse, slope):
    # Calculate the angle in radians using the arctangent (inverse tangent) of the slope
    angle_rad = math.atan(slope)
    
    # Calculate the lengths of sides using trigonometric functions
    side_a = hypotenuse * math.cos(angle_rad)  # Adjacent side
    side_b = hypotenuse * math.sin(angle_rad)  # Opposite side
    
    return side_a, side_b

def calculateDistance(angleC, distA, distB):
    distSquared = distA**2 + distB**2 - 2*distA*distB* math.cos(angleC)
    distC = math.sqrt(distSquared)
    #print(f"Firing Distance: {distC}")
    return distC

def calculateAngle(angle1, angle2):
    angle = abs(math.radians(angle1 - angle2))
    #print(f"Spotter Angle: {math.degrees(angle)}")
    return angle

def adjustSolution(firingAzim, firingDist, adjHoriz):
    # Calculate the tangent of the original angle to determine the slope of the tangent line
    firingAzimRad = math.radians(firingAzim)
    secant = 1 / math.cos(firingAzimRad)
    cosecant = 1 / math.sin(firingAzimRad)
    slope = secant / cosecant
    
    #print(f"Slope of tan({firingAzim}): {slope}")
    
    sideA, sideB = calculateLegs(adjHoriz, slope)
    #print(f"sideA: {sideA}")
    #print(f"sideB: {sideB}")
    
    cos = math.cos(firingAzimRad)
    sin = math.sin(firingAzimRad)
 
    #print(f"cos: {cos}")
    #print(f"sin: {sin}")
    
    if(adjHoriz >= 0):  # ADJUST RIGHT
        adjustedX = ((cos * firingDist)+abs(sideA))
        adjustedY = ((sin * firingDist)+abs(sideB))
    else:               # ADJUST LEFT
        adjustedX = ((cos * firingDist)-abs(sideA))
        adjustedY = ((sin * firingDist)-abs(sideB))
    
    #print(f"X: {adjustedX}")
    #print(f"Y: {adjustedY}")
    
    adjustedDist = math.sqrt(adjustedX**2 + adjustedY**2)
    #print(f"Adjusted Distance: {adjustedDist}")
    
    adjustedAzimRad = math.atan2(adjustedY, adjustedX) % (2*math.pi)
    adjustedAzimDeg = math.degrees(adjustedAzimRad)
    #print(f"Adjusted Azimuth: {adjustedAzimDeg}")
    
    return adjustedDist, adjustedAzimDeg

def calculateFiringSolution(gunDist, gunAzim, targDist, targAzim, adjHoriz = 0):
    spotterAzim = calculateAngle(gunAzim,targAzim)
    #print(f"spotterAzim: {math.degrees(spotterAzim)}")
    
    firingDist = calculateDistance(spotterAzim, gunDist, targDist)
    print(f"Distance: {firingDist}")
    
    firingAzim = lawOfCos(gunDist, targDist, firingDist)
    #print(f"Firing Azim: {int(firingAzim)}")
    
    if (math.degrees(spotterAzim) > 180):
        firingAzim = 360 - firingAzim
    
    if (gunAzim > targAzim):
        firingAzim = 180 + firingAzim
    
    print(f"Azimuth: {firingAzim}")
    
    adjustedDist, adjustedAzim = adjustSolution(firingAzim, firingDist, adjHoriz)
    print(f"Adjusted Distance: {adjustedDist}")
    print(f"Adjusted Azimuth: {adjustedAzim}")
    
    return int(firingDist), int(firingAzim), int(adjustedDist), int(adjustedAzim)