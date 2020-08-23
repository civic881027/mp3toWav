from pydub import AudioSegment
import os
import sys


def mp3_to_wav(current_path, d_path):
    files = get_mp3_files(current_path)
    for i in range(0, len(files)):
        print(current_path+'/'+files[i])
        sound = AudioSegment.from_mp3(current_path + '/'+files[i])
        transName = files[i].replace('.mp3', '.wav')
        sound.export(d_path+"/"+transName, format='wav')
    return 0


def get_mp3_files(current_path):
    files = []
    for file in os.listdir(current_path):
        if not file.startswith('.') and file.endswith('.mp3'):
            files.append(file)
    return files


current_path, filename = os.path.split(sys.argv[0])
folderName = input('please enter your folder name:')
d_path = current_path+'/'+folderName

print(d_path)
try:
    os.makedirs(d_path)
except FileExistsError:
    print("folder is already exist")
mp3_to_wav(current_path, d_path)
