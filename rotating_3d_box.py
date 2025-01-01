import os, math, time

class window:
    def __init__(self, sizeX, sizeY):
        os.system('clear')
        self.sizeX = sizeX
        self.sizeY = sizeY
        self.darknesses = "█$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,^`'"[::-1]
        self.state = [['.' for x in range(sizeX)] for x in range(sizeY)]
    
    def draw(self):
        os.system('clear')
        for i in range(len(self.state)-1, -1, -1):
            print("".join(self.state[i]))
    
    def drawPolygon(self, coords, color):
        #[[20.0, 3.29], [18.84, 4.64], [21.54, 3.91], 138]
        lines = [(coords[0],coords[1]),(coords[1],coords[2]),(coords[0],coords[2])]
        for pair in lines:
            try:
                if pair[0][0]-pair[1][0]>(pair[0][1]-pair[1][1]):
                    m = (pair[0][1]-pair[1][1])/(pair[0][0]-pair[1][0])

                    xpoints = sorted([round(pair[0][0])*2,round(pair[1][0])*2])
                    for x in (y/2 for y in range(*xpoints)):
                        y = m*(x-pair[0][0])+pair[0][1]
                        self.plot(int(x),int(y))
                else:
                    m = (pair[0][0]-pair[1][0])/(pair[0][1]-pair[1][1])

                    ypoints = sorted([round(pair[0][1])*2,round(pair[1][1])*2])
                    for y in (z/2 for z in range(*ypoints)):
                        x = m*(y-pair[0][1])+pair[0][0]
                        self.plot(int(x),int(y))
            except:
                pass

    def plot(self,x,y):
        if y<=0 or x<=0:
            return False
        y = -y
        try:
            self.state[y][x] = '█'
        except:
            pass

    def lerpDarkness(self, num):
        return self.darknesses[int((num/257)*67)]

    def reset(self):
        self.state = [['.' for x in range(self.sizeX)] for x in range(self.sizeY)]


class vec3d:
    def __init__(self, x=0, y=0, z=0, w=1):
        self.x = x
        self.y = y
        self.z = z
        self.w = w


class triangle:
    def __init__(self, v1=vec3d(), v2=vec3d(), v3=vec3d(), colour=[255, 255, 255]):
        self.coords = [v1, v2, v3]
        self.colour = colour

    def cartesian(self):
        return [
            [self.coords[0].x, self.coords[0].y],
            [self.coords[1].x, self.coords[1].y],
            [self.coords[2].x, self.coords[2].y],
        ]


class mesh:
    def __init__(self):
        self.tris = []


class mat4x4:
    def __init__(self):
        self.mat = [[0, 0, 0, 0] for x in range(4)]


def transformTrianglePoints(triangleToTransform, matrix):
    triToMap = triangle()
    triToMap.coords[0] = multiplyMatVec(triangleToTransform.coords[0], matrix)
    triToMap.coords[1] = multiplyMatVec(triangleToTransform.coords[1], matrix)
    triToMap.coords[2] = multiplyMatVec(triangleToTransform.coords[2], matrix)
    return triToMap


def multiplyTriangleByMatrix(triangleToMultiply, matrix):
    newTri = triangle()
    newTri.coords[0] = multiplyMatVec(triangleToMultiply.coords[0], matrix)
    newTri.coords[1] = multiplyMatVec(triangleToMultiply.coords[1], matrix)
    newTri.coords[2] = multiplyMatVec(triangleToMultiply.coords[2], matrix)
    return newTri


def vectorSubtract(point1, point2):
    newLine = vec3d()
    newLine.x = point1.x - point2.x
    newLine.y = point1.y - point2.y
    newLine.z = point1.z - point2.z
    return newLine


def vectorDivide(v1, k):
    v1.x /= k
    v1.y /= k
    v1.z /= k
    return v1


def normaliseVector(vec1, vec2):
    normalisedVector = vec3d()
    normalisedVector.x = vec1.y * vec2.z - vec1.z * vec2.y
    normalisedVector.y = vec1.z * vec2.x - vec1.x * vec2.z
    normalisedVector.z = vec1.x * vec2.y - vec1.y * vec2.x
    return normalisedVector


def multiplyMatVec(vec, matObj):
    outputVec = vec3d(0, 0, 0, 0)
    x, y, z, w = vec.x, vec.y, vec.z, vec.w
    outputVec.x = (
        x * matObj.mat[0][0]
        + y * matObj.mat[1][0]
        + z * matObj.mat[2][0]
        + w * matObj.mat[3][0]
    )
    outputVec.y = (
        x * matObj.mat[0][1]
        + y * matObj.mat[1][1]
        + z * matObj.mat[2][1]
        + w * matObj.mat[3][1]
    )
    outputVec.z = (
        x * matObj.mat[0][2]
        + y * matObj.mat[1][2]
        + z * matObj.mat[2][2]
        + w * matObj.mat[3][2]
    )
    outputVec.w = (
        x * matObj.mat[0][3]
        + y * matObj.mat[1][3]
        + z * matObj.mat[2][3]
        + w * matObj.mat[3][3]
    )

    return outputVec


def matrixMatrixMultiplication(m1, m2):
    outputMatrix = mat4x4()
    for row in range(4):
        for col in range(4):
            for el in range(4):
                outputMatrix.mat[row][col] += m1.mat[row][el] * m2.mat[el][col]
    return outputMatrix


def dotProduct(v1, v2):
    return v1.x * v2.x + v1.y * v2.y + v1.z * v2.z


def vectorLength(v):
    return math.sqrt(dotProduct(v, v))


def normaliseVector(v):
    l = max(vectorLength(v), 0.1)
    v.x /= l
    v.y /= l
    v.z /= l
    return v


def crossProduct(v1, v2):
    v = vec3d
    v.x = v1.y * v2.z - v1.z * v2.y
    v.y = v1.z * v2.x - v1.x * v2.z
    v.z = v1.x * v2.y - v1.y * v2.x
    return v


def makeIdentityMatrix():
    matrix = mat4x4()
    matrix.mat[0][0] = 1
    matrix.mat[1][1] = 1
    matrix.mat[2][2] = 1
    matrix.mat[3][3] = 1
    return matrix


def makeRotationMatrix_X(theta):
    matRotX = mat4x4()
    matRotX.mat[0][0] = 1
    matRotX.mat[1][1] = math.cos(theta * 0.5)
    matRotX.mat[1][2] = math.sin(theta * 0.5)
    matRotX.mat[2][1] = -math.sin(theta * 0.5)
    matRotX.mat[2][2] = math.cos(theta * 0.5)
    matRotX.mat[3][3] = 1
    return matRotX


def makeRotationMatrix_Y(theta):
    matRotY = mat4x4()
    matRotY.mat[0][0] = math.cos(theta)
    matRotY.mat[0][2] = math.sin(theta)
    matRotY.mat[2][0] = -math.sin(theta)
    matRotY.mat[1][1] = 1
    matRotY.mat[2][2] = math.cos(theta)
    matRotY.mat[3][3] = 1
    return matRotY


def makeRotationMatrix_Z(theta):
    matRotZ = mat4x4()
    matRotZ.mat[0][0] = math.cos(theta)
    matRotZ.mat[0][1] = math.sin(theta)
    matRotZ.mat[1][0] = -math.sin(theta)
    matRotZ.mat[1][1] = math.cos(theta)
    matRotZ.mat[2][2] = 1
    matRotZ.mat[3][3] = 1
    return matRotZ


def makeTranslationMatrix(x, y, z):
    matrix = mat4x4()
    matrix.mat[0][0] = 1
    matrix.mat[1][1] = 1
    matrix.mat[2][2] = 1
    matrix.mat[3][3] = 1
    matrix.mat[3][0] = x
    matrix.mat[3][1] = y
    matrix.mat[3][2] = z
    return matrix


def makeProjectionMatrix(aspectRatio, fovRad, far, near):
    matProj = mat4x4()
    matProj.mat[0][0] = aspectRatio * fovRad
    matProj.mat[1][1] = fovRad
    matProj.mat[2][2] = far / (far - near)
    matProj.mat[3][2] = (-far * near) / (far - near)
    matProj.mat[2][3] = 1
    matProj.mat[3][3] = 0
    return matProj


def importMesh(fName):
    tempMesh = mesh()
    verticies = []
    trisTemp = []

    f = open(fName, "r")
    for line in f:
        if line[0] == "v":
            verticies.append([float(x) for x in line.split(" ")[1:]])
        elif line[0] == "f":
            trisTemp.append(
                triangle(*[vec3d(*verticies[int(x) - 1]) for x in line.split(" ")[1:]])
            )

    tempMesh.tris = trisTemp
    return tempMesh


def onUserCreate():
    meshCube.tris = [
        triangle(vec3d(0, 0, 0), vec3d(0, 1, 0), vec3d(1, 1, 0)),
        triangle(vec3d(0, 0, 0), vec3d(1, 1, 0), vec3d(1, 0, 0)),
        triangle(vec3d(1, 0, 0), vec3d(1, 1, 0), vec3d(1, 1, 1)),
        triangle(vec3d(1, 0, 0), vec3d(1, 1, 1), vec3d(1, 0, 1)),
        triangle(vec3d(1, 0, 1), vec3d(1, 1, 1), vec3d(0, 1, 1)),
        triangle(vec3d(1, 0, 1), vec3d(0, 1, 1), vec3d(0, 0, 1)),
        triangle(vec3d(0, 0, 1), vec3d(0, 1, 1), vec3d(0, 1, 0)),
        triangle(vec3d(0, 0, 1), vec3d(0, 1, 0), vec3d(0, 0, 0)),
        triangle(vec3d(0, 1, 0), vec3d(0, 1, 1), vec3d(1, 1, 1)),
        triangle(vec3d(0, 1, 0), vec3d(1, 1, 1), vec3d(1, 1, 0)),
        triangle(vec3d(1, 0, 1), vec3d(0, 0, 1), vec3d(0, 0, 0)),
        triangle(vec3d(1, 0, 1), vec3d(0, 0, 0), vec3d(1, 0, 0)),
        # roof
    ]


def buildTri(tri, worldMatrix, matProj, trisToRasterize):
    triProjected, triTransformed = triangle(), triangle()
    triTransformed = transformTrianglePoints(tri, worldMatrix)

    line1 = vectorSubtract(triTransformed.coords[1], triTransformed.coords[0])
    line2 = vectorSubtract(triTransformed.coords[2], triTransformed.coords[0])

    normal = crossProduct(line1, line2)
    normal = normaliseVector(normal)

    cameraRay = vectorSubtract(triTransformed.coords[0], camera)
    if dotProduct(normal, cameraRay) < 0:
        lightDir = vec3d(0, 0, -1)
        lightDir = normaliseVector(lightDir)

        lightApathy = max(0.001, dotProduct(lightDir, normal))
        tempColour = [math.trunc(x * lightApathy) for x in tri.colour]
        triProjected = transformTrianglePoints(triTransformed, matProj)
        triProjected.colour = tempColour
        trisToRasterize.append(triProjected)

        triProjected.coords[0] = vectorDivide(
            triProjected.coords[0], triProjected.coords[0].w
        )
        triProjected.coords[1] = vectorDivide(
            triProjected.coords[1], triProjected.coords[1].w
        )
        triProjected.coords[2] = vectorDivide(
            triProjected.coords[2], triProjected.coords[2].w
        )


def onUserUpdate():
    screen.reset()

    near = 0.1
    far = 1000
    fov = 90
    aspectRatio = height / width
    fovRad = 1 / math.tan(fov * 0.5 / 180 * 3.14159)
    matProj = makeProjectionMatrix(aspectRatio, fovRad, far, near)

    global theta
    # theta += 0.015

    matRotZ = makeRotationMatrix_Z(20)
    matRotX = makeRotationMatrix_X(20)
    matRotY = makeRotationMatrix_Y(theta)

    translationMatrix = makeTranslationMatrix(0, 0, 2)
    worldMatrix = makeIdentityMatrix()
    worldMatrix = matrixMatrixMultiplication(matRotY, matRotX)
    worldMatrix = matrixMatrixMultiplication(worldMatrix, translationMatrix)

    importedMesh = meshCube
    trisToRasterize = []

    for tri in importedMesh.tris:
        target = buildTri(tri, worldMatrix, matProj, trisToRasterize)

    # ----------------------------------------------------------------
    trisToRasterize.sort(key=lambda tri: tri.coords[1].z, reverse=True)

    x = 1
    length = len(trisToRasterize)
    for tri in trisToRasterize:
        cartesianCoords = tri.cartesian()
        cartesianCoords = [
            [(x[0] + 1) * 0.5 * width, (x[1] + 1) * 0.5 * height]
            for x in cartesianCoords
        ]

        x += 1
        screen.drawPolygon(cartesianCoords, tri.colour)

width = 135
height = 45
screen = window(width, height)
screen.draw()

meshCube = mesh()
camera = vec3d()

theta = 1
agg = 0

onUserCreate()
shouldRun = True
while shouldRun:
    time.sleep(0.1)
    onUserUpdate()
    screen.draw()
    agg += 1
    theta += 0.1

