import torch
import sounddevice as sd
import time




language = 'ru'
model_id = 'ru_v3'
sample_rate = 48000
speaker = 'aidar'
device = torch.device('cpu') # gpu or cpu

model_speak, _ = torch.hub.load(repo_or_dir='snakers4/silero-models',
                                     model='silero_tts',
                                     language=language,
                                     speaker=model_id)

model_speak.to(device)


def speak(text: str):
    audio = model_speak.apply_tts(text=text,
                        speaker=speaker,
                        sample_rate=sample_rate)
    
    sd.play(audio, sample_rate * 1.05)
    time.sleep((len(audio) / sample_rate) + 0.5)
    sd.stop()