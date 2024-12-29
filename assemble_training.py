from pydub import AudioSegment
import random


def normalize_volume(audio, target_dBFS):
    """
    Normalize the volume of an audio segment to a target dBFS.
    :param audio: AudioSegment to normalize.
    :param target_dBFS: Target volume in dBFS.
    :return: Normalized AudioSegment.
    """
    change_in_dBFS = target_dBFS - audio.dBFS
    return audio.apply_gain(change_in_dBFS)


# Function to select a random target dBFS within the range
def get_random_dBFS(min_dBFS, max_dBFS):
    return random.uniform(min_dBFS, max_dBFS)


# Define the target dBFS range corresponding to 40-45 dB SPL
min_target_dBFS = -25.0
max_target_dBFS = -20.0

# Load generated audio files
initial_prompt = AudioSegment.from_file("./data/initial_prompt.mp3")
follow_up_prompt = AudioSegment.from_file("./data/follow_up_prompt.mp3")
cue_sequence = AudioSegment.from_file("./data/cue_sequence.wav")

# Normalize volumes to a random value within the range
initial_prompt = normalize_volume(
    initial_prompt, get_random_dBFS(min_target_dBFS, max_target_dBFS)
)
follow_up_prompt = normalize_volume(
    follow_up_prompt, get_random_dBFS(min_target_dBFS, max_target_dBFS)
)
cue_sequence = normalize_volume(
    cue_sequence, get_random_dBFS(min_target_dBFS, max_target_dBFS)
)

# Define time intervals
two_second_silence = AudioSegment.silent(duration=2 * 1000)  # 1 minute
one_minute_silence = AudioSegment.silent(duration=60 * 1000)  # 1 minute
longer_silence = AudioSegment.silent(duration=150 * 1000)  # 2.5 minutes

# 1. Combine initial section (5 minutes with prompts)
five_min_section = two_second_silence + initial_prompt + one_minute_silence
for _ in range(5):  # Add cues + follow-up prompts 5 times
    five_min_section += (
        cue_sequence + two_second_silence + follow_up_prompt + one_minute_silence
    )

# 2. Create the 8-minute section (cues only every minute)
eight_min_section = AudioSegment.empty()
for _ in range(8):  # Add cues 8 times
    eight_min_section += cue_sequence + one_minute_silence

# 3. Create the 7-minute section (cues spaced further apart)
seven_min_section = AudioSegment.empty()
for _ in range(3):  # Add cues 3 times with longer intervals
    seven_min_section += cue_sequence + longer_silence

# Combine all sections
full_audio = five_min_section + eight_min_section + seven_min_section

# Export the final MP3 file
output_path = "./out/lucid_dream_training.mp3"
full_audio.export(output_path, format="mp3")

print(f"Full audio sequence assembled and saved as {output_path}.")
