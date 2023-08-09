from pytube import YouTube, Playlist
import time
import threading

#get what url selector
def urlSelector():
    while True:
        selector = input("1. Urls\n 2. Playlist")
        if selector.isdigit():
            if int(selector) == 1 or int(selector) == 2:
                break
        print("Invalid Selector")
    return selector

#get what codec to use for download
def codecInput():
    while True:
        codec = input("1. Audio\n2. Video\n")
        if codec.isdigit():
            if int(codec) == 1 or int(codec) == 2:
                break
        print("Invalid Codec")
    return codec

#get the list of urls
def urlListInput():
    youtubelist = []
    print("Hit ENTER when complete")
    while True:
        try:
            url = input("URL: ")
            if url == "" and len(youtubelist) == 0:
                print("No Urls Entered")
                exit()
            if url == "":
                break
            video = YouTube(url)
            youtubelist.append(video)
        except Exception as e:
            print(e)
        youtubelist.append(input("URL: "))
    print("Total number of videos: " + str(len(youtubelist)))
    return youtubelist

#get playlist url
def playlistInput():
    playlist = None
    try:
        playlist = Playlist(input("URL: "))
    except Exception as e:
        print(e)
    print("Total number of videos: " + str(len(playlist)))
    return playlist

#download specified urls
def downloadPlaylist(playlist, codec):
    for video in playlist.videos:
        try:
            stream = None
            if codec == 1:
                stream = video.streams.get_audio_only()
            elif codec == 2:
                stream = video.streams.get_highest_resolution()
            else:
                print("Codec Argument Invalid")
            print("Downloading")
            print("TITLE: " + video.title)
            print("LENGTH: " + time.strftime("%H:%M:%S", time.gmtime(video.length)))
            stream.download("D:\Downloads")
            print("Downloaded")

        except Exception as e:
            print(e)

def downloadUrls(youtubeList, codec):
    for video in youtubeList:
        try:
            stream = None
            if codec == 1:
                stream = video.streams.get_audio_only()
            elif codec == 2:
                stream = video.streams.get_highest_resolution()
            else:
                print("Codec Argument Invalid")
            print("Downloading")
            print("TITLE: " + video.title)
            print("LENGTH: " + time.strftime("%H:%M:%S", time.gmtime(video.length)))
            stream.download("D:\Downloads")
            print("Downloaded")
        except Exception as e:
            print(e)


if __name__ == '__main__':
    selector = int(urlSelector())
    codec = int(codecInput())
    if selector == 1:
        youtubeList = urlListInput()
        downloadUrls(youtubeList, codec)
    elif selector == 2:
        playlist = playlistInput()
        downloadPlaylist(playlist, codec)
    else:
        print("Selector Argument Invalid")
