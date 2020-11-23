import numpy as np

class SoftMax:

    def __init__(self):
        pass

    def forward(self, input_tensor):
        self.input_tensor = input_tensor
        input_tensor = np.exp(input_tensor - np.max(input_tensor))
        # the_sum = np.exp(input_tensor).sum()
        self.output_tensor = input_tensor / input_tensor.sum()
        return self.output_tensor

    def backward(self, error_tensor):
        locsum = error_tensor * self.output_tensor
        locsum = locsum.sum()
        return self.output_tensor * (error_tensor - locsum)