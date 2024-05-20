class BouncingBall:
    debug = True

    # default constructor
    def __init__(self, v):
        self.velocity0 = v
        self.bounce = 0
        self.velocityN = v
        self.height = 0
        # Control Logic to simmulate flight and bounce.
        while self.bounce <= 5:
            if self.velocityN > 0:
                self.height += self.velocityN
                self.velocityN -= 32
            else:
                self.height += self.velocityN
                self.velocityN -= 32

            if self.debug:
                print(f"Velocity: {self.velocityN}, Height: {self.height}")
            
            if self.height < 0:
                self.height = self.height * -0.5
                self.velocityN = self.velocityN * -0.5
                self.bounce += 1
                if self.debug:
                    print(f"Bounce: {self.bounce}, Height after bounce: {self.height}, Velocity after bounce: {self.velocityN}")
            # on height change print velocity and height.
    
Ball100 = BouncingBall(100)
