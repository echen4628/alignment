

class GateProtocol:
    def __init__(self):
        pass

    def fixed_depth(self):
        # CONTROLS
        # move down by a fixed amount
        pass

    def spin(self):
        # CONTROLS
        # spin around until we see the gate and stop
        # CONTROLS
        # spin to set point of the gate in the center of our vision
        # OBJECT DETECTION
        # see the gate?
        pass

    def shimmy(self):
        # DEPTH SENSING
        # find distance to center of gate
        # CONTROLS / NAVIGATION
        # begin orbit around center of gate
        # OBJECT DETECTION
        # if bounding box shrinks, change direction
        # if bounding box grows, don't worry
        pass

    def orbit(self):
        # DEPTH SENSING
        # find distance to center of gate
        # CONTROLS / NAVIGATION
        # orbit around center of gate while maintaining the gate in the center of our vision
        # OBJECT DETECTION
        # stop when the width of the gate reaches a maximum
        pass
    
    def forward(self):
        # OBJECT DETECTION
        # see the gate! remember where it starts
        # publish the set point as it is
        # continue to check where the gate is and republish the set point if neccessary
        pass