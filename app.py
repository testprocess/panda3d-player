from direct.showbase.ShowBase import ShowBase
from direct.task import Task

from panda3d.core import *
from panda3d.core import PlaneNode, Plane, Fog, DirectionalLight

from math import pi, sin, cos
import sys


class App(ShowBase):

    def __init__(self):
        ShowBase.__init__(self)

        self.scene = self.loader.loadModel("./models/scene")
        self.scene.setScale(10)
        self.scene.reparentTo(self.render)
        self.useTrackball()


        plane1 = Plane((0, 0, 1), (0, 0, 5))
        plane1_np = self.render.attachNewNode(PlaneNode("plane1", plane1))
        plane1_np.show()
        self.scene.setClipPlane(plane1_np)

        self.isMove = False
        self.modelPosition = [6,70,8]

        self.model = self.loader.loadModel("./models/objects/box.gltf")
        self.model.reparentTo(self.render)
        self.model.setScale(10)

        self.model.setPos(self.modelPosition[0], self.modelPosition[1], self.modelPosition[2])


        myFog = Fog("Fog Name")
        myFog.setColor(5, 5, 5)
        myFog.setExpDensity(0.4574)
        self.render.setFog(myFog)


        dlight = DirectionalLight('my dlight')
        dlnp = self.render.attachNewNode(dlight)

        self.accept("escape", sys.exit)
        self.accept("a", self.moveLeft)
        self.accept("a-up", self.freeze)
        self.accept("d", self.moveRight)
        self.accept("d-up", self.freeze)
        self.accept("w", self.moveForward)
        self.accept("w-up", self.freeze)
        self.accept("s", self.moveBack)
        self.accept("s-up", self.freeze)

        taskMgr.doMethodLater(1/60, self.loop, 'tickTask')


    def loop(self, task):
        self.move()
        return Task.again

    def move(self):
        speed = 4
        if (self.isMove == False):
            return 0
        
        if (self.moveType == 'left'):
            self.modelPosition[0] -= speed
        elif (self.moveType == 'right'):
            self.modelPosition[0] += speed
        elif (self.moveType == 'forward'):
            self.modelPosition[1] += speed
        elif (self.moveType == 'back'):
            self.modelPosition[1] -= speed

        self.model.setPos(self.modelPosition[0], self.modelPosition[1], self.modelPosition[2])

    def freeze(self):
        self.isMove = False
        self.moveType = 'none'


    def moveLeft(self):
        self.isMove = True
        self.moveType = 'left'


    def moveRight(self):
        self.isMove = True
        self.moveType = 'right'

    def moveForward(self):
        self.isMove = True
        self.moveType = 'forward'

    def moveBack(self):
        self.isMove = True
        self.moveType = 'back'


app = App()
app.run()