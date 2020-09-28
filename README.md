# python-controller
This library allows communicating with a controller component using the UDP driver through the Gateway.

# How to use it

First you will need to clone this repository or copy Controller.py file to your computer.

Create an instance of UDP_Controller and then add the variables that you have used in the controller component.

    from Controller import UDP_Controller
    _controller = UDP_Controller()
    _controller.addVariable("inputs", "byte", 0)
    _controller.addVariable("outputs", "byte", 0)

Once the stup is completed you should call 'start()' to enable the controller.

    _controller.start()

Program your logic and call 'getValue(*variable_name*)' to obtain the latest value received from the controller component, and 'setValue()' to modify the value on the controller component.

    value = _controller.getValue("inputs")
    _controller.setValue("outputs", 12)


You can automatically map bit values of discrete datatypes using 'getMappedValue(*variable_name*)' or 'setMappedValue()' respectivelly.
Note that mapping is done following standard order [MSB...LSB]:

    [in_7, in_6, in_5, in_4, in_3, in_2, in_1, in_0] = _controller.getMappedValue("inputs")
    _controller.setMappedValue("outputs", [out_7, out_6, out_5, out_4, out_3, out_2, out_1, out_0])


## Simple example code (see example.py):

The next example code sets the 'inputs' value to the 'outputs' value:

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

## Example code with mapping (see example_mapping.py):

The next example code activates the output signals one after each other:

    import time
    from Controller import UDP_Controller

    if __name__ == '__main__':

        _controller = UDP_Controller()
        _controller.addVariable("inputs", "byte", 0)
        _controller.addVariable("outputs", "byte", 0)
        _controller.start()
        
        while True:

            [_, _, _, _, _, S03, S02, S01] = _controller.getMappedValue("inputs")
            H01 = S01
            H02 = not S01 and S02
            H03 = S03 or S02
            _controller.setMappedValue("outputs", [_, _, _, _, _, H03, H02, H01])
            
            time.sleep(2e-1)
