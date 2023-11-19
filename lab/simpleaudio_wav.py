import simpleaudio as sa
# Plays only the wave files


filename='./audio/sample.wav'
o=sa.WaveObject.from_wave_file(filename)
po=o.play()
po.wait_done()

