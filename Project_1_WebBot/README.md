# WebBot
### A bot designed to play [Sushi Go Round](https://www.miniclip.com/games/sushi-go-round/en/ "Miniclip")
This is a bot created to play Sushi Go Round, found on Miniclip. This bot was created following the tutorial on [Envato Tuts](https://code.tutsplus.com/tutorials/how-to-build-a-python-bot-that-can-play-web-games--active-11117 "Envanto Tuts") and updated for python 3.6.

## Changes
The following changes were made from the tutorial

This Web Bot was made with the [Anaconda](https://www.anaconda.com/download/ "Anaconda") distribution of python instead of PyWin

ImageGrab is now part of the PIL module and is imported through PIL.

ImageOps is now part of the PIL module and is imported through PIL

print now requires parenthesis

``` python
.has_key()
```
is deprecated and replaced with

```python
x in y
```

global variables have been replaced as arguments

I later changed the print lines with logging for a cleaner experience
## Videos
The first finished version had a problem where the cursor for the delivery was too high shown in the video below:
### [Original Video](https://www.youtube.com/watch?time_continue=5&v=rBhMgZqbAUs "WebBot Test Video")

After changing some values for the mouse position based on my laptops screen, this will have to be changed if run on a computer with different display settings, the bot worked as intended.

### [Updated Video](https://www.youtube.com/watch?v=uPW_BgZcbII&feature=youtu.be "WebBot Test Video Updated")
