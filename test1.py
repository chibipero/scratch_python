from mcpi.minecraft import Minecraft
from time import sleep
mc = Minecraft.create()
y = 0
for i in range(10):
    mc.setBlock(0, y, 0, 41)
    sleep(0.5)
    y = y + 1