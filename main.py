import serial
import GSVconvert
import GSVcommands
from time import sleep

def getUserScale(Channel):
    serialConnection.write(GSVcommands.ReadUserScale(Channel))
    AnswFrame = serialConnection.read(8)
    UserScale = GSVconvert.bytesTofloat(AnswFrame[3:7])
    return UserScale

def setUserScale(Channel, UserScale):
    serialConnection.write(GSVcommands.WriteUserScale(Channel, UserScale))
    AnswFrame = serialConnection.read(4)
    print("AnswFrame: ", AnswFrame.hex())

def SetZero(Channel):
    serialConnection.write(GSVcommands.SetZero(Channel))
    AnswFrame = serialConnection.read(4)
    print("AnswFrame: ", AnswFrame.hex())

def getMeasValues():
    serialConnection.write(GSVcommands.GetValue())
    MeasFrame = serialConnection.read(36)
    MeasValues = MeasFrameToMeasValues(MeasFrame)
    return MeasValues

def MeasFrameToMeasValues(MeasFrame):
    MeasValues = []
    for i in range(8):
        MeasValues.append(GSVconvert.bytesTofloat(MeasFrame[i*4+3:i*4+7]))
    return MeasValues


if __name__ == '__main__':

    serialConnection = serial.Serial("COM8", 230400, timeout=1)
    serialConnection.isOpen()

    serialConnection.write(GSVcommands.StopTransmission())
    sleep(0.1)
    serialConnection.reset_input_buffer()

    print("MeasValues: ", getMeasValues())
    sleep(0.1)
    SetZero(Channel=1) # SetZero channel 1
    sleep(0.1)
    print("MeasValues: ", getMeasValues())
    sleep(0.1)
    SetZero(Channel=0) # SetZero all channels
    sleep(0.1)
    print("MeasValues: ", getMeasValues())


    setUserScale(Channel=2, UserScale=2.0)
    print("UserScale - channel 2: ", getUserScale(Channel=2))
    setUserScale(Channel=2, UserScale=1.0)
    print("UserScale - channel 2: ", getUserScale(Channel=2))

    serialConnection.close()


