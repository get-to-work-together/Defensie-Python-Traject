from abc import ABC
from collections.abc import Callable
from functools import partial
from typing import List

import numpy as np


def derivative(f, z, eps=0.000001):
    """Determine the derivative if the formule is not available."""
    return (f(z + eps) - f(z - eps))/(2 * eps)



class ActivationFunctionBaseClass(ABC):
    title: str
    description: str
    formula: str   # markdown latex
    additional_information: str
    plot_title: str
    plot_explanation: List[str] = ''
    pros: List[str] = []
    cons: List[str] = []
    activation_function: Callable[[float], float]
    derivative_title: str
    derivative_formula: str   # markdown latex
    derivatice_plot_explanation: List[str] = []
    derivative_function: Callable[[float], float]
    notes: List[str] = []


# ======================================================================================
# Logistic

def logistic(z):
    return 1 / (1 + np.exp(-z))


def logistic_derivative(z):
    return logistic(z) * (1 - logistic(z))


class Logistic(ActivationFunctionBaseClass):

    title = 'Logistic (Sigmoid) Activation Function'

    description = 'It is a sigmoid function with a characteristic "S"-shaped curve.'

    formula = r'**$sigmoid(z)=\frac{1}{1+exp(-z)}$**'   # Markdown LATEX

    additional_information = 'The output of the logistic (sigmoid) function is always between 0 and 1.'

    plot_title = 'Logistic Function'

    plot_explanation = ['- The logistic function saturates as the inputs become larger (either positive or negative).',
                        '- For large positive and negative values, the function gets asymptotically close to 1 and 0, respectively.',
                        '- When the function saturates, its gradient becomes very close to zero, which slows down learning.']

    pros = ["1. The logistic function introduces non-linearity into the network which allows it to solve more complex problems than linear activation functions.\n2. It is continuous and differentiable everywhere.\n3. Because its output is between 0 and 1, it is very common to use in the output layer in binary classification problems."]

    cons = ["1. Limited Sensitivity\n- The logistic function saturates across most of its domain.\n- It is only sensitive to inputs around its midpoint 0.5.",
            "2. Vanishing Gradients in Deep Neural Networks\n- Because the logistic function can get easily saturated with large inputs, its gradient gets very close to zero. This causes the gradients to get smaller and smaller as backpropagation progresses down to the lower layers of the network.\n- Eventually, the lower layers' weights receive very small updates and never converge to their optimal values."]

    activation_function = logistic

    derivative_title = 'Derivative of the Logistic Function'

    derivative_formula = r'$sigmoid^{\prime}(z)=sigmoid(z)(1−sigmoid(z))$'

    derivatice_plot_explanation = ['Notice that the derivative of the logistic function gets very close to zero for large positive and negative inputs.']

    derivative_function = logistic_derivative

    notes = []

# ======================================================================================
# Tanh


def tanh(z):
    return np.tanh(z)


def tanh_derivative(z):
    return 1 - tanh(z) ** 2


class Tanh(ActivationFunctionBaseClass):

    title = 'Hyperbolic Tangent Function'

    description = 'The tanh function is also a sigmoid "S"-shaped function.'

    formula = r'$tanh(z)=\frac{e^{z} - e^{-z}}{e^{z} + e^{-z}}$'   # Markdown LATEX

    additional_information = 'The range of the tanh function is between -1 and 1.'

    plot_title = 'Tanh Function'
    plot_explanation = ['- The tanh function saturates as the inputs become larger (either positive or negative).',
                        '- For large positive and negative values, the function gets asymptotically close to 1 and -1, respectively.',
                        '- When the function saturates, its gradient becomes very close to zero, which slows down learning.']

    pros = ["1. The logistic function introduces non-linearity into the network which allows it to solve more complex problems than linear activation functions.\n2. It is continuous and differentiable everywhere.\n3. Because its output is between 0 and 1, it is very common to use in the output layer in binary classification problems."]

    cons = ["1. Limited Sensitivity\n- The logistic function saturates across most of its domain.\n- It is only sensitive to inputs around its midpoint 0.5.",
            "2. Vanishing Gradients in Deep Neural Networks\n- Because the logistic function can get easily saturated with large inputs, its gradient gets very close to zero. This causes the gradients to get smaller and smaller as backpropagation progresses down to the lower layers of the network.\n- Eventually, the lower layers' weights receive very small updates and never converge to their optimal values."]

    activation_function = tanh

    derivative_title = 'Derivative of the Tanh Function'

    derivative_formula = r'$tanh^{\prime}(z)= 1 - (tanh(z))^{2}$'

    derivatice_plot_explanation = ['Notice that the derivative of the tanh function gets very close to zero for large positive and negative inputs.']

    derivative_function = tanh_derivative

    notes = ["**Note**: the vanishing gradient problem is less severe with the tanh function because it has a mean of 0 (instead of 0.5 like the logistic function)."]


# ======================================================================================
# RelU

def relu(z):
    return np.maximum(0, z)


def relu_derivative(z):
    return (z >= 0).astype(int)


class ReLU(ActivationFunctionBaseClass):

    name = 'ReLU function'
    title = 'Rectified Linear Unit (ReLU) Function'
    description = 'It is a piecewise linear function with two linear pieces that will output the input directly is it is positive (identity function), otherwise, it will output zero.'
    formula = r'$$ReLU(z) = max(0, z)$$'
    additional_information = 'It has become the default activation function for many neural netowrks because it is easier to train and achieves better performance.'

    plot_title = 'ReLU Function'
    activation_function = relu

    derivative_formula = r'$$Relu^{\prime}(z)= \left\{\begin{array}{ll}1 & z>0 \\0 & z<=0 \\\end{array}\right.$$'
    derivative_title = 'Derivative of the ReLU Function'

    derivative_function = relu_derivative

    derivatice_plot_explanation = ['- The derivative of the ReLU function is 1 for z > 0, and 0 for z < 0.',
                                   '- The ReLU function is not differentiable at z = 0.']

    pros = ["1. Computationally Efficient\n- The ReLU function does not require a lot of computation (Unlike the logistic and the tanh function which include an exponential function).\n- Because the ReLU function mimics a linear function when the input is positive, it is very easy to optimize."
            "2. Sparse Representaion\n- The ReLU function can output true zero values when the input is negative. This results in sparse weight matricies which help simplify the model architecure and speed up the learning process.\n- In contrast, the logistic and the tanh function always output non-zero values (sometimes the output is very close to zero, but not a true zero), which results in a dense representation.",
            "3. Avoid Vanishing Gradients\n- The ReLU function does not saturate for positive values which helps avoid the vanishing gradient problem.\n- Switching from the logistic (sigmoid) activation function to ReLU has helped revolutionize the field of deep learning."]

    cons = ["1. Dying ReLUs\n- A problem where ReLU neurons become inactive and only output 0 for any input.\n- This usually happens when the weighted sum of the inputs for all training examples is negative, coupled with a large learning rate.\n- This causes the ReLU function to only output zeros and gradient descent algorithm can not affect it anymore.\n- One of the explanations of this phenomenon is using symmetirc weight distributions to initialize weights and biases.",
            "2. Not differentiable at 0.\n- An abrupt change in the slope causes gradient descent to bounce around."]


# ======================================================================================

## LeakyReLU Function

def leaky_relu(z, alpha = 0.2):
    return np.maximum(alpha * z, z)


def leaky_relu_derivative(z):
    return derivative(leaky_relu, z)


class LeakyReLU(ActivationFunctionBaseClass):

    title = "LeakyReLU Function"

    description = 'A variant of the ReLU function that solves the dying ReLUs problem.'
    formula = r'$LeakyReLU_{\alpha}(z) = max({\alpha}z, z)$'
    additional_information = 'It will output the input directly if it is positive (identity function), but it will output (α * input) if it is negative. This will ensure that the LeakyReLU function never dies.'

    # with st.sidebar.form('leakage'):
    #     alpha = st.slider('α Value', 0.0, 1.0, 0.2)
    #     st.form_submit_button('Apply Changes')
    alpha = 0.2

    activation_function = leaky_relu

    plot_title = 'LeakyReLU Function'

    explanation = ["- This plot will automatically change when you change the value of α from the sidebar slider.",
                   '- Notice that the output of the LeakyReLU function is never a true zero for negative inputs, which helps avoid the dying ReLUs problem.',
                   '- The value α is a hyperparameter that defines how much the function leaks.',
                   '- α represents the slope of the function when the input is negative.',
                   '- The value of α is usually between 0.1 and 0.3.']

    derivative_formula = r'$$LeakyRelu^{\prime}(z)= \left\{\begin{array}{ll}1 & z>0 \\{\alpha} & z<=0 \\\end{array}\right.$$'

    derivative_function = leaky_relu_derivative

    derivative_title = "Derivative of the LeakyReLU Function"

    explanation = ["- This plot will automatically change when you change the value of α from the sidebar slider.",
                   "- Notice that the derivative of the function when the input is negative is equal to the value of α.",
                   "- The function has a nonzero gradient for negative inputs."]

    pros = ["1. Alleviate the Vanishing Gradient Problem",
            "2. Avoids the Dead ReLUs Problem\n- By allowing the function to have a small gradient when the input is negative, we ensure that the neuron never dies.",
            "3. Better Performance\n- The LeakyReLU function along with its variants almost always outperform the standard ReLU."]

# ======================================================================================

    # title: str
    # description: str
    # formula: str   # markdown latex
    # additional_information: str
    # plot_title: str
    # plot_explanation: List[str]
    # pros: List[str]
    # cons: List[str]
    # activation_function: Callable[[float], float]
    # derivative_title: str
    # derivative_formula: str   # markdown latex
    # derivatice_plot_explanation = List[str]
    # derivative_function: Callable[[float], float]
    # notes = List[str] | None

class Variants_of_LeakyReLU:

    title = "Randomized LeakyReLU (RReLU)"

    desription = 'In this variant, the value of α is picked randomly in a given range during training, and is fixed to an average during testing. In addition to having the same advantages of the LeakyReLU, it also has a slight regularization effect (reduce overfitting).'

    additional_information = 'In this variant, the value of α is a trainable (learnable) parameter rather than a hyperparameter. In other words, the backpropagation algorithm can tweak its value like any other model parameter.'

#
#
# # ======================================================================================

def elu(z, alpha=0.2):
    return np.where(z < 0, alpha * (np.exp(z) - 1), z)


class Exponential_Linear_Unit:

    title = 'Exponential Linear Unit (ELU)'
    formula = r'$$ELU_{\alpha}(z)= \left\{\begin{array}{ll}z & z>0 \\{\alpha}(exp(z)-1) & z<=0 \\\end{array}\right.$$'
    additional_information = 'Similar to the ReLU function, ELU will output the input directly if it is positive (identity function). However, ELU\'s output is negative for negative inputs depending on the value of α'
#     with st.sidebar.form('leakage'):
#         alpha = st.slider('α Value', 0.0, 1.0, 0.2)
#         st.form_submit_button('Apply Changes')

#     def elu(z, alpha=alpha):
#         return np.where(z < 0, alpha * (np.exp(z) - 1), z)
#
#
#     elu_fig = plot_function(elu, title="Exponential Linear Unit (ELU) Function", alpha=alpha)
#     st.plotly_chart(elu_fig)
#
#     with st.expander('Plot Explanation'):
#         st.write("- This plot will automatically change when you change the value of α from the sidebar slider.")
#         st.write(
#             '- Similar to LeakyReLU, the output of the  function is never a true zero for negative inputs, which helps avoid the dying ReLUs problem.')
#         st.write('- The value of α is usually set to 1, or chosen in the range of [0.1 and 0.3].')
#         st.write('- If α is equal to 1, the function is smooth everywhere (easier optimization).')
#
#     st.subheader('Derivative')
#     st.markdown(r'$$ELU^{\prime}(z)= \left\{\begin{array}{ll}1 & z>0 \\{\alpha}*exp(z) & z<=0 \\\end{array}\right.$$')
#
#     elu_der_fig = plot_function_derivative(elu, title='Derivative of ELU')
#     st.plotly_chart(elu_der_fig)
#
#     with st.expander('Plot Explanation'):
#         st.write("- This plot will automatically change when you change the value of α from the sidebar slider.")
#         st.write("- The function has a nonzero gradient for negative inputs.")
#
#     st.subheader('Pros')
#     st.write("1. Alleviate the Vanishing Gradient Problem")
#     st.write("2. Avoids the Dead ReLUs Problem")
#     st.write(
#         "3. Faster Convergence\n- When the value of α equals 1, the function is smooth everywhere, which speeds up gradient descent.")
#     st.write(
#         "4. Better Performance.\n- The ELU function outperforms most other ReLU variants with reduced training time.")
#
#     st.subheader("Cons")
#     st.write(
#         "1. Computationally Expensive\n- Because it uses the exponential function, the ELU is slower to compute than other variants of ReLU.")
#
# # ======================================================================================
#
# ## SELU
# if activation_function == 'SELU Function':
#     st.title('Scaled ELU (SELU)')
#
#     st.subheader('Description')
#     st.write('The SELU function is a scaled variant of the ELU function.')
#
#     st.markdown(
#         r'$$SELU_{\alpha}(z)= {\lambda}\left\{\begin{array}{ll}z & z>0 \\{\alpha}(exp(z)-1) & z<=0 \\\end{array}\right.$$')
#
#     st.write("Under certain conditions, using the SELU function will cause the neural network to self-normalize.")
#
#     st.write("The values of λ and α are predetermined by the authors of the function and you do not need to tune them.")
#     st.write(r"$α {\approx} %f$" % selu_alpha)
#     st.write(r"$λ {\approx} %f$" % selu_alpha)
#
#     st.subheader('Plot')
#     selu_fig = plot_function(selu, title='Scaled ELU (SELU) Function')
#     st.plotly_chart(selu_fig)
#
#     with st.expander('Plot Explanation'):
#         st.write("- If the input is positive, the function will return (λ * input).")
#         st.write(
#             "- Similar to LeakyReLU, the output of the  function is never a true zero for negative inputs, which helps avoid the dying ReLUs problem.")
#
#     st.subheader("Derivative")
#     st.markdown(
#         r'$$SELU^{\prime}(z)= {\lambda}\left\{\begin{array}{ll}1 & z>0 \\{\alpha} * exp(z) & z<=0 \\\end{array}\right.$$')
#
#     st.text("")
#
#     selu_der_fig = plot_function_derivative(selu, title='Derivative of the SELU Function')
#     st.plotly_chart(selu_der_fig)
#
#     st.subheader("SELU\'s Self-Normalization Effect")
#     st.write(
#         "One of the major benefits of using the SELU activation function is that it will cause the network to self-normalize.\nIn other words, the output of each layer will maintain a mean of 0 and standard deviation of 1 (follow the standard normal distribution)")
#     st.write("However, for self-normalization to take place, there are certain conditions that need to be satisfied.")
#     st.markdown("**1. The network's architecure must be sequential**")
#     st.write(
#         "Self-normalization is not guaranteed for different architectures such as RNNs, or architectures with skip connections for example.")
#     st.write(
#         "**2. The network parameters (weights and biases) must be initialized using \"LeCun normal initialization\"**")
#     st.write("**3. The input features must be standardized**")
#
#     st.subheader("Pros")
#     st.write(
#         "1. Avoid the Vanishing Gradient Problem\n- Because of the self-normalization effect, the vanishing/exploding gradient problem is eliminated.")
#     st.write(
#         "2. Better Performance\n- The SELU function performs significantly better than other activation functions.")
#
#     st.subheader("Cons")
#     st.write(
#         "1. Unguaranteed Self-Normalization\n- The self-normalization effect of SELU is only guaranteed under certain conditions.")
#

# ======================================================================================


activation_functions = {'None': None,
                        'Logistic (Sigmoid) Function': Logistic,
                        'Hyperbolic Tangent (Tanh) Function': Tanh,
                        'ReLU Function': ReLU,
                        'LeakyReLU Function': LeakyReLU,
                        'Variants of LeakyReLU Function': None,
                        'Exponential Linear Unit Function': None,
                        'SELU Function': None}
