import streamlit as st
import numpy as np
import plotly.graph_objects as go

from activation_functions import *


def plot_function(func, title, alpha=None):
    fig = go.Figure()
    if alpha:
        fig.add_trace(go.Scatter(x=z, y=func(z, alpha=alpha), mode='lines', line=dict(color='red', width=3)))
    else:
        fig.add_trace(go.Scatter(x=z, y=func(z), mode='lines', line=dict(color='red', width=3)))
    fig.update_layout(title = title, xaxis_title='Z',width=700, height=400,
                            font=dict(family="Courier New, monospace",size=16,color="White"), margin=dict(t=30, b=0, l=0, r=0))
    fig.update_xaxes(zeroline=True, zerolinewidth=3, zerolinecolor='violet')
    fig.update_yaxes(zeroline=True, zerolinewidth=3, zerolinecolor='violet')
    return fig


def plot_function_derivative(func, title):
    return plot_function(derivative(func, z), title)
    # fig = go.Figure()
    # fig.add_trace(go.Scatter(x=z, y=derivative(func, z), mode='lines', line=dict(color='red', width=3)))
    # fig.update_layout(title = title, xaxis_title='Z', width=700, height=400,
    #                         font=dict(family="Courier New, monospace",size=16,color="White"), margin=dict(t=30, b=0, l=0, r=0))
    # fig.update_xaxes(zeroline=True, zerolinewidth=3, zerolinecolor='violet')
    # fig.update_yaxes(zeroline=True, zerolinewidth=3, zerolinecolor='violet')
    # return fig


# Domain
z = np.linspace(-8, 8, 200)

# Build the page
st.title('Activation Functions')

selected_activation_function = st.selectbox('Choose an activation function',
                                             activation_functions.keys())

activation_function_class = activation_functions[selected_activation_function]

if activation_function_class is not None:

    # Header
    st.header(selected_activation_function)

    # Description
    st.subheader('Description')

    st.write(activation_function_class.description)
    st.markdown(activation_function_class.formula)
    st.write(activation_function_class.additional_information)

    # Plot
    st.subheader('Plot')

    fig = plot_function(activation_function_class.activation_function,
                        title=activation_function_class.title)

    st.plotly_chart(fig)

    # Explanation
    if activation_function_class.plot_explanation:
        with st.expander('Plot Explanation'):
            for explanation in activation_function_class.plot_explanation:
                st.write(explanation)

    # Derivative
    st.subheader('Derivative')

    st.markdown(activation_function_class.derivative_formula)

    # Plot Derivative
    st.subheader('Plot')

    fig = plot_function(activation_function_class.derivative_function,
                        title=activation_function_class.derivative_title)

    st.plotly_chart(fig)

    # Explanation
    if activation_function_class.derivatice_plot_explanation:
        with st.expander('Plot Explanation'):
            for item in activation_function_class.derivatice_plot_explanation:
                st.write(item)

    # Pro's
    if activation_function_class.pros:
        st.subheader('Pros')
        for item in activation_function_class.pros:
            st.write(item)

    # Con's
    if activation_function_class.cons:
        st.subheader('Cons')
        for item in activation_function_class.cons:
            st.write(item)

    # Notes
    if activation_function_class.notes:
        st.subheader('Notes')
        for item in activation_function_class.notes:
            st.write(item)
