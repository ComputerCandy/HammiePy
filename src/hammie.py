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
