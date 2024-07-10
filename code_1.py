from pytube import YouTube

try:
    url = input("Enter the YouTube URL: ")
    
    link = YouTube(url)
    
    print("Title:", link.title)
    print("Views:", link.views)

    linkstream = link.streams.get_highest_resolution()

    print("Video Downloading...")
    
    linkstream.download('local directory')
    
    print("Video Downloaded")
except Exception as e:
    print("An error occurred:", str(e))

#put the location of folder in place of local directory (line 15).
