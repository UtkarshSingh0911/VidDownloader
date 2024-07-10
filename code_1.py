from pytube import YouTube

try:
    url = input("Enter the YouTube URL: ")
    
    link = YouTube(url)
    
    print("Title:", link.title)
    print("Views:", link.views)

    linkstream = link.streams.get_highest_resolution()

    print("Video Downloading...")
    
    linkstream.download('D:\\Work\\AAA\\projects\\ytdownload\\videos')
    
    print("Video Downloaded")
except Exception as e:
    print("An error occurred:", str(e))