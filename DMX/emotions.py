from DMXEnttecPro import Controller
from Aputure import Infinibar
from Epix import Flex20
from time import sleep
import logging, tomli, threading, random

# Emotion-Color Mappings (examples, can be customized)
EMOTION_SCHEMAS = {
    "joy": {
        "colors": [[255, 255, 0], [255, 165, 0]],  # Yellows and Oranges
        "effect": "chase"
    },
    "sadness": {
        "colors": [[0, 0, 139], [0, 0, 255]],  # Deep Blues
        "effect": "slow_fade"
    },
    "anger": {
        "colors": [[255, 0, 0], [139, 0, 0]],  # Reds
        "effect": "strobe"
    },
    "fear": {
        "colors": [[128, 0, 128], [75, 0, 130]],  # Purples and Indigos
        "effect": "flicker"
    },
    "surprise": {
        "colors": [[0, 255, 255], [255, 255, 255]],  # Cyan and White
        "effect": "flash"
    },
    "disgust": {
        "colors": [[0, 128, 0], [85, 107, 47]],  # Greens
        "effect": "pulse"
    },
    "trust": {
        "colors": [[0, 191, 255], [30, 144, 255]],  # Sky and Dodger Blue
        "effect": "solid"
    },
    "anticipation": {
        "colors": [[255, 69, 0], [255, 140, 0]],  # Orange-Red and Dark Orange
        "effect": "fast_chase"
    },
    "love": {
        "colors": [[255, 105, 180], [255, 20, 147]],  # Pinks
        "effect": "gentle_pulse"
    },
    "calmness": {
        "colors": [[0, 255, 127], [64, 224, 208]],  # Aquamarine and Turquoise
        "effect": "slow_wave"
    },
    "excitement": {
        "colors": [[255, 215, 0], [255, 20, 147], [0, 255, 255]],  # Gold, Deep Pink, Cyan
        "effect": "multi_strobe"
    },
    "jealousy": {
        "colors": [[50, 205, 50], [154, 205, 50]],  # Lime Green and Yellow-Green
        "effect": "alternating"
    },
    "confusion": {
        "colors": [[128, 0, 128], [255, 165, 0], [0, 0, 255]],  # Purple, Orange, Blue
        "effect": "random_flash"
    },
    "hope": {
        "colors": [[255, 255, 240], [240, 230, 140]],  # Ivory and Khaki (gentle yellows)
        "effect": "breathing"
    },
    "pride": {
        "colors": [[255, 215, 0], [128, 0, 128]],  # Gold and Purple
        "effect": "regal_march"
    }
}

def play_emotion(emotion: str, bars: list[Infinibar], strips: list[Flex20], duration: int = 10):
    if emotion not in EMOTION_SCHEMAS:
        print(f"Unknown emotion: {emotion}")
        return

    schema = EMOTION_SCHEMAS[emotion]
    effect = schema["effect"]
    colors = schema["colors"]

    # --- Effect Implementations ---

    if effect == "chase":
        for _ in range(duration):
            for i in range(len(bars[0].chunks)):
                for bar in bars:
                    for c in range(len(bar.chunks)):
                        bar.set_intensity(c, 0)
                    color = random.choice(colors)
                    bar.set_red(i, color[0])
                    bar.set_green(i, color[1])
                    bar.set_blue(i, color[2])
                    bar.set_intensity(i, 255)
                for strip in strips:
                    strip.fg_rgb(random.choice(colors))
                bars[0].submit()
                sleep(0.1)

    elif effect == "slow_fade":
        for _ in range(duration * 2):
            for color in colors:
                for strip in strips:
                    strip.fg_rgb(color)
                for bar in bars:
                    for c in range(len(bar.chunks)):
                        bar.set_red(c, color[0])
                        bar.set_green(c, color[1])
                        bar.set_blue(c, color[2])
                        bar.set_intensity(c, 128)
                bar.submit()
                sleep(1)

    elif effect == "strobe":
        for _ in range(duration * 5):
            color = random.choice(colors)
            for strip in strips:
                strip.fg_rgb(color)
            for bar in bars:
                bar.ON()
            bar.submit()
            sleep(0.05)
            for bar in bars:
                bar.OFF()
            bar.submit()
            sleep(0.05)

    # Add more effect implementations here...

    else:
        print(f"Unknown effect: {effect}")


if __name__ == "__main__":
    import argparse

    cliArgumentParser = argparse.ArgumentParser()
    cliArgumentParser.add_argument("-e", dest="EMOTION", metavar="EMOTION", type=str, required=True, help="What emotion should be displayed?")
    cliArgumentParser.add_argument("-c", dest="COM", metavar="COM", type=str, required=True, help="What COM port is the Enttec controller on?")
    cliArgumentParser.add_argument("-m", dest="MODE", metavar="MODE", type=int, default=9, help="What mode should the bar(s) be set to?")
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

    dmx = Controller(args.COM)

    bars = []
    for b in config['lights']['BARS']:
        bars.append(Infinibar(b, args.MODE, dmx, logger))
    
    strips = []
    for s in config['lights']['STRIPS']:
        strips.append(Flex20(s, dmx, logger))

    play_emotion(args.EMOTION, bars, strips)

    dmx.close()
