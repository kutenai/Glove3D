#!/usr/bin/env python


#Importing math constants and functions
#from direct.stdpy import threading
#from direct.stdpy import socket
import socket

# Thread class that executes processing
class SocketListener(threading.Thread):
    """Worker Thread Class."""
    def __init__(self, destClass):
        """Init Worker Thread Class."""
        print("Initing the thread")
        threading.Thread.__init__(self)
        self.destClass = destClass
        print("Done..")
        # This starts the thread running on creation, but you could
        # also make the GUI thread responsible for calling this
        self.start()

    def run(self):
        """Run Worker Thread."""
        # This is the code executing in the new thread. Simulation of
        # a long process (well, 10s here) as a simple loop - you will
        # need to structure your processing so that you periodically
        # peek at the abort variable
        print("Opening the socket")
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_socket.bind(("", 5010))
        server_socket.listen(5)

        print ("Client Socket Setup")

        while 1:
            client_socket, address = server_socket.accept()
            print "I got a connection from ", address
            data = client_socket.recv(512)
            while data:
                cmdFound = False
                m = re.search("pos (\d+)",data,re.IGNORECASE)
                if m:
                    pos = int(m.group(1))
                    #wx.PostEvent(self._notify_window,PositionEvent(pos) )
                    #print ("Updated Position to %d" % pos)
                    destClass.notifyPos(pos)
                    cmdFound = True
                m = re.search("load \"(.*)\"", data, re.IGNORECASE)
                if m:
                    # Re-load a new file
                    #wx.PostEvent(self._notify_window,LoadEvent(m.group(1)))
                    cmdFound = True

                if re.search("play",data,re.IGNORECASE):
                    #wx.PostEvent(self._notify_window,ControlEvent(2) )
                    print("Play Video")
                    cmdFound = True
                elif re.search("pause",data,re.IGNORECASE):
                    #wx.PostEvent(self._notify_window,ControlEvent(1) )
                    print("Pause Video")
                    cmdFound = True
                elif re.search("stop",data,re.IGNORECASE):
                    #wx.PostEvent(self._notify_window,ControlEvent(0) )
                    print("Stop Video")
                    cmdFound = True

                if not cmdFound:
                    print("Unknown Command:%s" % data)

                data = client_socket.recv(512)
