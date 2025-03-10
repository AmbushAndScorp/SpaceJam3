from direct.showbase.ShowBase import ShowBase
from direct.showbase.Loader import *
from panda3d.core import NodePath
from panda3d.core import Vec3

class Universe (ShowBase):
    def __init__(self, loader: Loader, modelPath: str, parentNode: NodePath, nodeName: str, texPath: str, scaleVec: float):
        self.modelNode = loader.loadModel(modelPath)
        self.modelNode.reparentTo(parentNode)
        self.modelNode.setScale(scaleVec)
        self.modelNode.setName(nodeName)
        self.modelNode.setPos(0,0,0)
        tex = loader.loadTexture(texPath)
        self.modelNode.setTexture(tex, 1)