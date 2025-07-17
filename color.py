from DMXEnttecPro import Controller
from DMX.Aputure import Infinibar
import logging
import time

# ─────────────── Config ─────────────── #
COM_PORT = "/dev/cu.usbserial-EN472951"
DMX_ADDRESS_RANGE = range(1, 480, 10)  # Start addresses from 1–480 in steps of 10
DMX_MODES = [12] #range(9, 17)  # Modes 9 through 16
PAUSE_BETWEEN_TESTS = 2   # Seconds to wait per test
# ────────────────────────────────────── #

# Logging
logger = logging.getLogger("DMX-BruteTest")
logger.setLevel(logging.INFO)
logger.addHandler(logging.StreamHandler())

# Simple rainbow color wheel
def color_wheel(i):
    colors = [
        (255, 0, 0), (0, 255, 0), (0, 0, 255),
        (255, 255, 0), (0, 255, 255), (255, 0, 255),
        (255, 128, 0), (128, 0, 255), (255, 255, 255)
    ]
    return colors[i % len(colors)]

# The actual test
def run_test_combo(dmx, address, mode):
    try:
        bar = Infinibar(address, mode, dmx, logger)
    except Exception as e:
        logger.warning(f"Could not initialize bar at address {address} mode {mode}: {e}")
        return

    logger.info(f"🧪 DMX Mode {mode}, Address {address}, Chunks: {len(bar.chunks)}")

    for c in range(len(bar.chunks)):
        r, g, b = color_wheel(c)
        bar.set_cct_temp(c, 0)
        bar.set_crossfade(c, 0)
        bar.set_red(c, r)
        bar.set_green(c, g)
        bar.set_blue(c, b)
        bar.set_intensity(c, 255)

    bar.submit()
    time.sleep(PAUSE_BETWEEN_TESTS)
    bar.OFF()
    bar.submit()

def main():
    dmx = Controller(COM_PORT)

    try:
        for mode in DMX_MODES:
            for address in DMX_ADDRESS_RANGE:
                run_test_combo(dmx, address, mode)
    finally:
        dummy_bar = Infinibar(1, 9, dmx, logger)
        dummy_bar.OFF()
        dummy_bar.submit()
        dmx.close()
        logger.info("✅ All DMX output stopped.")

if __name__ == "__main__":
    main()
