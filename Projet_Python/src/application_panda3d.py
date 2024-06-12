#Panda 3D Engine
from direct.showbase.ShowBase import ShowBase
from direct.actor.Actor import Actor
from panda3d.core import AmbientLight
from panda3d.core import Vec4

# Custom module

class Panda3DApplication (ShowBase):

    def __init__ (self):
        ShowBase.__init__(self)

        #Launching Panda3D windows
        #self.run()

        #Loading scene
        self.scene = self.loader.loadModel("models/environment")
        self.scene.reparentTo(self.render)
        self.scene.setScale(0.25, 0.25, 0.25)
        self.scene.setPos(-10, 40, 0)

        #Loading 3D model
        self.pandaActor = Actor("models/panda-model",
                                {"walk" : "models/panda-walk4"})
        self.pandaActor.reparentTo(self.render)
        self.pandaActor.setScale(0.05, 0.05, 0.05)
        self.pandaActor.loop("walk")

# Temporary Main Guard
if __name__ == "__main__":
    panda3d_instance = Panda3DApplication()
    panda3d_instance.run()

