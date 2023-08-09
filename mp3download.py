from yt_dlp import YoutubeDL
import threading

def download(url):
    try:
        with YoutubeDL() as ydl:
            ydl.download(url)
            ydl.download(url)
    except Exception:
        pass

def urlInput():
    urlList = []
    print("Hit ENTER when complete")
    while True:
        url = input("URL: ")
        if url == "" and len(urlList) == 0:
            print("No Urls Entered")
            exit()
        if url == "":
            break
        urlList.append(url)
    print("Total number of videos: " + str(len(urlList)))
    return urlList

if __name__ == '__main__':
    threadList = list()
    urls = urlInput()
    for url in urls:
        thread = threading.Thread(target=download, args=(url,))
        threadList.append(thread)
        thread.start()

    for thread in threadList:
        thread.join()

