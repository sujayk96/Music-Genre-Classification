import os
from pydub import AudioSegment
import config

INPUT_DIR = config.ConvertWav.CONVERT_DIRECTORY
OUTPUT_DIR = INPUT_DIR + "_wav" + "/"
FILE_TYPE = config.ConvertWav.FILE_TYPE


def main():
    print("Creating new folder...")
    try:
        os.mkdir(OUTPUT_DIR)
        print("Converting files to wav format...")
        for eachdir in os.listdir(INPUT_DIR):
            print(eachdir)
            os.mkdir(OUTPUT_DIR+"/"+eachdir)
            for eachfile in os.listdir(INPUT_DIR+"/"+eachdir):
                print(INPUT_DIR+"/"+eachdir+"/"+eachfile)
                song = AudioSegment.from_file(INPUT_DIR+"/"+eachdir+"/"+eachfile, FILE_TYPE)
                song.export(OUTPUT_DIR+"/"+eachdir+"/" + eachfile[:-3] + "_wav.wav", format="wav")
        print("DONE!")
    except:
        pass


if __name__ == '__main__':
    main()