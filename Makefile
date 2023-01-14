download:
	wget http://www.pmonta.com/data/cd/cd-stitched.png

process:
	python track.py
	python resample.py <waveform.dat >channel-symbols.dat
	python nrzi.py <channel-symbols.dat >channel-bits.dat
	python efm-decode.py <channel-bits.dat >frames.dat
	python c1-decode.py <frames.dat >c1-codewords.dat

clean:
	rm -f waveform.dat channel-symbols.dat channel-bits.dat frames.dat c1-codewords.dat
	rm -f *~
	rm -rf __pycache__
