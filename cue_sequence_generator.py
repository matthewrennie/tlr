import numpy as np
from pydub import AudioSegment
from pydub.generators import Sine


def generate_beep(frequency, duration_ms, silence_ms=200):
    """Generate a single beep tone followed by silence."""
    beep = Sine(frequency).to_audio_segment(duration=duration_ms)
    silence = AudioSegment.silent(duration=silence_ms)
    return beep + silence


def generate_beeping_sequence():
    """Generate a sequence of 500Hz, 700Hz, 900Hz tones."""
    beep_500 = generate_beep(500, 200)
    beep_700 = generate_beep(700, 200)
    beep_900 = generate_beep(900, 200)
    return beep_500 + beep_700 + beep_900


# Generate the cue
cue_sequence = generate_beeping_sequence()
cue_sequence.export("./data/cue_sequence.wav", format="wav")

print("Beeping sequence generated and saved as ./data/cue_sequence.wav.")
