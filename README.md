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


## Example code:

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

