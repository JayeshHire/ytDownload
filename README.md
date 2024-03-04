# ytDownload
### a terminal tool for downloading youtube audio, video or the thumbnail of the video.

## Installation guide
```
 python3 -m pip install --index-url https://test.pypi.org/simple/ --no-deps ytMediaDownload
```
## **or**
**use this command**

Running above command without ` python3 -m` should also work.
```
pip install --index-url https://test.pypi.org/simple/ --no-deps ytMediaDownload
```

## Guide to use this tools
After proper installation of this library is done use the below commands to use this python toolkit.
The basic syntax of the commands for this tool is as follows:
```
$ yt-media <media-type> <url>
```
Here `media-type` is the type of the download to be made. There are only three media types. They are : 
1. audio
2. video
3. thumbnail (image)

The `url` is the url of the page on which the youtube video is played.

### 1. Downloading videos
Run this command to download video from the youtube
```
$ yt-media video <url>
```
### 2. Downloading audio
Run this command to download audio file for the youtube video.
```
$ yt-media audio <url>
```
### 3. Downloading thumbnail of the video
Run this command to download the thumbnail for the youtube video.
```
$ yt-media thumbnail <url>
```
