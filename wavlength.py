"""Scans a given path (folder) for .wav files recursively and returns their
collective length. The primary use case is to calculate the overall length of a
set of wav files given an amplitude treshold.
"""
from pathlib import Path
import matplotlib.pyplot as plt
import numpy as np
from numpy import fft as fft
import click
import scipy.io.wavfile


def get_files(folder):
    """Scans a given path (folder) for .wav files recursively."""
    files = []
    for file in folder.glob(f'{folder}/**/*.wav'):
        files.append(file)

    return files


def plot_wav(rate, audio_data):
    """Generate a time/amplitude plot."""
    time = np.arange(0, float(audio_data.shape[0]), 1) / rate

    channels = len(audio_data.shape)
    if channels == 2:
        channel_l = audio_data[:, 0]
        channel_r = audio_data[:, 1]

    if channels == 1:
        plt.plot(time, audio_data, linewidth=0.01, alpha=0.7, color='#004256')
        plt.xlabel('Time (s)')
        plt.ylabel('Amplitude')
        plt.show()
    elif channels == 2:
        plt.plot(time, channel_l, linewidth=0.01, alpha=0.7, color='#004256')
        plt.plot(time, channel_r, linewidth=0.01, alpha=0.7, color='#ff0033')
        plt.xlabel('Time (s)')
        plt.ylabel('Amplitude')
        plt.show()


def analyze_wav(wavfile, amp_threshold, plot=False):
    """Analyze a given wav file based on an amplitude threshold."""
    if wavfile.is_file():
        try:
            rate, audio_data = scipy.io.wavfile.read(wavfile.resolve())

            length_s = audio_data.shape[0] / rate
            channels = len(audio_data.shape)

            if channels == 2:
                mode = 'Stereo'
                channel_l = audio_data[:, 0]
                channel_r = audio_data[:, 1]
                amp_avg = np.average((abs(channel_l) + abs(channel_r)) / 2)
                length_s_above_threshold = audio_data[abs(audio_data) > amp_threshold].shape[0] / rate / 2
            elif channels == 1:
                mode = 'Mono'
                amp_avg = np.average(abs(audio_data))
                length_s_above_threshold = audio_data[abs(audio_data) > amp_threshold].shape[0] / rate

            if plot:
                plot_wav(rate, audio_data)

            return {'mode': mode, 'amp_avg': amp_avg, 'length_s': length_s,
                    'length_s_above_threshold': length_s_above_threshold}
        except Exception as e:
            print(f'There seems to be an issue with file {wavfile}', e)
            return False
    else:
        return False


@click.command()
@click.option('--folder', default='.', help='The folder to scan.')
@click.option('--amp_threshold', default=100,
              help='The maximum amplitude threshold to be recognized as silence.')
@click.option('--plot', default=False, help='Plotting time/amplitude graphs.')
def scan(folder, amp_threshold, plot):
    """Scan a given folder and report the length of all wav files combined."""
    files = get_files(Path(folder))
    length_s = 0
    length_s_above_threshold = 0

    for wavfile in files:
        analysis = analyze_wav(wavfile, amp_threshold, plot)
        length_s += analysis['length_s']
        length_s_above_threshold += analysis['length_s_above_threshold']

    print(f'{len(files)} files have been analyzed')
    print(f'Overall Length: {round(length_s)} s / {round(length_s/60)} m')
    print(f'Overall Length (above Treshold (amp > {amp_threshold})): {round(length_s_above_threshold)} s / {round(length_s_above_threshold/60)} m')


if __name__ == '__main__':
    scan()