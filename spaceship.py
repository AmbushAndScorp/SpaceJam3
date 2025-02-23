from direct.showbase.ShowBase import ShowBase
from direct.showbase.Loader import *
from panda3d.core import NodePath
from panda3d.core import Vec3
from direct.task import Task
from direct.showbase.DirectObject import DirectObject

class Spaceship (ShowBase):
    def __init__(self, loader: Loader, modelPath: str, parentNode: NodePath, nodeName: str, texPath: str, posVec: Vec3, scaleVec: float):
        self.modelNode = loader.loadModel(modelPath)
        self.modelNode.reparentTo(parentNode)
        self.modelNode.setPos(posVec)
        self.modelNode.setScale(scaleVec)
        self.modelNode.setName(nodeName)
        tex = loader.loadTexture(texPath)
        self.modelNode.setTexture(tex, 1)
    
    def keyBinds(self):
        # all bindings for movement
        self.accept('space', Spaceship.Thrust(Spaceship, keyDown='space'), [1])
        self.accept('space-up', Spaceship.Thrust, [0])
        self.accept('arrow_left', Spaceship.LeftTurn('arrow_left'), [1])
        self.accept('arrow_left-up', Spaceship.LeftTurn, [0])
    
    def Thrust(self, keyDown):
        if keyDown:
            self.taskMgr.add(self.ApplyThrust, 'forward-thrust') 
        else:
            self.taskMgr.remove('forward-thrust')

    def ApplyThrust(self, task):
        rate = 5
        traj = self.render.getRelativeVector(self.modelNode, Vec3.forward())
        traj.normalize()
        self.modelNode.setFluidPos(self.modelNode.getPos() + traj * rate)

        return Task.cont
    
    def LeftTurn(self, keyDown):
        if keyDown:
            self.taskMgr.add(self.ApplyLeftTurn, 'turn-left')
        else:
            self.taskMgr.remove('turn-left')
    
    def ApplyLeftTurn(self, task):
        # half a degree every frame
        rate = .5
        self.modelNode.setH(self.modelNode.getH() + rate)
        return Task.cont
