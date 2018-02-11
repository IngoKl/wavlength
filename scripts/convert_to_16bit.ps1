$wav_files = Get-ChildItem . -Filter *.wav
New-Item -ItemType directory -Path ./16bit

ForEach( $file in $wav_files ) { 
	$wav_file = $file.Name
	$wav_file_new = "16bit/" + $file.Name.Split(".")[0] + "-16b.wav"
	sox $wav_file -b16 $wav_file_new
}