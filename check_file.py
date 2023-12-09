from pydub import AudioSegment
def check_wav():
    file=''
    if file!='.wav':
        new_wav=AudioSegment.from_mp3(file)
        new_wav.export("", format="wav")
    else:
        return "It's a WAV!"


