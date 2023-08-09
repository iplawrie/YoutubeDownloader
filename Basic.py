from pytube import YouTube

url = input()

video = YouTube(url)
stream = video.streams.get_highest_resolution()
stream.download()