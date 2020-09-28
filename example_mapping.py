import time
from Controller import UDP_Controller

if __name__ == '__main__':

    _controller = UDP_Controller()
    _controller.addVariable("inputs", "byte", 0)
    _controller.addVariable("outputs", "byte", 0)
    _controller.start()

    H01 = H02 = H03 = False
    
    while True:

        [_, _, _, _, _, S03, S02, S01] = _controller.getMappedValue("inputs")
        H01 = S01
        H02 = not S03 and S02
        H03 = S03 or S02
        _controller.setMappedValue("outputs", [_, _, _, _, _, H03, H02, H01])
        
        time.sleep(1e-5)
