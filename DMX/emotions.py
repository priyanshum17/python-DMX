from DMXEnttecPro import Controller
from Aputure import Infinibar
from Epix import Flex20
from time import sleep, time
import logging, tomli, threading, random, math

# Emotion-Color Mappings (examples, can be customized)
EMOTION_SCHEMAS = {
    "joy": {
        "colors": [[255, 255, 0], [255, 165, 0], [255, 215, 0]],  # Yellows, Oranges, Gold
        "effect": "chase"
    },
    "sadness": {
        "colors": [[0, 0, 139], [0, 0, 205], [70, 130, 180]],  # Deep Blues, Steel Blue
        "effect": "slow_fade"
    },
    "anger": {
        "colors": [[255, 0, 0], [139, 0, 0], [255, 69, 0]],  # Reds, Orange-Red
        "effect": "strobe"
    },
    "fear": {
        "colors": [[128, 0, 128], [75, 0, 130], [138, 43, 226]],  # Purples, Indigos, Blue-Violet
        "effect": "flicker"
    },
    "surprise": {
        "colors": [[0, 255, 255], [255, 255, 255], [224, 255, 255]],  # Cyan, White, Light Cyan
        "effect": "flash"
    },
    "disgust": {
        "colors": [[0, 128, 0], [85, 107, 47], [107, 142, 35]],  # Greens, Olive Drab
        "effect": "pulse"
    },
    "trust": {
        "colors": [[0, 191, 255], [30, 144, 255], [173, 216, 230]],  # Sky, Dodger Blue, Light Blue
        "effect": "solid"
    },
    "anticipation": {
        "colors": [[255, 69, 0], [255, 140, 0], [255, 99, 71]],  # Orange-Red, Dark Orange, Tomato
        "effect": "fast_chase"
    },
    "love": {
        "colors": [[255, 105, 180], [255, 20, 147], [219, 112, 147]],  # Pinks, Pale Violet Red
        "effect": "gentle_pulse"
    },
    "calmness": {
        "colors": [[0, 255, 127], [64, 224, 208], [175, 238, 238]],  # Aquamarine, Turquoise, Pale Turquoise
        "effect": "slow_wave"
    },
    "excitement": {
        "colors": [[255, 215, 0], [255, 20, 147], [0, 255, 255]],  # Gold, Deep Pink, Cyan
        "effect": "multi_strobe"
    },
    "jealousy": {
        "colors": [[50, 205, 50], [154, 205, 50], [0, 255, 0]],  # Lime Green, Yellow-Green, Green
        "effect": "alternating"
    },
    "confusion": {
        "colors": [[128, 0, 128], [255, 165, 0], [0, 0, 255]],  # Purple, Orange, Blue
        "effect": "random_flash"
    },
    "hope": {
        "colors": [[255, 255, 240], [240, 230, 140], [255, 250, 205]],  # Ivory, Khaki, Lemon Chiffon
        "effect": "breathing"
    },
    "pride": {
        "colors": [[255, 215, 0], [128, 0, 128], [218, 165, 32]],  # Gold, Purple, Goldenrod
        "effect": "regal_march"
    }
}

def play_emotion(emotion: str, bars: list[Infinibar], strips: list[Flex20], duration: int):
    if emotion not in EMOTION_SCHEMAS:
        print(f"Unknown emotion: {emotion}")
        return

    schema = EMOTION_SCHEMAS[emotion]
    effect = schema["effect"]
    colors = schema["colors"]
    start_time = time()

    def set_all_bars(r, g, b, intensity=255):
        for bar in bars:
            for c in range(len(bar.chunks)):
                bar.set_red(c, r)
                bar.set_green(c, g)
                bar.set_blue(c, b)
                bar.set_intensity(c, intensity)

    def set_all_strips(r, g, b, brightness=255):
        for strip in strips:
            strip.fg_rgb((r, g, b), brightness=brightness)

    while time() - start_time < duration:
        if effect == "chase" or effect == "fast_chase":
            speed = 0.05 if effect == "fast_chase" else 0.1
            for i in range(len(bars[0].chunks)):
                if time() - start_time > duration: break
                color = random.choice(colors)
                for bar in bars:
                    # Turn off all chunks first for a cleaner chase
                    for c in range(len(bar.chunks)):
                        bar.set_intensity(c, 0)
                    bar.set_red(i, color[0])
                    bar.set_green(i, color[1])
                    bar.set_blue(i, color[2])
                    bar.set_intensity(i, 255)
                set_all_strips(color[0], color[1], color[2])
                bars[0].submit()
                sleep(speed)

        elif effect == "slow_fade":
            for color1, color2 in zip(colors, colors[1:] + [colors[0]]):
                if time() - start_time > duration: break
                for i in range(101):
                    if time() - start_time > duration: break
                    # Calculate intermediate color
                    r = int(color1[0] + (color2[0] - color1[0]) * (i/100))
                    g = int(color1[1] + (color2[1] - color1[1]) * (i/100))
                    b = int(color1[2] + (color2[2] - color1[2]) * (i/100))
                    set_all_bars(r, g, b, 150)
                    set_all_strips(r, g, b, 150)
                    bars[0].submit()
                    sleep(0.03)

        elif effect == "strobe" or effect == "multi_strobe":
            speed = 0.05
            for _ in range(int(0.2 / speed)): # Strobe for 0.2s
                if time() - start_time > duration: break
                color = random.choice(colors)
                set_all_bars(color[0], color[1], color[2])
                set_all_strips(color[0], color[1], color[2])
                bars[0].submit()
                sleep(speed)
                set_all_bars(0,0,0,0)
                set_all_strips(0,0,0,0)
                bars[0].submit()
                sleep(speed)
            sleep(0.3) # Pause between strobes

        elif effect == "flicker":
            for _ in range(int(0.5 / 0.05)): # Flicker for 0.5s
                if time() - start_time > duration: break
                intensity = random.randint(100, 255)
                color = random.choice(colors)
                set_all_bars(color[0], color[1], color[2], intensity)
                set_all_strips(color[0], color[1], color[2], intensity)
                bars[0].submit()
                sleep(0.05)
            set_all_bars(0,0,0,0) # End with lights off
            set_all_strips(0,0,0,0)
            bars[0].submit()
            sleep(random.uniform(0.2, 0.8)) # Random pause

        elif effect == "flash":
            if time() - start_time > duration: break
            color = random.choice(colors)
            set_all_bars(color[0], color[1], color[2])
            set_all_strips(color[0], color[1], color[2])
            bars[0].submit()
            sleep(0.1)
            set_all_bars(0,0,0,0)
            set_all_strips(0,0,0,0)
            bars[0].submit()
            sleep(1)

        elif effect == "pulse" or effect == "gentle_pulse":
            speed = 0.02 if effect == "pulse" else 0.04
            for color in colors:
                 if time() - start_time > duration: break
                 # Pulse up
                 for i in range(50, 200, 5):
                     if time() - start_time > duration: break
                     set_all_bars(color[0], color[1], color[2], i)
                     set_all_strips(color[0], color[1], color[2], i)
                     bars[0].submit()
                     sleep(speed)
                 # Pulse down
                 for i in range(200, 50, -5):
                     if time() - start_time > duration: break
                     set_all_bars(color[0], color[1], color[2], i)
                     set_all_strips(color[0], color[1], color[2], i)
                     bars[0].submit()
                     sleep(speed)

        elif effect == "solid":
            color = colors[0]
            set_all_bars(color[0], color[1], color[2])
            set_all_strips(color[0], color[1], color[2])
            bars[0].submit()
            sleep(duration) # Hold for the whole duration

        elif effect == "slow_wave":
            for i in range(int(duration * 10)): # Loop for duration
                if time() - start_time > duration: break
                pos = i / 10.0
                for c in range(len(bars[0].chunks)):
                    # Create a sine wave across the bar chunks
                    intensity = int((math.sin(pos + c) + 1) / 2 * 255)
                    color = colors[c % len(colors)]
                    for bar in bars:
                        bar.set_red(c, color[0])
                        bar.set_green(c, color[1])
                        bar.set_blue(c, color[2])
                        bar.set_intensity(c, intensity)
                # Strips can follow the average color/intensity
                avg_intensity = int((math.sin(pos) + 1) / 2 * 255)
                avg_color = colors[int(pos) % len(colors)]
                set_all_strips(avg_color[0], avg_color[1], avg_color[2], avg_intensity)
                bars[0].submit()
                sleep(0.1)

        elif effect == "alternating":
            if time() - start_time > duration: break
            color1 = colors[0]
            color2 = colors[1]
            set_all_bars(color1[0], color1[1], color1[2])
            set_all_strips(color2[0], color2[1], color2[2])
            bars[0].submit()
            sleep(0.5)
            if time() - start_time > duration: break
            set_all_bars(color2[0], color2[1], color2[2])
            set_all_strips(color1[0], color1[1], color1[2])
            bars[0].submit()
            sleep(0.5)

        elif effect == "random_flash":
            if time() - start_time > duration: break
            # Flash a random chunk on a random bar
            bar = random.choice(bars)
            chunk = random.randint(0, len(bar.chunks) - 1)
            color = random.choice(colors)
            bar.set_red(chunk, color[0])
            bar.set_green(chunk, color[1])
            bar.set_blue(chunk, color[2])
            bar.set_intensity(chunk, 255)
            # Also flash one of the strips
            strip = random.choice(strips)
            strip.fg_rgb(color)
            bars[0].submit()
            sleep(0.1)
            bar.set_intensity(chunk, 0)
            strip.fg_rgb((0,0,0), brightness=0)
            bars[0].submit()
            sleep(random.uniform(0.2, 0.5))

        elif effect == "breathing":
            speed = 0.05
            for color in colors:
                if time() - start_time > duration: break
                # Breathe in
                for i in range(10, 150, 2):
                    if time() - start_time > duration: break
                    set_all_bars(color[0], color[1], color[2], i)
                    set_all_strips(color[0], color[1], color[2], i)
                    bars[0].submit()
                    sleep(speed)
                # Breathe out
                for i in range(150, 10, -2):
                    if time() - start_time > duration: break
                    set_all_bars(color[0], color[1], color[2], i)
                    set_all_strips(color[0], color[1], color[2], i)
                    bars[0].submit()
                    sleep(speed)
                sleep(1) # Pause

        elif effect == "regal_march":
            speed = 0.2
            color1, color2 = colors[0], colors[1]
            for i in range(len(bars[0].chunks)):
                if time() - start_time > duration: break
                for bar in bars:
                    for c in range(len(bar.chunks)):
                        # Alternate colors down the bar
                        color = color1 if (c+i) % 2 == 0 else color2
                        bar.set_red(c, color[0])
                        bar.set_green(c, color[1])
                        bar.set_blue(c, color[2])
                        bar.set_intensity(c, 255)
                # Strips can alternate too
                strip_color = color1 if i % 2 == 0 else color2
                set_all_strips(strip_color[0], strip_color[1], strip_color[2])
                bars[0].submit()
                sleep(speed)

        else:
            print(f"Unknown effect: {effect}")
            break # Exit loop if effect is not found

def turn_off_all(bars, strips):
    print("\nTurning off all lights.")
    for bar in bars:
        bar.OFF()
    for strip in strips:
        strip.OFF()
    if bars or strips:
        (bars or strips)[0].submit()

if __name__ == "__main__":
    import argparse

    cliArgumentParser = argparse.ArgumentParser(description="Control DMX lights based on emotions.")
    cliArgumentParser.add_argument("-e", dest="EMOTION", metavar="EMOTION", type=str, required=True, help=f"Emotion to display. Choices: {', '.join(EMOTION_SCHEMAS.keys())}")
    cliArgumentParser.add_argument("-c", dest="COM", metavar="COM", type=str, required=True, help="COM port or device path for the Enttec controller.")
    cliArgumentParser.add_argument("-d", dest="DURATION", metavar="SECONDS", type=int, default=10, help="How long the emotion should be displayed for, in seconds.")
    cliArgumentParser.add_argument("-m", dest="MODE", metavar="MODE", type=int, default=9, help="DMX mode for the Infinibar(s).")
    cliArgumentParser.add_argument('--verbose', '-v', action='count', default=0, help="Enable verbose output. -v for INFO, -vv for DEBUG.")
    args = cliArgumentParser.parse_args()

    # Setup logging
    if args.verbose == 0:
        loglevel = logging.WARNING
    elif args.verbose == 1:
        loglevel = logging.INFO
    else:
        loglevel = logging.DEBUG
    logger = logging.getLogger()
    logger.setLevel(loglevel)
    streamHandler = logging.StreamHandler()
    streamHandler.setLevel(loglevel)
    logger.addHandler(streamHandler)

    # Load config
    try:
        with open('config.toml', "rb") as conf:
            config = tomli.load(conf)
    except FileNotFoundError:
        logger.error("Error: config.toml not found. Please ensure it exists in the same directory.")
        exit(1)


    dmx = Controller(args.COM)
    bars = [Infinibar(b, args.MODE, dmx, logger) for b in config['lights']['BARS']]
    strips = [Flex20(s, dmx, logger) for s in config['lights']['STRIPS']]

    try:
        logger.info(f"Displaying emotion '{args.EMOTION}' for {args.DURATION} seconds...")
        play_emotion(args.EMOTION, bars, strips, args.DURATION)
    except KeyboardInterrupt:
        pass # The finally block will handle cleanup
    finally:
        turn_off_all(bars, strips)
        dmx.close()
        print("Cleanup complete. Exiting.")