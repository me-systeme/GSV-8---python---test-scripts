import GSVconvert

def GetValue():
    return b'\xAA\x90\x3B\x85'

def StopTransmission():
    return b'\xAA\x90\x23\x85'

def StartTransmission():
    return b'\xAA\x90\x24\x85'

def ReadUserScale(Channel):
    return b'\xAA\x91\x14' + Channel.to_bytes(1, byteorder='big') + b'\x85'

def WriteUserScale(Channel, newUserScale):
    return b'\xAA\x95\x15' + Channel.to_bytes(1, byteorder='big') + GSVconvert.floatTobytes(newUserScale) + b'\x85'

def ReadUserOffset(Channel):
    return b'\xAA\x91\x9A' + Channel.to_bytes(1, byteorder='big') + b'\x85'

def WriteUserOffset(Channel, newUserOffset):
    return b'\xAA\x95\x9B' + Channel.to_bytes(1, byteorder='big') + GSVconvert.floatTobytes(newUserOffset) + b'\x85'

def ReadDataRate():
    return b'\xAA\x90\x8A\x85'

def WriteDataRate(DataRate):
    return b'\xAA\x94\x8B' + GSVconvert.floatTobytes(DataRate) + b'\x85'

def SetZero(Channel):
    return b'\xAA\x91\x0C' + Channel.to_bytes(1, byteorder='big') + b'\x85'
