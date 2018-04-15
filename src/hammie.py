import socket

class Hammie:

    def __init__(self,ip = "192.168.4.1", port = 6000, debug=False):
        self.s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.to = (ip, port)
        self.debug = debug

    def sendRawNR(self, msg): #no response
        self.s.sendto(msg.encode(), self.to)
        if(self.debug):
            print "Out: " + msg

    def sendRaw(self, msg):
        x = ""
        self.s.sendto(msg.encode(), self.to)
        if(self.debug):
            print "Out:" + msg
        while True:
            data = self.s.recv(4096)
            if not data:
                break
            x = x + repr(data)
        if(self.debug):
            print "In: " + msg
        return x
    def close(self):
        self.s.close()

        #End Raw Commands, Begin User Methods

    def SetState(self, Port, Pin, State):
        msg = Port + str(Pin) + " " + ("1" if State == True else "0")
        msg = msg.lower()
        self.sendRawNR(msg)

    def Toggle(self, Port, Pin):
        msg = Port + "tg " + str(Pin)
        msg = msg.lower()
        self.sendRawNR(msg)
    def TurnOn(self, Port, Pin):
        self.SetState(Port,Pin,True)

    def TurnOff(self, Port, Pin):
        self.SetState(Port,Pin,False)

    def AllOn(self, Port):
        msg = Port + "on"
        msg = msg.lower()
        self.sendRawNR(msg)

    def AllOff(self, Port):
        msg = Port + "off"
        msg = msg.lower()
        self.sendRawNR(msg)

    def AllToggle(self, Port):
        msg = Port + "tga"
        msg = msg.lower()
        self.sendRawNR(msg)

    def GetPinState(self, Port, Pin):
        msg = "get " + Port + str(Pin)
        msg = msg.lower()
        return self.sendRaw(msg).split(" ")[1]

    def GetAllPinStates(self, Port):
        msg = "gall " + Port
        msg = msg.lower()
        return self.sendRaw(msg).split(" ")[1:]

    def GetAnalogValue(self, Port, Pin):
        msg = "adr " + Port + str(Pin)
        msg = msg.lower()
        return self.sendRaw(msg).split(" ")[1]

    def GetAnalogVoltage(self, Port, Pin):
        msg = "adv " + Port + str(Pin)
        msg = msg.lower()
        return self.sendRaw(msg).split(" ")[1]

    def GetAnalogAverage(self, Port, Pin, PeriodMS):
        msg = "ada " + Port + str(Pin) + " " + str(PeriodMS)
        msg = msg.lower()
        return self.sendRaw(msg).split(" ")[1]

    def ServoPositon(self, Port, Pin, Position):
        msg = "svp " + Port + str(Pin) + " " + str(Position)
        msg = msg.lower()
        self.sendRawNR(msg)

    def ServoSweep(self, Port, Pin, Position, Delay):
        msg = "svs " + Port + str(Pin) + " " + str(Position) + " " + str(Delay)
        msg = msg.lower()
        self.sendRawNR(msg)

    def ServoPositonToggle(self, Port, Pin, Position1, Position2):
        msg = "svt " + Port + str(Pin) + " " + str(Position1) + " " + str(Position2)
        msg = msg.lower()
        self.sendRawNR(msg)

    def PWMSignal(self, Port, Pin, DutyPercentage):
        msg = "pwm " + Port + str(Pin) + " " + str(DutyPercentage)
        msg = msg.lower()
        self.sendRawNR(msg)

    def Faster(self):
        self.sendRawNR("faster")

    def Slower(self):
        self.sendRawNR("slower")

    def Stop(self):
        self.sendRawNR("stop")

    def SetLRMotorSpeed(self, speed):
        self.sendRawNR("bms " + str(speed))

    def SetLMotorSpeed(self, speed):
        self.sendRawNR("lms " + str(speed))

    def SetRMotorSpeed(self, speed):
        self.sendRawNR("rms " + str(speed))

    def SetLRMotorSpeed(self, leftSpeed, rightSpeed):
        self.sendRawNR("sms " + str(leftSpeed) + " " + str(rightSpeed))

    def SetLRMotorThreshold(self, speed):
        self.sendRawNR("bmt " + str(speed))

    def SetLMotorSpeed(self, speed):
        self.sendRawNR("lmt " + str(speed))

    def SetRMotorSpeed(self, speed):
        self.sendRawNR("rmt " + str(speed))

    def SpeedStep(self, speedStep):
        self.sendRawNR("ssv " + str(speedStep))

    def Left(self):
        self.sendRawNR("left")

    def Straight(self):
        self.sendRawNR("straight")

    def Right(self):
        self.sendRawNR("right")

    def Turn(self,angle):
        self.sendRawNR("turn" + str((angle / 1.8) - 50))

    def SteeringUrgency(self, Step):
        self.sendRawNR("stur " + str(speedStep))

    def RecenterTime(self, time):
        self.sendRawNR("stdtt " + str(time))
