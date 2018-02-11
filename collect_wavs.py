"""Scans a given path (folder) for .wav files recursively and copys all of 
them into a new folder.
"""
from pathlib import Path
import shutil
import click
from wavlength import get_files


@click.command()
@click.option('--scan_folder', default='.', help='The folder to scan.')
@click.option('--copy_folder', default='./collected_wavs', help='The folder top copy to.')
def collect(scan_folder, copy_folder):
    """Scan a given folder and copies all .wav files into a new folder."""
    files = get_files(Path(scan_folder))
    copy_folder = Path(copy_folder)

    if not copy_folder.is_dir():
        copy_folder.mkdir()

    for wavfile in files:
        shutil.copy(wavfile.resolve(), copy_folder.resolve())

if __name__ == '__main__':
    collect()