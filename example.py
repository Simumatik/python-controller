import time
from Controller import UDP_Controller
import logging

if __name__ == '__main__':

    _controller = UDP_Controller(log_lever=logging.DEBUG)
    _controller.addVariable("inputs", "byte", 0)
    _controller.addVariable("outputs", "byte", 0)
    _controller.start()
    inputs = [0, 0, 0, 0, 0, 0, 0, 0]
    outputs = [0, 0, 0, 0, 0, 0, 0, 0]

    def updateInputs():
        input_byte = _controller.getValue("inputs")
        for i in range(8):
            inputs[i] = 1 if input_byte & (2 ** i) else 0

    def updateOutputs():
        output_byte = 0
        for i in range(8):
            output_byte += 2 ** i if outputs[i] == 1 else 0
        _controller.setValue("outputs", output_byte)

    while True:
        updateInputs()

        # Here you handle the inputs, and manipulate the outputs
        outputs = inputs

        updateOutputs()
        print("I: " + str(inputs) + " O: " + str(outputs), end="\r")
        time.sleep(1e-5)
        