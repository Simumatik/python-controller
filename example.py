import time
from Controller import UDP_Controller
import logging

if __name__ == '__main__':

    _controller = UDP_Controller(log_lever=logging.DEBUG)
    _controller.addVariable("inputs", "byte", 0)
    _controller.addVariable("outputs", "byte", 0)
    _controller.start()

    while True:

        value = _controller.getValue("inputs")
        _controller.setValue("outputs", value)
        
        time.sleep(1e-5)
