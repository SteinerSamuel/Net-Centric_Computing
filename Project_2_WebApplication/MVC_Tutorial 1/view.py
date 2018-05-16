import sys
import compute

# Input: float r
# Output: "Hello World! sin(r)=..."


def get_input():
    """
    Gets input data from command line
    :return: r
    """
    r = float(sys.argv[1])
    return r


def present_output(r):
    """
    Writes results to the terminal window
    :param r:
    :return:
    """
    s = compute.compute(r)
    print('Hello World! sin(%g) = %g' % (r, s))
