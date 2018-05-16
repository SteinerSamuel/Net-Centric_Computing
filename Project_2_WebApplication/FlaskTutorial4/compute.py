from numpy import exp, cos, linspace
import matplotlib.pyplot as plt
import os
import time
import glob


def damped_vibrations(t, a, b, w):
    return a*exp(-b*t)*cos(w*t)


def compute(a, b, w, t, resolution=500):
    """Return filename of plot of the damped_vibration function."""
    t = linspace(0, t, resolution+1)
    u = damped_vibrations(t, a, b, w)
    plt.figure()  # needed to avoid adding curves in plot
    plt.plot(t, u)
    plt.title('A=%g, b=%g, w=%g' % (a, b, w))
    if not os.path.isdir('static'):
        os.mkdir('static')
    else:
        # Remove old plot files
        for filename in glob.glob(os.path.join('static', '*.png')):
            os.remove(filename)
    # Use time since Jan 1, 1970 in filename in order make
    # a unique filename that the browser has not chached
    plotfile = os.path.join('static', str(time.time()) + '.png')
    plt.savefig(plotfile)
    return plotfile


if __name__ == '__main__':
    print(compute(1, 0.1, 1, 20))
