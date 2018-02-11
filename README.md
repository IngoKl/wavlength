# wavlength
Wavelength is a simple (Python > 3.5) script that returns the overall length of all .wav files in a folder structure.
It also reports how long a given amplitude threshold has been overstepped. This can be used to identify
how much of the files is just 'silence'.

The primary use case for this script is to calculate transcription cost, which often is
based on the overall playtime of the files submitted.

*collect_wavs.py* can be used to automatically copy all existing .wav files in a folder structure into one folder.

*scripts/convert_to_16bit.ps1* is a PowerShell script that will take all .wav files in the folder it is run in and
converts them into 16 bit wav files (converted files can be found in ./16bit).

## How To
Both *wavelength.py* and *collect_wavs.py* expose a simple click CLI interface.

`python wavelength.py --folder ./wavs --amp_threshold=100 --plot=True`

`python collect_wavs.py --scan_folder ./wavs --copy_folder ./collected_wavs`
