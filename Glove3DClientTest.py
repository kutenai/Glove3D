# TCP client example
import socket
import time
socket1 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
socket1.setblocking(2)

pos = [0,0,2.5]
hpr = [270,0,0]
poslist = []

idx = 0

def send(idx,pos,hpr,dly):
    pVal = [idx]+pos+hpr
    s = ",".join([str(x) for x in pVal])
    socket1.sendto(s, ("127.0.0.1",5432))
    time.sleep(dly)


def tapFinger(idx):
    dly = 0.01
    step = 2
    for x in range(0,3):
        for theta in range(-40,40,step):
            pos[0] = 5
            pos[1] = idx*0.7
            pos[2] = 0
            hpr[0] = -90
            hpr[1] = theta
            hpr[2] = 0
            send(idx,pos,hpr,dly)
        for theta in range(40,-40,-step):
            pos[0] = 5
            pos[1] = idx*0.7
            pos[2] = 0
            hpr[0] = -90
            hpr[1] = theta
            hpr[2] = 0
            send(idx,pos,hpr,dly)
    for theta in range(-40,0,step):
        pos[0] = 5
        pos[1] = idx*0.7
        pos[2] = 0
        hpr[0] = -90
        hpr[1] = theta
        hpr[2] = 0
        send(idx,pos,hpr,dly)

def waveHand():
    idx = 0
    dly = 0.01
    step = 2
    for x in range(0,3):
        for theta in range(-40,40,step):
            pos[0] = 0
            pos[1] = 0
            pos[2] = 2
            hpr[0] = 0
            hpr[1] = 0
            hpr[2] = theta
            send(idx,pos,hpr,dly)
        for theta in range(40,-40,-step):
            pos[0] = 0
            pos[1] = 0
            pos[2] = 2
            hpr[0] = 0
            hpr[1] = 0
            hpr[2] = theta
            send(idx,pos,hpr,dly)

    for theta in range(-40,0,step):
        pos[0] = 0
        pos[1] = 0
        pos[2] = 2
        hpr[0] = 0
        hpr[1] = 0
        hpr[2] = theta
        send(idx,pos,hpr,dly)

def test(idx):
    for z in range(-10,11,1):
        pos[0] = 5
        pos[1] = idx*0.7
        pos[2] = z/10.0
        pVal = [idx]+pos+hpr
        s = ",".join([str(x) for x in pVal])
        socket1.sendto(s, ("127.0.0.1",5432))
        time.sleep(0.1)

    # Put it back to normall.
    pVal = [idx]+[5,(idx)*0.7,0]+[-90,0,0]
    s = ",".join([str(x) for x in pVal])
    socket1.sendto(s, ("127.0.0.1",5432))


waveHand()
#tapFinger(0)
