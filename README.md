# python-controller
This library allows communicating with controller using the UDP driver through the Gateway.

# How to use it

'''
import time
from Controller import UDP_Controller

if __name__ == '__main__':

    _controller = UDP_Controller()
    _controller.addVariable("inputs", "byte", 0)
    _controller.addVariable("outputs", "byte", 0)
    _controller.start()

    while True:

        value = _controller.getValue("inputs")
        _controller.setValue("outputs", value)
        
        time.sleep(1e-5)
'''
