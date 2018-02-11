# wavlength
Wavelength is a simple script that returns the overall length of all .wav files in a folder structure.
It also reports how long a given amplitude threshold has been overstepped. This can be used to identify
how much of the files is just 'silence'.

The primary use case for this script is to calculate transcription cost, which often is
based on the overall playtime of the files submitted.

## How To
Wavelength exposes a simple click CLI interface.

`python wavelength.py --folder ./wavs --amp_threshold=100 --plot=True`
