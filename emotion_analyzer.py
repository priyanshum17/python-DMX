from google import genai
from pydantic import BaseModel
import argparse
import subprocess
from datetime import datetime


# Configure Gemini
client = genai.Client(api_key="ENTER_KEY")

# Available emotions and effects
AVAILABLE_EMOTIONS = [
    "joy", "sadness", "anger", "fear", "surprise", "disgust", "trust",
    "anticipation", "love", "calmness", "excitement", "jealousy",
    "confusion", "hope", "pride"
]

AVAILABLE_EFFECTS = [
    "chase", "slow_fade", "strobe", "flicker", "flash", "pulse", "solid",
    "fast_chase", "gentle_pulse", "slow_wave", "multi_strobe", "alternating",
    "random_flash", "breathing", "regal_march"
]

# Pydantic schema
class DMXResponse(BaseModel):
    emotion: str
    effect: str

def analyze_text_with_gemini(text_to_analyze):
    """Analyzes text and returns the best-matched emotion and lighting effect."""
    try:
        response = client.models.generate_content(
            model="gemini-2.0-flash-lite",
            contents=f"""
                Analyze the following input text and choose the most dominant emotion it conveys.
                Then select the most appropriate DMX lighting effect that best represents that emotion.

                Emotions: {AVAILABLE_EMOTIONS}
                Effects: {AVAILABLE_EFFECTS}

                Input: "{text_to_analyze}"

                Return a single JSON object with 'emotion' and 'effect' fields.
            """,
            config={
                "response_mime_type": "application/json",
                "response_schema": list[DMXResponse], 
            }
        )

        parsed_result: list[DMXResponse] = response.parsed
        if not parsed_result:
            print("No valid response from Gemini.")
            return None, None

        result = parsed_result[0]

        # Validate content
        if result.emotion not in AVAILABLE_EMOTIONS:
            print(f"Invalid emotion: {result.emotion}")
            return None, None
        if result.effect not in AVAILABLE_EFFECTS:
            print(f"Invalid effect: {result.effect}")
            return None, None

        return result.emotion, result.effect

    except Exception as e:
        print(f"Error during Gemini API call: {e}")
        return None, None

def run_lighting_script(emotion, effect, com_port, duration):
    """Runs the DMX lighting script with emotion as the trigger."""
    print(f"\nRunning lighting for emotion: '{emotion}'")
    print("To control effect independently, modify emotions.py to accept an effect parameter.")

    command = [
        "python3",
        "DMX/emotions.py",
        "-e", emotion,
        "-c", com_port,
        "-d", str(duration)
    ]

    try:
        subprocess.run(command, check=True)
    except subprocess.CalledProcessError as e:
        print(f"Script execution failed: {e}")
    except FileNotFoundError:
        print("Error: Could not find DMX/emotions.py.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Analyze text and trigger DMX lighting.")
    parser.add_argument("text", type=str, help="The input text to analyze.")
    parser.add_argument("-c", "--COM", type=str, required=True, help="COM port for Enttec DMX.")
    parser.add_argument("-d", "--DURATION", type=int, default=15, help="Lighting duration in seconds.")

    args = parser.parse_args()

    emotion, effect = analyze_text_with_gemini(args.text)

    if emotion and effect:
        print(f"\n✓ Analysis Complete:")
        print(f"  Emotion → {emotion}")
        print(f"  Effect  → {effect}")
        run_lighting_script(emotion, effect, args.COM, args.DURATION)
    else:
        print("\n✗ Failed to determine valid emotion/effect.")
