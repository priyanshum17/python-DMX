from DMXEnttecPro import Controller
from Aputure import Infinibar
from Epix import Flex20
from time import sleep
import logging, tomli, threading

def bar_test(bar: Infinibar, sep_func, arg=None):

    bar.ON()
    bar.submit()

    sep_func(arg)

    bar.OFF()
    bar.submit()

    sep_func(arg)

    bar.ON()
    bar.submit()

    sep_func(arg)

    for c in range(len(bar.chunks)):
        logger.debug("Blue")
        bar.set_red(c, 0)
        bar.set_green(c, 0)
        bar.set_blue(c, 255)
        bar.set_crossfade(c, 255)
    bar.submit()

    sep_func(arg)

    for c in range(len(bar.chunks)):
        logger.debug("Green")
        bar.set_blue(c, 0)
        bar.set_green(c, 255)
    bar.submit()

    sep_func(arg)

    for c in range(len(bar.chunks)):
        logger.debug("Red")
        bar.set_green(c, 0)
        bar.set_red(c, 255)
    bar.submit()

    sep_func(arg)

    for c in range(len(bar.chunks)):
        bar.set_crossfade(c, 0)
    bar.submit()

    sep_func(arg)

    bar.OFF()
    bar.submit()

def flex_test(strip: Flex20, sep_func, arg=None):
    strip.fg_rgb(config['colors']['RED'])
    strip.submit()
    logger.debug("RED FG")

    sep_func(arg)

    strip.fg_rgb(config['colors']['BLUE'])
    strip.submit()
    logger.debug("BLUE FG")

    sep_func(arg)

    strip.fg_rgb(config['colors']['YELLOW'], 0)
    strip.submit()
    logger.debug("FG OFF")

    sep_func(arg)

    strip.fg_rgb(config['colors']['YELLOW'])
    strip.submit()
    logger.debug("FG YELLOW")

    sep_func(arg)

    strip.bg_rgb(config['colors']['TEAL'])
    strip.submit()
    logger.debug("BG TEAL")

    sep_func(arg)

    strip.fg_rgb(config['colors']['YELLOW'])
    strip.fg_program(45)
    strip.fg_speed(200)
    strip.submit()
    logger.debug("FG YELLOW, FG Program 45")

    sep_func(arg)

    strip.bg_program(45)
    strip.bg_speed(200)
    strip.submit()

    logger.debug("BG Program 45")

    sep_func(arg)

    strip.fg_program(0)
    strip.bg_program(0)
    strip.fg_rgb(config['colors']['YELLOW'])
    strip.submit()
    logger.debug("PROGRAMS OFF, FG YELLOW")

    sep_func(arg)

    strip.OFF()
    logger.debug("OFF")

    sep_func(arg)

if __name__=="__main__":
    import argparse

    cliArgumentParser = argparse.ArgumentParser()
    cliArgumentParser.add_argument("-m", dest="MODE", metavar="MODE", type=int, required=True, help="What mode should the bar(s) be set to?")
    cliArgumentParser.add_argument("-c", dest="COM", metavar="COM", type=int, required=True, help="What COM port is the Enttec controller on?")
    cliArgumentParser.add_argument('--verbose', '-v', action='count', default=0, required=False, help="Enable verbose output")
    args = cliArgumentParser.parse_args()

    with open('config.toml', "rb") as conf:
        config = tomli.load(conf)

    if args.verbose == 0:
        loglevel = logging.WARNING
    elif args.verbose == 1:
        loglevel = logging.INFO
    elif args.verbose > 1:
        loglevel = logging.DEBUG
    
    logger = logging.getLogger()
    logger.setLevel(loglevel)
    streamHandler = logging.StreamHandler()
    streamHandler.setLevel(loglevel)
    logger.addHandler(streamHandler)

    dmx = Controller('COM%d' % args.COM)

    lightThreads = []

    bars = []
    for b in config['lights']['BARS']:
        bars.append(Infinibar(b, args.MODE, dmx, logger))
    
    strips = []
    for s in config['lights']['STRIPS']:
        strips.append(Flex20(s, dmx, logger))

    for strip in strips:
        lT = threading.Thread(target=flex_test, args=(strip, sleep, 3))
        lT.start()
        lightThreads.append(lT)
        
    #for bar in bars:
    #    bar_test(bar, sleep, .5)

    for lT in lightThreads:
        lT.join()

    dmx.close()
