"""
Name: WebBot
Version: 1.0
Dependencies: PIL, Numpy
Author: Samuel Steiner
Description: A Bot made to play online game Sushi Go Round found at https://www.miniclip.com/games/sushi-go-round/en/
Information: This program was made for playing the game in a firefox window with no toolbars active at a resolution of
             1600 x 900.
"""

# import statements
from PIL import ImageGrab, ImageOps
# import os # used for debugging make sure to comment out when running without debug
import time
import win32api
import win32con
import numpy
import logging


# configure logging
logging.basicConfig(filename=str(time.time()).replace('.', '') + '.log', level=logging.INFO)

# Dictionary to hold values for food on hand.
foodOnHand = {'shrimp': 5,
              'rice': 10,
              'nori': 10,
              'roe': 10,
              'salmon': 5,
              'unagi': 5}

# Dictionary to hold color values for each basic sushi type
sushiTypes = {2670: 'onigiri',
              3143: 'caliroll',
              2677: 'gunkan'}


# a class that holds the values for the blank seat color values when there is no bubble
class Blank:
    seat_1 = 8119
    seat_2 = 5986
    seat_3 = 11598
    seat_4 = 10532
    seat_5 = 6782
    seat_6 = 9041


# a class which holds coordinates of where certain game elements are relative to the padding
class Cord:
    f_shrimp = (47, 340)
    f_rice = (75, 340)
    f_nori = (47, 406)
    f_roe = (75, 406)
    f_salmon = (47, 440)
    f_unagi = (75, 440)

    # =================

    phone = (582, 329)

    toppings = (543, 269)

    t_shrimp = (523, 211)
    t_nori = (521, 272)
    t_roe = (598, 275)
    t_salmon = (521, 330)
    t_unagi = (601, 215)
    t_exit = (592, 327)

    menu_rice = (535, 291)
    buy_rice = (541, 269)

    delivery_norm = (486, 300)


def screengrab(x_pad=306, y_pad=232):
    """
    grabs a screen shot using the bound by coordinates designated by box
    :param x_pad: The x_padding of the x coordinate default is 306
    :param y_pad: the y_padding of the y coordinate default is 232
    :return: Returns the image  bounded by box
    """
    box = (x_pad+1, y_pad+1, x_pad+640, y_pad+480)
    im = ImageGrab.grab(box)
    # im.save(os.getcwd() + '\\full_snap__' + str(int(time.time())) + '.png', 'PNG')                         # Debugging
    return im


def grab(x_pad=306, y_pad=232):
    """
    Grabs a screen of the screen and returns a greyscale sum of the area selected
    :return: a,  the sum of the greyscale values for the screen shot
    :param x_pad: The x_padding of the x coordinate default is 306
    :param y_pad: the y_padding of the y coordinate default is 232
    """
    box = (x_pad+1, y_pad+1, x_pad+640, y_pad+480)
    im = ImageOps.grayscale(ImageGrab.grab(box))
    a = numpy.array(im.getcolors())
    a = a.sum()
    logging.debug('Color:' + a)

    return a


def grab_seat_one(x_pad, y_pad):
    """
    Takes a screen shot then finds the greyscale sum of the area determined by box this is for the first seat in the
    game.
    :param x_pad: The x_padding of the x coordinate
    :param y_pad: the y_padding of the y coordinate
    :return: a, returns the sum of the greyscale values of the area
    """
    box = (x_pad + 26, y_pad + 61, x_pad + 89, y_pad + 77)
    im = ImageOps.grayscale(ImageGrab.grab(box))
    a = numpy.array(im.getcolors())
    a = a.sum()
    logging.debug(a)                                                                                         # Debugging

    return a


def grab_seat_two(x_pad, y_pad):
    """
    Takes a screen shot then finds the greyscale sum of the area determined by box this is for the second seat in the
    game.
    :param x_pad: The x_padding of the x coordinate
    :param y_pad: the y_padding of the y coordinate
    :return: a, returns the sum of the greyscale values of the area
    """
    box = (x_pad + 127, y_pad + 61, x_pad + 190, y_pad + 77)
    im = ImageOps.grayscale(ImageGrab.grab(box))
    a = numpy.array(im.getcolors())
    a = a.sum()
    logging.debug(a)                                                                                         # Debugging

    return a


def grab_seat_three(x_pad, y_pad):
    """
    Takes a screen shot then finds the greyscale sum of the area determined by box this is for the third seat in the
    game.
    :param x_pad: The x_padding of the x coordinate
    :param y_pad: the y_padding of the y coordinate
    :return: a, returns the sum of the greyscale values of the area
    """
    box = (x_pad + 228, y_pad + 61, x_pad + 291, y_pad + 77)
    im = ImageOps.grayscale(ImageGrab.grab(box))
    a = numpy.array(im.getcolors())
    a = a.sum()
    logging.debug(a)                                                                                         # Debugging

    return a


def grab_seat_four(x_pad, y_pad):
    """
    Takes a screen shot then finds the greyscale sum of the area determined by box this is for the fourth seat in the
    game.
    :param x_pad: The x_padding of the x coordinate
    :param y_pad: the y_padding of the y coordinate
    :return: a, returns the sum of the greyscale values of the area
    """
    box = (x_pad + 329, y_pad + 61, x_pad + 392, y_pad + 77)
    im = ImageOps.grayscale(ImageGrab.grab(box))
    a = numpy.array(im.getcolors())
    a = a.sum()
    logging.debug(a)                                                                                         # Debugging

    return a


def grab_seat_five(x_pad, y_pad):
    """
    Takes a screen shot then finds the greyscale sum of the area determined by box this is for the fifth seat in the
    game.
    :param x_pad: The x_padding of the x coordinate
    :param y_pad: the y_padding of the y coordinate
    :return: a, returns the sum of the greyscale values of the area
    """
    box = (x_pad + 430, y_pad + 61, x_pad + 493, y_pad + 77)
    im = ImageOps.grayscale(ImageGrab.grab(box))
    a = numpy.array(im.getcolors())
    a = a.sum()
    logging.debug(a)                                                                                         # Debugging

    return a


def grab_seat_six(x_pad, y_pad):
    """
    Takes a screen shot then finds the greyscale sum of the area determined by box this is for the sixth seat in the
    game.
    :param x_pad: The x_padding of the x coordinate
    :param y_pad: the y_padding of the y coordinate
    :return: a, returns the sum of the greyscale values of the area
    """
    box = (x_pad + 531, y_pad + 61, x_pad + 594, y_pad + 77)
    im = ImageOps.grayscale(ImageGrab.grab(box))
    a = numpy.array(im.getcolors())
    a = a.sum()
    logging.debug(a)                                                                                         # Debugging

    return a


def grab_all_seats(x_pad, y_pad):
    """
    A function that quickly runs through and gets the greyscale value for all seats mostly for debugging
    :param x_pad: The x_padding of the x coordinate
    :param y_pad: the y_padding of the y coordinate
    """
    grab_seat_one(x_pad, y_pad)
    grab_seat_two(x_pad, y_pad)
    grab_seat_three(x_pad, y_pad)
    grab_seat_four(x_pad, y_pad)
    grab_seat_five(x_pad, y_pad)
    grab_seat_six(x_pad, y_pad)


def leftclick():
    """
    Simulates a left click
    """
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    time.sleep(.1)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)
    logging.info("Click.")


def leftdown():
    """
    Simulates a left mouse press down
    """
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    time.sleep(.1)
    logging.info('left Down')


def leftup():
    """
    Simulates a left mouse release
    """
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)
    time.sleep(.1)
    logging.info('left release')


def mousepos(cord, x_pad=306, y_pad=232):
    """
    Moves the mouse to a prescribed location
    :param cord: The coordinates minus the padding in a tuple where the mouse should go
    :param x_pad: The x_padding of the x coordinate default is 306
    :param y_pad: the y_padding of the y coordinate default is 232
    """
    win32api.SetCursorPos((x_pad + cord[0], y_pad + cord[1]))


def get_cords(x_pad=306, y_pad=232):
    """
    Prints the coordinates of the of the mouse to the log file when called on
    :param x_pad: The x_padding of the x coordinate default is 306
    :param y_pad: the y_padding of the y coordinate default is 232
    """
    x, y = win32api.GetCursorPos()
    x = x - x_pad
    y = y - y_pad
    logging.info('x:' + x + 'y:' + y)


def startgame():
    """
    A function which starts the game from the initial menu
    """
    # location of first menu
    mousepos((315, 205))
    leftclick()
    time.sleep(.1)

    # location of second menu
    mousepos((327, 393))
    leftclick()
    time.sleep(.1)

    # location of third menu
    mousepos((578, 453))
    leftclick()
    time.sleep(.1)

    # location of fourth menu
    mousepos((373, 374))
    leftclick()
    time.sleep(.1)


def clear_tables():
    """
    Clears the tables of empty plates.
    """
    mousepos((97, 207))
    leftclick()

    mousepos((189, 209))
    leftclick()

    mousepos((292, 209))
    leftclick()

    mousepos((396, 205))
    leftclick()

    mousepos((503, 205))
    leftclick()

    mousepos((583, 207))
    leftclick()
    time.sleep(2)


def foldmat():
    """
    Folds the sushi mat to make the sushi
    """
    mousepos((Cord.f_rice[0]+100, Cord.f_rice[1]))
    leftclick()
    time.sleep(.1)


def makefood(food):
    """
    Takes a food name and then passes instructions and makes the sushi
    :param food: the sushi which needs to be made could be one of three basic sushi, caliroll, onigiri, or gunkan
    """
    if food == 'caliroll':
        logging.info('Making a caliroll')
        # updates food on hand with food spent to make roll
        foodOnHand['rice'] -= 1
        foodOnHand['nori'] -= 1
        foodOnHand['roe'] -= 1

        # mouse clicks used to make the caliroll
        mousepos(Cord.f_rice)
        leftclick()
        time.sleep(.05)
        mousepos(Cord.f_nori)
        leftclick()
        time.sleep(.05)
        mousepos(Cord.f_roe)
        leftclick()
        time.sleep(.1)
        foldmat()
        time.sleep(1.5)

    elif food == 'onigiri':
        logging.info('Making a onigiri')
        # updates food on hand with food spent to make onigiri
        foodOnHand['rice'] -= 2
        foodOnHand['nori'] -= 1

        # mouse clicks used to make the onigiri
        mousepos(Cord.f_rice)
        leftclick()
        time.sleep(.05)
        mousepos(Cord.f_rice)
        leftclick()
        time.sleep(.05)
        mousepos(Cord.f_nori)
        leftclick()
        time.sleep(.1)
        foldmat()
        time.sleep(.05)

        time.sleep(1.5)

    elif food == 'gunkan':
        logging.info('Making gunkan')
        # updates food on hand with food spent to make gunkan
        foodOnHand['rice'] -= 1
        foodOnHand['nori'] -= 1
        foodOnHand['roe'] -= 2

        # mouse clicks used to make gunkan
        mousepos(Cord.f_rice)
        leftclick()
        time.sleep(.05)
        mousepos(Cord.f_nori)
        leftclick()
        time.sleep(.05)
        mousepos(Cord.f_roe)
        leftclick()
        time.sleep(.05)
        mousepos(Cord.f_roe)
        leftclick()
        time.sleep(.1)
        foldmat()
        time.sleep(1.5)


def buyfood(food):
    """
    Purchases food from the phone menu
    :param food: Which food is needed to replenish stock can be one of 3 options. rice, nori , or roe
    """

    if food == 'rice':
        mousepos(Cord.phone)
        time.sleep(.1)
        leftclick()
        mousepos(Cord.menu_rice)
        time.sleep(.5)
        leftclick()
        s = screengrab()
        if s.getpixel(Cord.buy_rice) != (127, 127, 127):
            logging.info('Rice is available')
            mousepos(Cord.buy_rice)
            time.sleep(.1)
            leftclick()
            mousepos(Cord.delivery_norm)
            foodOnHand['rice'] += 10
            time.sleep(1)
            logging.info("Click")
            leftclick()
            time.sleep(2.5)
        else:
            logging.info('Rice is unavailable')
            mousepos(Cord.t_exit)
            leftclick()
            time.sleep(1)
            buyfood(food)

    if food == 'nori':
        mousepos(Cord.phone)
        time.sleep(.1)
        leftclick()
        mousepos(Cord.toppings)
        time.sleep(.05)
        leftclick()
        s = screengrab()
        time.sleep(.1)
        if s.getpixel(Cord.t_nori) != (109, 123, 127):
            logging.info('Nori is available')
            mousepos(Cord.t_nori)
            time.sleep(.1)
            leftclick()
            mousepos(Cord.delivery_norm)
            foodOnHand['nori'] += 10
            time.sleep(1)
            logging.info("Click")
            leftclick()
            time.sleep(2.5)
        else:
            logging.info('nori is unavailable')
            mousepos(Cord.t_exit)
            leftclick()
            time.sleep(1)
            buyfood(food)

    if food == 'roe':
        mousepos(Cord.phone)
        time.sleep(.1)
        leftclick()
        mousepos(Cord.toppings)
        time.sleep(.05)
        leftclick()
        s = screengrab()
        time.sleep(.1)
        if s.getpixel(Cord.t_roe) != (109, 123, 127):
            logging.info('Roe is available')
            mousepos(Cord.t_roe)
            time.sleep(.1)
            leftclick()
            mousepos(Cord.delivery_norm)
            foodOnHand['roe'] += 10
            time.sleep(.5)
            logging.info("Click")
            leftclick()
            time.sleep(2.5)
        else:
            logging.info('Roe is unavailable')
            mousepos(Cord.t_exit)
            leftclick()
            time.sleep(1)
            buyfood(food)


def checkfood():
    """
    Checks the food on hand and buys food if necessary
    """
    printonhand()
    for i, j in foodOnHand.items():
        logging.info(i)
        if i == 'nori' or i == 'rice' or i == 'roe':
            if j <= 4:
                logging.info('%s is low and needs to be replenished' % i)
                buyfood(i)


def printonhand():
    logging.info(foodOnHand)


def check_bubs(x_pad=306, y_pad=232):
    """
    Runs through checking if each seat has a customer, periodically checking food on hand and for empty plates. If there
    is a customer who wants a sushi checks to see if it is one of the three known sushi, and makes the food using the
    makefood function
    :param x_pad: This parameter is the x_padding for the game window; default is 306.
    :param y_pad: This parameter is the y_padding for the game window; default is 232.
    """
    checkfood()
    s1 = grab_seat_one(x_pad, y_pad)
    if s1 != Blank.seat_1:
        if s1 in sushiTypes:
            logging.info('table 1 is occupied and needs %s' % sushiTypes[s1])
            makefood(sushiTypes[s1])
        else:
            logging.error('sushi not found!\n sushiType = %i' % s1)

    else:
        logging.info('Table 1 unoccupied')

    clear_tables()
    checkfood()
    s2 = grab_seat_two(x_pad, y_pad)
    if s2 != Blank.seat_2:
        if s2 in sushiTypes:
            logging.info('table 2 is occupied and needs %s' % sushiTypes[s2])
            makefood(sushiTypes[s2])
        else:
            logging.error('sushi not found!\n sushiType = %i' % s2)

    else:
        logging.info('Table 2 unoccupied')

    checkfood()
    s3 = grab_seat_three(x_pad, y_pad)
    if s3 != Blank.seat_3:
        if s3 in sushiTypes:
            logging.info('table 3 is occupied and needs %s' % sushiTypes[s3])
            makefood(sushiTypes[s3])
        else:
            logging.error('sushi not found!\n sushiType = %i' % s3)

    else:
        logging.info('Table 3 unoccupied')

    checkfood()
    s4 = grab_seat_four(x_pad, y_pad)
    if s4 != Blank.seat_4:
        if s4 in sushiTypes:
            logging.info('table 4 is occupied and needs %s' % sushiTypes[s4])
            makefood(sushiTypes[s4])
        else:
            logging.error('sushi not found!\n sushiType = %i' % s4)

    else:
        logging.info('Table 4 unoccupied')

    clear_tables()
    checkfood()
    s5 = grab_seat_five(x_pad, y_pad)
    if s5 != Blank.seat_5:
        if s5 in sushiTypes:
            logging.info('table 5 is occupied and needs %s' % sushiTypes[s5])
            makefood(sushiTypes[s5])
        else:
            logging.error('sushi not found!\n sushiType = %i' % s5)

    else:
        logging.info('Table 5 unoccupied')

    checkfood()
    s6 = grab_seat_six(x_pad, y_pad)
    if s6 != Blank.seat_6:
        if s6 in sushiTypes:
            logging.info('table 1 is occupied and needs %s' % sushiTypes[s6])
            makefood(sushiTypes[s6])
        else:
            logging.error('sushi not found!\n sushiType = %i' % s6)

    else:
        logging.info('Table 6 unoccupied')

    clear_tables()


def main():
    """
    Main function that starts the game and plays it
    """
    startgame()
    while True:
        check_bubs()


if __name__ == '__main__':
    main()
