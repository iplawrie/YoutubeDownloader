from pytube import YouTube, Playlist

url = input()
p = Playlist(url)
for video in p.videos:
    print(video.title)