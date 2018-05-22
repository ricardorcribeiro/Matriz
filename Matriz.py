
import wave
from pydub import AudioSegment
from pydub.silence import split_on_silence
import os
from scipy.io.wavfile import read


THIS_FOLDER = os.path.abspath('')

print(THIS_FOLDER)

min_silence_len = 100
silence_thresh = -30

sound_file = AudioSegment.from_wav("ab.wav")

toMaximo = sound_file.max_possible_amplitude
racao = sound_file.duration_seconds
vefile = wave.open("ab.wav", 'r')
#nframes = wavefile.getnframes()#total de frames
#framerate = wavefile.getframerate()#media de frames

fs, data = read('ab.wav')
data_size = len(data)

#data = data / (2.**15)

varia = data.shape

varia2 = varia[0] / fs #aqui estou pegando a duraçao do audi. mediçao em ms(milésimo de segundo)

focus_size = int(0.15 * fs)

audio_chunks = split_on_silence(sound_file, min_silence_len, silence_thresh)

matriz = []

for i, chunk in enumerate(audio_chunks):
    linha = []
    nome = "silvio"
    pontoMaximo = chunk.max_possible_amplitude
    mediaFrame = chunk.frame_rate
    amplitude = chunk.max
    mediaItencidade = chunk.rms
    naosei = chunk.raw_data
    tamanho = len(naosei)
    linha.append(nome)
    linha.append(pontoMaximo)
    linha.append(mediaFrame)
    linha.append(amplitude)
    linha.append(mediaItencidade)
    matriz.append(linha)

'''
    out_file = "NovoAudio/chunk{0}.wav".format(i)
    print("exporting", out_file)
    chunk.export(out_file, format="wav")
'''