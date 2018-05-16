import sympy as sp
import numpy as np
import matplotlib.pyplot as plt
import os
import time
import glob

legends = []


def visualize_series(formula, independent_variable, n, xmin, xmax, ymin, ymax, legend_loc, x0='0', erase='yes'):
    """
    :param formula:  String: Formula
    :param independent_variable:  String: Name of independent var
    :param n:  int: degree of polynomial approx.
    :param xmin:  string: x axis min
    :param xmax:  string: x axis max
    :param ymin:  string: y axis min
    :param ymax:  string: y axis max
    :param legend_loc: int: passes an int value of the legend location based on pylpot documentation
    :param x0: point of expansion.
    :param erase: String: passes a string yes or no
    :return:
    """
    # Turns independent variable into sympy symbol stored as x
    x = sp.symbols(f'{independent_variable}')
    # exec("x = sp.symbols('%s')" % independent_variable)
    namespace = sp.__dict__.copy()  # copies the sympy namespace
    namespace.update({independent_variable: sp.symbols(independent_variable)})
    # adds the sympy symbol into our name space
    formula = eval(formula, namespace)  # evaluates the formula to create a sympy formula
    x0 = eval(x0, namespace)  # evaluates x0 into a sympy symbol
    xmin = eval(xmin, np.__dict__)  # evaluates xmin as a numpy object
    xmax = eval(xmax, np.__dict__)  # evaluates xmax as a numpy object
    ymin = eval(ymin, np.__dict__)  # evaluates ymin as a numpy object
    ymax = eval(ymax, np.__dict__)  # evaluates ymax as a numpy object

    # calls our function to set the generate a function for the sin and the expansion
    f, s, tex, = formula2series2pyfunc(formula, n, x, x0)

    t = np.linspace(xmin, xmax)  # sets the x values

    label_tex = sp.latex(formula)  # makes a LaTeX version of the formula

    """
    The following part of code is necessary in order to not re draw the same line over and over again when just changing
    the degree of the taylor series or not changing anything.
    """

    global legends
    if erase == 'yes':  # Starts a new figure if the erase parameter is set to yes
        plt.figure()
        legends = []

    if f'{label_tex}' not in legends:  # checks to see if the label is included in the legend
        # plots the original formula figure and sets the label to the LaTeX version
        plt.plot(t, f(t), label='$%s$' % label_tex)
        legends.append(f'{label_tex}')  # appends label to label list
    if f'{label_tex}, {n}' not in legends:
        # plots the taylor series and sets the label to the series value
        plt.plot(t, s(t), label='Series, N = %s' % n)
        legends.append(f'{label_tex}, {n}')
    # changes the y axis length of the figure to the user specified ones
    plt.ylim(ymin, ymax)
    # creates the legend for the figure
    legend_loc = eval(legend_loc, np.__dict__)
    plt.legend(loc=legend_loc)
    # plt.show()                                                                                        # Debugging Code
    if not os.path.isdir('static'):  # checks to see if there is a static directory if there isn't it creates it
        os.mkdir('static')
    else:  # removes any png images that are in the static directory if the directory exists
        for filename in glob.glob(os.path.join('static', '*.png')):
            os.remove(filename)

    plotfile = os.path.join('static', str(time.time()) + '.png')  # sets the plot to a file based off the time.

    plt.savefig(plotfile)  # saves the figure to the plot file
    return plotfile, tex


def formula2series2pyfunc(formula, n, x, x0=0):
    """
    :param formula: a sympy formula
    :param n: an integer
    :param x: a sympy symbol
    :param x0: a sympy sumbol
    :return: returns a python function for the given sympy formula a function for the sympy formula series to the Nth
             term
    and a latex version of the formula
    """
    temp = formula.series(x, x0, n+1)  # creates a temp variable to hold the formula for manipulation
    tex = sp.latex(temp)  # creates a latex version of the formula given
    fs = temp.removeO()  # removes the O() term
    s = sp.lambdify([x], fs)  # creates a python formula for the taylor series to the Nth term

    f = sp.lambdify([x], formula)  # Creates a python function for the formula

    return f, s, tex
