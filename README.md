

# PyTorch Tensor Operations Module

This module provides a set of functions to perform operations on PyTorch 2-dimensional tensors.

You can install the associated module using the following command in on your Conda environment

**pip install git+https://github.com/jaimelhd/module_structure1.git@v1.0.0
**
You can use the The -U option to update an already installed package to the latest available version.

And after you install it, you need to go to python and import the module. If you want to use the tensor operator project use this command:

**import tensor_operator
**
## Functions

- `zeros_tensor()`: Returns an all-zeros tensor of the specified shape.
- `ones_tensor()`: Returns an all-ones tensor of the specified shape.
- `random_tensor()`: Returns a tensor with random values of the specified shape.
- `add_tensors(tensor1, tensor2)`: Returns the sum of two tensors.
- `multiply_tensors(tensor1, tensor2)`: Returns the multiplication of two tensors.
- `tensor_transpose(tensor)`: Returns the transpose of a tensor.
- `tensor_dot_product(tensor1, tensor2)`: Returns the dot product of two tensors.
- `tensor_mean(tensor)`: Returns the mean of a tensor.
- `tensor_max(tensor)`: Returns the maximum value in a tensor.
- `tensor_min(tensor)`: Returns the minimum value in a tensor.

## Usage

First, initialize the class with the desired shape:


tensor_ops = TensorOperations((3, 3))


Then, you can use the functions like this:

```
# Create a zeros tensor
zeros = tensor_ops.zeros_tensor()

# Create a ones tensor
ones = tensor_ops.ones_tensor()

# Create a random tensor
random = tensor_ops.random_tensor()

# Add two tensors
added = tensor_ops.add_tensors(zeros, ones)

# Multiply two tensors
multiplied = tensor_ops.multiply_tensors(ones, random)

# Transpose a tensor
transposed = tensor_ops.tensor_transpose(random)

# Dot product of two tensors
dot_product = tensor_ops.tensor_dot_product(ones, random)

# Mean of a tensor
mean = tensor_ops.tensor_mean(random)

# Max of a tensor
max_value = tensor_ops.tensor_max(random)

# Min of a tensor
min_value = tensor_ops.tensor_min(random)
```

## Installation

This module requires PyTorch. You can install it using pip:

**pip install torch**

