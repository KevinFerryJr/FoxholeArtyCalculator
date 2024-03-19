import math

def lawOfCos(distA,distB,distC):
    resA = distB**2 - (distC**2 + distA**2)
    resB = 2 * distC * distA
    cosB = resA / resB
    angleB = math.degrees(math.acos(cosB))
    #print(f"Firing Azim: {angleB}")
    return angleB

def calculateDistance(angleC, distA, distB):
    distSquared = distA**2 + distB**2 - 2*distA*distB* math.cos(angleC)
    distC = math.sqrt(distSquared)
    #print(f"Firing Distance: {distC}")
    return round(distC, 1)

def calculateAngle(startAngle, endAngle):
    angle = abs(math.radians(startAngle - endAngle))
    #print(f"Spotter Angle: {math.degrees(angle)}")
    return angle

def addAngles(angleA, angleB):
    result = angleA + angleB
    return result

def calculateFiringAzim(gunDist, gunAzim, targDist, targAzim):
    gunX = math.cos(math.radians(gunAzim)) * gunDist
    guny = math.sin(math.radians(gunAzim)) * gunDist
    
    targX = math.cos(math.radians(targAzim)) * targDist
    targy = math.sin(math.radians(targAzim)) * targDist
    
    finalX = targX - gunX
    finalY = targy - guny
    
    finalAngleRad = math.atan(finalY/finalX)
    finalAngleDeg = math.degrees(finalAngleRad)
    
    angleTotal = addAngles(gunAzim, targAzim)
    if(angleTotal > 360):
        finalAngleDeg+= 180
    
    if(gunAzim<targAzim):
           finalAngleDeg= finalAngleDeg+180

    result = round(finalAngleDeg, 1) % 360
    return result

def calculateFiringSolution(gunDist, gunAzim, targDist, targAzim):
    spotterAngle = calculateAngle(gunAzim,targAzim)
    #print(f"spotterAzim: {math.degrees(spotterAzim)}")
    
    firingDist = calculateDistance(spotterAngle, gunDist, targDist)
    #print(f"Distance: {firingDist}")
    
    firingAzim = calculateFiringAzim(gunDist, gunAzim, targDist, targAzim)
    #print(f"Azimuth: {firingAzim}")
    
    return firingDist, firingAzim
