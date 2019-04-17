import lighton
import projectHalf2
from socket import *
from time import ctime
import time

lighton.setUP()

ctrCmd = ['UP','DOWN','VIEW']
message="hello world"
HOST = '192.168.43.96'
PORT = 5555

BUFSIZE = 1024
ADDR = (HOST,PORT)

tcpSerSock = socket(AF_INET, SOCK_STREAM)
tcpSerSock.bind(ADDR)
tcpSerSock.listen(5)

        
while True:
        tcpCliSock,addr = tcpSerSock.accept()
        
        time.sleep(.05)
        data = ''
        data = tcpCliSock.recv(BUFSIZE).decode()
        
        
        print(data)
        
        if not data:
                print("there is no data")
                break
        
        if data == ctrCmd[0]:
        	lighton.ledOn()
        
        if data == ctrCmd[1]:
                lighton.ledOff()
        
        if data == ctrCmd[2]:
                lighton.ledOn()
                #Sends string back
                TCPCliSock.send("Your String".encode()) #Please reaplace Your string with The required text (NOTE:use str() if data is not string)

        	

        
        	
                
tcpCliSock.close();





