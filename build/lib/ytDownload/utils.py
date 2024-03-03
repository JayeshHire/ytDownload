from pytube import YouTube
from PIL import Image
import requests
import io
 
 
#testing remaining
class ContentDownload :
    url : str
    filename_audio : str | None
    filename_video : str | None
    filename_thumbnail : str | None
    path_to_store : str | None

    def __init__(self, url : str = None, filename_audio : str = None,\
                  filename_video : str | None= None,\
                      filename_thumbnail: str | None=None,\
                          path_to_store : str | None= None):
        self.url = url
        self.filename_audio = filename_audio
        self.filename_thumbnail = filename_thumbnail
        self.filename_video = filename_video
        self.path_to_store = path_to_store


    def download_audio(self) -> int :
        yt = YouTube(self.url)
        stream = yt.streams.filter(only_audio=True)
        itag = stream[0].itag
        file = yt.streams.get_by_itag(itag)
        file.download(output_path=self.path_to_store, filename=self.filename_audio)
        return 0
        

    def download_video(self) -> int:
        yt = YouTube(self.url)
        stream = yt.streams
        itag = stream[0].itag
        file = yt.streams.get_by_itag(itag)
        file.download(output_path=self.path_to_store, filename=self.filename_video)
        return 0

    def download_thumbnail(self) -> int:
        yt = YouTube(self.url)
        thumbnail_url = yt.thumbnail_url
        image_content = requests.get(thumbnail_url).content
        image_file = io.BytesIO(image_content)
        image = Image.open(image_file).convert('RGB')
        image.save("{}/{}".format(self.path_to_store, self.filename_thumbnail)\
                   , "PNG", quality=80)
        return 0
    
    @property
    def filename_audio(self):
        print("Getting audio file name ...")
        return self._filename_audio
    
    @filename_audio.setter
    def filename_audio(self, filename) :
        print("Setting audio file new name...")
        try:
            if filename[-4::] != '.mp3':            
                raise ValueError("Audio file name is not valid ...")
        except :
            print("audio file name is set to NoneType for now ..")
        self._filename_audio = filename

    @property
    def filename_video(self):
        print("Getting the file name ....")
        return self._filename_video
    
    @filename_video.setter
    def filename_video(self, filename) :
        print("Setting video file new name ...")
        try:
            if filename[-4::] != '.mp4':
                raise ValueError("Video file name is not valid ...")
        except:
            print("video file name is set to NoneType for now ...")
        self._filename_video = filename 

    @property
    def filename_thumbnail(self):
        print("Getting thumbnail file name ...")
        return self._filename_thumbnail
    
    @filename_thumbnail.setter
    def filename_thumbnail(self, filename) :
        print("Setting the thumbnail file name ...")
        # if filename[-4::] != ".png" or filename[-4::] != ".jpg" or \
        #     filename[-5::] != ".jpeg" :
        #     raise ValueError("Image file name is not valid ...")
        self._filename_thumbnail = filename 

    @property
    def url(self):
        print("Getting the url value...")
        return self._url
    
    @url.setter
    def url(self, value) :
        print("setting the url value ...")
        self._url = value 

    @property
    def path_to_store(self):
        print("Getting the storage path value ...")
        return self._path_to_store
    
    @path_to_store.setter
    def path_to_store(self, path) :
        print("Setting the path value for file storage ....")
        self._path_to_store = path 

    