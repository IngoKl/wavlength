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
    copy_id = 0

    if not copy_folder.is_dir():
        copy_folder.mkdir()

    print(f'{len(files)} have been found and will be copied.')
    for wavfile in files:
        copy_id += 1
        try:
            shutil.copy(wavfile.resolve(), copy_folder.resolve())
            #Rename the copied file to avoid file collisions
            new_file = Path(copy_folder.joinpath(wavfile.name))
            new_file.rename(copy_folder.joinpath(wavfile.name.replace('.wav', f'-{copy_id}.wav')))
        except Exception as e:
            print(e)

if __name__ == '__main__':
    collect()