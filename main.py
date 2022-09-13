from pytube import YouTube

def main():
    yt = YouTube("https://www.youtube.com/watch?v=LIZmt7SXxMM")
    print(yt.title)
    print(yt.thumbnail_url)
    print(yt.streams.filter(file_extension='mp4'))
    stream = yt.streams.get_by_itag(int(input("ID потока: ")))
    stream.download(filename="видос.mp4")

if __name__ == "__main__":
    main()