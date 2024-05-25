import pyaudio
import wave
import numpy as np
from scipy.fftpack import fft

# Function to get the dominant frequency from an audio signal
def get_dominant_frequency(data, rate):
    # Perform Fourier Transform on the data
    N = len(data)
    yf = fft(data)
    xf = np.fft.fftfreq(N, 1 / rate)
    idx = np.argmax(np.abs(yf))
    freq = abs(xf[idx])
    return freq

# Function to play audio file and print the dominant frequency
def play_audio(filename):
    # Open the audio file
    wf = wave.open(filename, 'rb')

    # Instantiate PyAudio
    p = pyaudio.PyAudio()

    # Define callback function to stream audio and analyze frequency
    def callback(in_data, frame_count, time_info, status):
        data = wf.readframes(frame_count)
        if len(data) == 0:
            return (None, pyaudio.paComplete)
        
        # Convert data to numpy array
        audio_data = np.frombuffer(data, dtype=np.int16)
        
        # Get the dominant frequency
        dominant_freq = get_dominant_frequency(audio_data, wf.getframerate())
        print(f"Dominant Frequency: {dominant_freq} Hz")
        
        return (data, pyaudio.paContinue)

    # Open a stream
    stream = p.open(format=p.get_format_from_width(wf.getsampwidth()),
                    channels=wf.getnchannels(),
                    rate=wf.getframerate(),
                    output=True,
                    stream_callback=callback)

    # Start the stream
    stream.start_stream()

    # Wait for the stream to finish
    while stream.is_active():
        pass

    # Stop and close the stream
    stream.stop_stream()
    stream.close()
    wf.close()

    # Terminate the PyAudio object
    p.terminate()

if __name__ == "__main__":
    audio_file = 'test.wav'  # Replace with your audio file path
    play_audio(audio_file)
