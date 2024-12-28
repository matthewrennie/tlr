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


def get_random_dBFS(min_dBFS, max_dBFS):
    """
    Get a random target dBFS within the specified range.
    :param min_dBFS: Minimum dBFS value.
    :param max_dBFS: Maximum dBFS value.
    :return: Random dBFS value within the range.
    """
    return random.uniform(min_dBFS, max_dBFS)


# Define the target dBFS range corresponding to 40-45 dB SPL
min_target_dBFS = -25.0
max_target_dBFS = -20.0

# Load the cue sequence
cue_sequence = AudioSegment.from_file("./data/cue_sequence.wav")

# Normalize the cue sequence to a random volume level within the range
random_target_dBFS = get_random_dBFS(min_target_dBFS, max_target_dBFS)
normalized_cue_sequence = normalize_volume(cue_sequence, random_target_dBFS)

# Define new time intervals for the REM cueing sequence
thirty_second_silence = AudioSegment.silent(duration=30 * 1000)  # 30 seconds
ten_minute_silence = AudioSegment.silent(duration=10 * 60 * 1000)  # 10 minutes

# Create the REM cueing sequence
rem_cueing_section = ten_minute_silence
for _ in range(5):  # Add normalized cues 5 times with 30-second intervals
    rem_cueing_section += normalized_cue_sequence + thirty_second_silence

# Export the REM cueing sequence
rem_cueing_output_path = "./out/rem_cueing.mp3"
rem_cueing_section.export(rem_cueing_output_path, format="mp3")

print(f"REM cueing sequence assembled and saved as {rem_cueing_output_path}.")
