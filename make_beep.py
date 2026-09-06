import wave
import math
import struct

filename = "sounds/beep.wav"

rate = 44100
duration = 0.08   # very short beep
frequency = 1400  # higher pitch

with wave.open(filename, "w") as sound:
    sound.setnchannels(1)
    sound.setsampwidth(2)
    sound.setframerate(rate)

    for i in range(int(rate * duration)):
        value = int(24000 * math.sin(2 * math.pi * frequency * i / rate))
        sound.writeframes(struct.pack("<h", value))

print("Fast beep created!")