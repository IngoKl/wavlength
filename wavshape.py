"""Scans a given path (folder) for .wav files recursively and plots them all into files."""
from pathlib import Path, PurePath
import matplotlib.pyplot as plt
import numpy as np
from numpy import fft as fft
import click
import scipy.io.wavfile
from wavlength import get_files, plot_wav


def analyze_and_plot(wavfile, output, save_to=False, title=False):
    """Analyze a given wav file based on an amplitude threshold."""
    rate = 0
    audio_data = 0

    if wavfile.is_file():
        try:
            rate, audio_data = scipy.io.wavfile.read(wavfile.resolve())
            plot_wav(rate, audio_data, save_to=save_to, title=title)
        except Exception as e:
            print(e)
            return False


@click.command()
@click.option('--folder', default='.', help='The folder to scan.')
@click.option('--output', default='./plots', help='The folder to plot to..')
def plotting(folder, output):
    """Scan a given folder and plot all wav files."""
    files = get_files(Path(folder))
    print(f'{len(files)} have been found and will be plotted.')

    for wavfile in files:
        save_to = str(Path(PurePath(output + '/'), wavfile.name).resolve()) + '.png'
        analyze_and_plot(wavfile, output, save_to=save_to, title=wavfile.name)

if __name__ == '__main__':
    plotting()