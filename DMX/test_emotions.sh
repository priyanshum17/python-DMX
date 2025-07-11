#!/bin/bash

# This script tests all the emotion lighting schemas defined in emotions.py

# IMPORTANT: Replace this with the actual path to your serial port
COM_PORT="/dev/ttyUSB1"

# List of all emotions and their effects
EMOTIONS=(
    "joy chase"
    "sadness slow_fade"
    "anger strobe"
    "fear flicker"
    "surprise flash"
    "disgust pulse"
    "trust solid"
    "anticipation fast_chase"
    "love gentle_pulse"
    "calmness slow_wave"
    "excitement multi_strobe"
    "jealousy alternating"
    "confusion random_flash"
    "hope breathing"
    "pride regal_march"
)

# Change to the directory where the script is located
cd "$(dirname "$0")"

# Loop through the emotions and run the test
for item in "${EMOTIONS[@]}"; do
    # Split the item into emotion and effect
    read -r emotion effect <<<"$item"

    echo "----------------------------------------"
    echo "Testing Emotion: $emotion"
    echo "Effect: $effect"
    echo "----------------------------------------"

    # Run the python script
    python3 emotions.py -e "$emotion" -c "$COM_PORT" -m 13 -d 10

    # Optional: add a small delay between tests if needed
    sleep 2
done

echo "All emotion tests complete."
