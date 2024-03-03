import sys
from ytDownload import utils


class MainProgram :
    loader_instance = utils.ContentDownload()
    filename : str
    location : str

    @staticmethod
    def audio_download(url):
        MainProgram.storage_info()
        setattr(MainProgram.loader_instance, 'filename_audio', MainProgram.filename)
        setattr(MainProgram.loader_instance, 'path_to_store', MainProgram.location)
        setattr(MainProgram.loader_instance, 'url', url)
        MainProgram.loader_instance.download_audio()
        pass

    @staticmethod
    def video_download(url):
        MainProgram.storage_info()
        setattr(MainProgram.loader_instance, 'filename_video', MainProgram.filename)
        setattr(MainProgram.loader_instance, 'path_to_store', MainProgram.location)
        setattr(MainProgram.loader_instance, 'url', url)
        MainProgram.loader_instance.download_video()
        pass

    @staticmethod
    def thumbnail_download(url):
        MainProgram.storage_info()
        setattr(MainProgram.loader_instance, 'filename_thumbnail', MainProgram.filename)
        setattr(MainProgram.loader_instance, 'path_to_store', MainProgram.location)
        setattr(MainProgram.loader_instance, 'url', url)
        MainProgram.loader_instance.download_thumbnail()
        pass

    @staticmethod
    def storage_info():
        MainProgram.filename = input("Enter the name of the file (for video and audio files .mp3 and .mp4 format must be mentioned) :\n")
        MainProgram.location = input("Enter the path to store the file :\n")

    @staticmethod
    def main():
        if sys.argv[1] == "audio" :
            url = sys.argv[2]
            MainProgram.audio_download(url)
        elif sys.argv[1] == "video" :
            url = sys.argv[2]
            MainProgram.video_download(url)
        elif sys.argv[1] == "thumbnail" :
            url = sys.argv[2]
            MainProgram.thumbnail_download(url)

def main():
    main_prog = MainProgram()
    MainProgram.main()
    print("\n\n\t\t\t Sucessfully downloaded the media ....\n")
    

if __name__ == "__main__" :
    main()



