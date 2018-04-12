import socket

class Hammie:

    def __init__(self,ip, port):
        self.s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.to = (ip, port)

    def sendRawNR(self, msg): #no response
        self.s.sendto(msg.encode(), self.to)

    def sendRaw(self, msg):
        x = ""
        self.s.sendto(msg.encode(), self.to)
        while True:
            data = self.s.recv(4096)
            if not data:
                break
            x = x + repr(data)
    def close(self):
        self.s.close()

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
