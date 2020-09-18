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

        # You can  handle the inputs, and manipulate the outputs
        # Example: connect out_0 directly to in_0
        outputs[0] = inputs[0]

        # We can invert in_1 and output to out_1
        outputs[1] = not inputs[1]

        # If both in_0 and in_1 are active, activate out_2
        if inputs[0] and inputs[1]:
            outputs[2] = 1

        updateOutputs()
        print("I: " + str(inputs) + " O: " + str(outputs), end="\r")
        time.sleep(1e-5)
        