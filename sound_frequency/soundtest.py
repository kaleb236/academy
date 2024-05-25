import pyaudio
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Parameters
CHUNK = 1024  # Number of audio samples per frame
FORMAT = pyaudio.paInt16  # Audio format (16-bit PCM)
CHANNELS = 1  # Number of audio channels (1 for mono)
RATE = 44100  # Sample rate (samples per second)

# Initialize PyAudio
p = pyaudio.PyAudio()

# Open audio stream
stream = p.open(format=FORMAT,
                channels=CHANNELS,
                rate=RATE,
                input=True,
                frames_per_buffer=CHUNK)

# Initialize the plot
fig, ax = plt.subplots()
x = np.fft.fftfreq(CHUNK, 1.0 / RATE)
x = x[:CHUNK // 2]  # Only positive frequencies
line, = ax.plot(x, np.zeros(CHUNK // 2))
ax.set_xlim(0, RATE / 2)
ax.set_ylim(0, 1000)  # Adjust the y-axis limit as necessary

# Update function for the animation
def update(frame):
    data = stream.read(CHUNK, exception_on_overflow=False)
    audio_data = np.frombuffer(data, dtype=np.int16)
    fft_data = np.fft.fft(audio_data)
    freq_magnitudes = np.abs(fft_data)[:CHUNK // 2]
    print(freq_magnitudes)
    
    line.set_ydata(freq_magnitudes)
    return line,

# Animation
ani = FuncAnimation(fig, update, interval=50, blit=True)

# Show the plot
plt.show()

# Close the stream when done
stream.stop_stream()
stream.close()
p.terminate()
