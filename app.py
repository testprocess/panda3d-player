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

        myModel = self.loader.loadModel("./models/objects/box.gltf")
        myModel.reparentTo(self.render)
        myModel.setPos(6,70,8)


        myFog = Fog("Fog Name")
        myFog.setColor(5, 5, 5)
        myFog.setExpDensity(0.4574)
        self.render.setFog(myFog)

        # terrain = GeoMipTerrain("mySimpleTerrain")
        # terrain.setHeightfield("heightField.png")
        # #terrain.setBruteforce(True)
        # terrain.getRoot().reparentTo(self.render)
        # terrain.generate()

        dlight = DirectionalLight('my dlight')
        dlnp = self.render.attachNewNode(dlight)

        self.accept("escape", sys.exit)



app = App()
app.run()