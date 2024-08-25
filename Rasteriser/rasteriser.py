import pygame as renderer, math, time
renderer.init()

width = 500
height = 500
screen = renderer.display.set_mode([width, height], renderer.NOFRAME)
renderer.display.set_caption("Rendering 'Cube'")
renderer.display.flip()

class vec3d:
  def __init__(self,x=0,y=0,z=0):
    self.x = x
    self.y = y
    self.z = z

class triangle:
  def __init__(self,v1=0,v2=0,v3=0,colour=[255,255,255]):
    self.coords = [v1, v2, v3]
    self.colour = colour
  
  def cartesian(self):
    return [
    [self.coords[0].x,self.coords[0].y],
    [self.coords[1].x,self.coords[1].y],
    [self.coords[2].x,self.coords[2].y]]


class mesh:
  def __init__(self):
      self.tris = []

class mat4x4:
  def __init__(self):
    self.mat = [[0,0,0,0] for x in range(4)]

def multiplyMatVec(vec, matObj):
  outputVec = vec3d(0,0,0)
  x, y, z = vec.x, vec.y, vec.z
  outputVec.x = x*matObj.mat[0][0] + y*matObj.mat[1][0] + z*matObj.mat[2][0] + matObj.mat[3][0]
  outputVec.y = x*matObj.mat[0][1] + y*matObj.mat[1][1] + z*matObj.mat[2][1] + matObj.mat[3][1]
  outputVec.z = x*matObj.mat[0][2] + y*matObj.mat[1][2] + z*matObj.mat[2][2] + matObj.mat[3][2]
  w = x*matObj.mat[0][3] + y*matObj.mat[1][3] + z*matObj.mat[2][3] + matObj.mat[3][3]
  
  if w!=0:
      outputVec.x, outputVec.y, outputVec.z = outputVec.x/w, outputVec.y/w, outputVec.z/w

  return outputVec

def importMesh(fName):
  tempMesh = mesh()
  verticies = []
  trisTemp = []

  f = open(fName, 'r')
  for line in f:
    if line[0] == "v":
      verticies.append([float(x) for x in line.split(" ")[1:]])
    elif line[0] == "f":
      trisTemp.append(triangle(*[vec3d(*verticies[int(x)-1]) for x in line.split(" ")[1:]]))
  
  tempMesh.tris = trisTemp
  return tempMesh

def onUserCreate():
  meshCube.tris= [
      triangle(vec3d(0,0,0),vec3d(0,1,0),vec3d(1,1,0)),
      triangle(vec3d(0,0,0),vec3d(1,1,0),vec3d(1,0,0)),

      triangle(vec3d(1,0,0),vec3d(1,1,0),vec3d(1,1,1)),
      triangle(vec3d(1,0,0),vec3d(1,1,1),vec3d(1,0,1)),

      triangle(vec3d(1,0,1),vec3d(1,1,1),vec3d(0,1,1)),
      triangle(vec3d(1,0,1),vec3d(0,1,1),vec3d(0,0,1)),

      triangle(vec3d(0,0,1),vec3d(0,1,1),vec3d(0,1,0)),
      triangle(vec3d(0,0,1),vec3d(0,1,0),vec3d(0,0,0)),

      triangle(vec3d(0,1,0),vec3d(0,1,1),vec3d(1,1,1)),
      triangle(vec3d(0,1,0),vec3d(1,1,1),vec3d(1,1,0)),

      triangle(vec3d(1,0,1),vec3d(0,0,1),vec3d(0,0,0)),
      triangle(vec3d(1,0,1),vec3d(0,0,0),vec3d(1,0,0)),

      #roof
      triangle(vec3d(0,0,1),vec3d(0.5,0,2),vec3d(0.5,1,2),[140,25,180]),
      triangle(vec3d(0,0,1),vec3d(0.5,1,2),vec3d(0,1,1),[140,25,180]),
      triangle(vec3d(0.5,1,2),vec3d(0.5,0,2),vec3d(1,1,1),[140,25,180]),
      triangle(vec3d(0.5,0,2),vec3d(1,0,1),vec3d(1,1,1),[140,25,180]),
      triangle(vec3d(1,0,1),vec3d(0.5,0,2),vec3d(0,0,1),[140,25,180]),
      triangle(vec3d(0,1,1),vec3d(0.5,1,2),vec3d(1,1,1),[140,25,180]),
  ]

  near = 0.1
  far = 1000
  fov = 90
  aspectRatio = height/width
  fovRad = 1/math.tan(fov*0.5/180*3.14159)

  matProj.mat[0][0] = aspectRatio*fovRad
  matProj.mat[1][1] = fovRad
  matProj.mat[2][2] = far/(far-near)
  matProj.mat[3][2] = (-far*near)/(far-near)
  matProj.mat[2][3] = 1

def getTriangleSideCoords(triangle, point1, point2):
  newLine = vec3d()
  newLine.x = triangle.coords[point1].x - triangle.coords[point2].x
  newLine.y = triangle.coords[point1].y - triangle.coords[point2].y
  newLine.z = triangle.coords[point1].z - triangle.coords[point2].z
  return newLine

def multiplyTriangleByMatrix(triangleToMultiply, matrix):
  newTri = triangle()
  newTri.coords[0] = multiplyMatVec(triangleToMultiply.coords[0], matrix)
  newTri.coords[1] = multiplyMatVec(triangleToMultiply.coords[1], matrix)
  newTri.coords[2] = multiplyMatVec(triangleToMultiply.coords[2], matrix)
  return newTri

def transformTrianglePoints(triToMap, triangleToTransform, matrix):
  triToMap.coords[0] = multiplyMatVec(triangleToTransform.coords[0], matrix)
  triToMap.coords[1] = multiplyMatVec(triangleToTransform.coords[1], matrix)
  triToMap.coords[2] = multiplyMatVec(triangleToTransform.coords[2], matrix)

def onUserUpdate():
  screen.fill((25, 25, 25))
  
  global theta
  theta += 0.01

  matRotZ = mat4x4()
  matRotZ.mat[0][0] = math.cos(theta)
  matRotZ.mat[0][1] = math.sin(theta)
  matRotZ.mat[1][0] = -math.sin(theta)
  matRotZ.mat[1][1] = math.cos(theta)
  matRotZ.mat[2][2] = 1
  matRotZ.mat[3][3] = 1

  matRotX = mat4x4()
  matRotX.mat[0][0] = 1
  matRotX.mat[1][1] = math.cos(theta * 0.5)
  matRotX.mat[1][2] = math.sin(theta * 0.5)
  matRotX.mat[2][1] = -math.sin(theta * 0.5)
  matRotX.mat[2][2] = math.cos(theta * 0.5)
  matRotX.mat[3][3] = 1

  ship = importMesh("ship.obj")
  trisToRasterize = []
  for tri in ship.tris:
    triProjected, triRotatedZ, triRotatedZX = triangle(), triangle(), triangle()

    triRotatedZ = multiplyTriangleByMatrix(tri, matRotZ)
    triRotatedZX = multiplyTriangleByMatrix(triRotatedZ, matRotX)

    triTranslated = triangle(*triRotatedZX.coords)
    triTranslated.coords[0].z += 8
    triTranslated.coords[1].z += 8
    triTranslated.coords[2].z += 8

    normal, line1, line2 = vec3d(), vec3d(), vec3d()
    line1 = getTriangleSideCoords(triTranslated, 1, 0)
    line2 = getTriangleSideCoords(triTranslated, 2, 0)

    normal.x = line1.y * line2.z - line1.z * line2.y
    normal.y = line1.z * line2.x - line1.x * line2.z
    normal.z = line1.x * line2.y - line1.y * line2.x

    l = math.sqrt(normal.x*normal.x + normal.y*normal.y + normal.z*normal.z)
    if l!=0:
        normal.x/=l
        normal.y/=l
        normal.z/=l

    if (normal.x * (triTranslated.coords[0].x - camera.x) + 
        normal.y * (triTranslated.coords[0].y - camera.y) + 
        normal.z * (triTranslated.coords[0].z - camera.z)) < 0:

      lightDir = vec3d(0,0,-1)
      l2 = math.sqrt(lightDir.x**2 + lightDir.y**2 + lightDir.z**2)
      lightDir.x/=l2
      lightDir.y/=l2
      lightDir.z/=l2
          

      lightApathy =  (normal.x * (lightDir.x - camera.x) + 
                      normal.y * (lightDir.y - camera.y) + 
                      normal.z * (lightDir.z - camera.z))
          
      tempColour = [abs(x*lightApathy) for x in tri.colour]

      transformTrianglePoints(triProjected, triTranslated, matProj)
      triProjected.colour = tempColour
      trisToRasterize.append(triProjected)

  trisToRasterize.sort(key=lambda tri:tri.coords[1].z, reverse=True)
  for tri in trisToRasterize:
    cartesianCoords = tri.cartesian()
    cartesianCoords = [[(x[0]+1) * 0.5 * width,(x[1]+1) * 0.5 * height] for x in cartesianCoords]
    renderer.draw.polygon(screen, tri.colour, cartesianCoords, 0)
      


meshCube = mesh()
matProj = mat4x4()
camera = vec3d()
  
theta = 1
onUserCreate()
shouldRun = True
while shouldRun:
  for event in renderer.event.get():
    if event.type == renderer.QUIT:
      shouldRun = False
  onUserUpdate()
  renderer.display.flip()
  
  time.sleep(0.0)

renderer.quit()
