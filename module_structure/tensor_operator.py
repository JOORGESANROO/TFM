import torch

class TensorOperations:
    def __init__(self, shape):
        self.shape = shape

    def zeros_tensor(self):
        return torch.zeros(self.shape)

    def ones_tensor(self):
        return torch.ones(self.shape)

    def random_tensor(self):
        return torch.rand(self.shape)

    @staticmethod
    def add_tensors(tensor1, tensor2):
        return torch.add(tensor1, tensor2)

    @staticmethod
    def multiply_tensors(tensor1, tensor2):
        return torch.mul(tensor1, tensor2)

    @staticmethod
    def tensor_transpose(tensor):
        return torch.t(tensor)

    @staticmethod
    def tensor_dot_product(tensor1, tensor2):
        return torch.dot(tensor1.view(-1), tensor2.view(-1))

    @staticmethod
    def tensor_mean(tensor):
        return torch.mean(tensor)

    @staticmethod
    def tensor_max(tensor):
        return torch.max(tensor)

    @staticmethod
    def tensor_min(tensor):
        return torch.min(tensor)

