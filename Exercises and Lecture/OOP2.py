import time

class Rocket:

    def __init__(self, stages=[], payload=None):
        self.stages = stages
        self.payload = payload

        self.situation = 'LANDED'
        self.activeStage = 0
        self.height = 0
    
    def launch(self, countdown=0):
        print('NEW MISSON: {}'. format(self.payload.name.upper()))

        self.activeStage = 0

        if self.stages[self.activeStage].thrust > self.getMass():
            print('LIFTOFF IN...')
            for i in range(countdown, 0, -1):
                print(i)
                time.sleep(1)
            print('Successful Liftoff. Rocket currently has mass of {} tons and is producing a thrust of {} kN.'.format(self.getMass(), self.stages[self.activeStage].getThrust()))
            self.situation = 'FLYING'

            time.sleep(3)
            self.burnStage(self.stages[self.activeStage]) # go a distance
        else:
            print('Failure - insufficient thrust!')

    def stageSep(self):
        self.activeStage += 1
        print('Stage {} Burnout. Current Mass is {} tons'.format(self.activeStage, self.getMass()))
        time.sleep(1)
        print('STAND BY FOR STAGE SEPARATION...')

        if len(self.stages) > self.activeStage:
            print('Rocket is now in stage {} burn with thrust of {} KN.'.format(self.activeStage + 1, self.stages[self.activeStage].getThrust()))
            time.sleep(3)
            self.burnStage(self.stages[self.activeStage]) # go a distance
        else:
            print('Payload is now in a parabolic trajectory of {} KM'.format(self.height))


    def burnStage(self, stage):
        self.height += stage.dV
        self.stageSep()
        
        

    def getMass(self):
        n = 0
        for i in range(len(self.stages)):
            if i >= self.activeStage:
                n += self.stages[i].mass
        return n + self.payload.mass

class Stage:
    def __init__(self, fuel=0, mass=0, thrust = 0):
        self.mass = mass
        self.fuel = fuel
        self.thrust = thrust
        self.dV = 50
    
    def getThrust(self):
        return self.thrust if self.fuel > 0 else 0 # only thrust if stage has thrust

class Payload:
    def __init__(self, name='', mass=0):
        self.name = name
        self.mass = mass
    def deploy(self):
        print('Deployment of {} successful!'.format(self.name))
        

if __name__ == "__main__":
    r = Rocket([Stage(100, 150, 500), Stage(50, 70, 200), Stage(20, 30, 100)], Payload('K1 Sounding Probe', 5))
    r.launch(5)
