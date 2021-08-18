
import pytube
video_url = 'https://www.youtube.com/watch?v=6IidqsD7MeA' # paste here your Youube videos' url
youtube = pytube.YouTube(video_url)
video = youtube.streams.first()
video.download('C://Users//Harshul Gupta//Desktop//Practice//Day-5') # path, where to video download.