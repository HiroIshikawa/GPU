import time


try:
    import smbus
    bus = smbus.SMBus(1)
    address = 0x04
except ImportError:
    print('Not importing smbus')
    pass


def writeNumber(value):
    try:
        bus.write_byte(address, value)
    except IOError:
        print('IOError happend')
        pass
    except NameError:
        print('NameError happend')
        pass


def readNumber():
    try:
        number = bus.read_byte(address)
    except IOError:
        number = -1
        pass
    except NameError:
        number = -1
        pass
    return number


def track(avg_pos):
    if avg_pos > 300:
        print("Detected at +"+str(avg_pos)+" units, Rotate Right.")
        var = 4  # rotate right
        writeNumber(var)
    elif avg_pos < -300:
        print("Detected at "+str(avg_pos)+" units, : Rotate Left.")
        var = 3  # rotate left
        writeNumber(var)
    elif avg_pos > 40:
        print("Detected at +"+str(avg_pos)+" units, Tilt Right.")
        var = 7  # tilt right
        writeNumber(var)
    elif avg_pos < -40:
        print("Detected at "+str(avg_pos)+" units, Tilt Left.")
        var = 6  # tilt left
        writeNumber(var)
    else:
        print("Detected at "+str(avg_pos)+" units, Go Straight: ")
        var = 1  # go straight
        writeNumber(var)


def monitor(avg_pos):
    if avg_pos < 150 or avg_pos > -150:
        distance = readNumber()
    else:
        distance = -1
    # print('Distance reading: '+str(distance))
    if distance > 0 and distance < 29 and not distance == 1 and not distance == 25:
        start_time = time.time()
        writeNumber(8)  # Initiate pickup motion
        while True:
            if time.time()-start_time > 1.:  #
                complete = readNumber()
                print('Complete?: '+str(complete))
                if complete==1:
                    print('Received Complete Signal From Arduino')
                    writeNumber(0)
                    time.sleep(5)
                    break
                start_time = time.time()
