# Targeted Lucidity Reactivation
## Training and REM-sleep cueing audio generator

Scripts to generate audio files similar to those described in the paper **"Combining presleep cognitive training and REM-sleep stimulation in a laboratory morning nap for lucid dream induction."**, *Carr. M., et al.* [^lnk]

### Getting started

Use ElevenLabs to generate the voice prompts and download into ```./data/initial_prompt.mp3``` and ```./data/follow_up_prompt.mp3``` respectively.

ElevenLabs Prompts:

- Initial
```
Now we are going to practice becoming lucid. We want to train your mind to recognize the beeping sounds as “lucidity cues” so that you can have a lucid dream. While you rest here, we are going to play the cues at approximate 1-minute intervals. Whenever you hear the cues, you should remain in the same position with your eyes closed, but you will become lucid by attending to where your mind has been, attending to your body, and attending to your surroundings. Focus on how aspects of your experience might be in any way different from your normal waking experience.
```

- Follow-up prompt
```
As you notice the cue, you become lucid. Bring your attention to your thoughts, notice how your mind has wandered.<break time="5s" />Now observe your body, sensations, and feelings.<break time="5s" />Observe your breathing<break time="5s" />remain critically aware, lucid, and notice how aspects of this experience are in any way different from your normal waking experience.
```

### Installation

```
conda create -n lucid python=3.10
conda activate lucid
conda install numpy
conda install conda-forge::pydub
conda install ffmpeg
python ./cue_sequence_generator.py
python ./assemble_training.py
python ./assemble_rem_cueing.py
```

Copy ```./out/lucid_dream_training.mp3``` and ```./out/rem_cueing.mp3``` to your media player.


[^lnk]: "[Combining presleep cognitive training and REM-sleep stimulation in a laboratory morning nap for lucid dream induction.](https://psycnet.apa.org/doiLanding?doi=10.1037%2Fcns0000227)", *Carr. M., et al.*
