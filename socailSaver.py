#Project_3 Download social media content using Libraries

from pytube import YouTube
import instaloader


def downProfilePic(username):
  L = instaloader.Instaloader()
  profile = instaloader.Profile.from_username(L.context, username)
  if not profile.is_private:
    L.download_profilepic(profile)
    print(f"Profile picture for {username} downloaded successfully.")
  else:
    print(f"Error: The profile for {username} is private.")


def downPost(postLink):
  L = instaloader.Instaloader()
  postlink = postLink.split("/")[-2]
  post = instaloader.Post.from_shortcode(L.context, postlink)
  if post:
    L.download_post(post, target=post.owner_username)
    print(f"Post downloaded successfully.")
  else:
    print("Error: Invalid post URL.")


def downYtVideo(link):
  video = YouTube(link)

  stream = video.streams.get_highest_resolution()

  print("Downloading:", video.title)
  stream.download()
  print("Download completed!")


def downMp3(link):
  yt = YouTube(link)
  mp3 = yt.streams.filter(only_audio=True, file_extension='mp4').first()

  if not mp3:
    print("No MP3 available for the given video.")
    return

  print("Downloading Mp3...")
  mp3.download()
  print("Download completed!")


print('''Which Type Of Content You Would Like To Download :
        1. Instagram
        2. Youtube''')
N = int(input())
while (True):
  if N == 2:
    print('''What You Want To Download From Youtube : 
            1.Video
            2.Audio''')
    X = int(input())
    if X == 1:
      videoLink = input("Enter Video Link To Be Downloaded : ")
      downYtVideo(videoLink)
    elif X == 2:
      videoLinkMp3 = input("Enter Video Link To Download Mp3 : ")
      downMp3(videoLinkMp3)
    elif X == 3:
      break
  if N == 1:

    print('''What You Want To Download From Instagram :
      1. Profile Picture
      2. Instagram Post
      3. Instagram Reel
      4. Exit''')
    M = int(input())
    if M == 1:
      username = input("Enter Your User Name To Download : ")
      downProfilePic(username)
    elif M == 2:
      postLink = input("Enter Post Link To Download : ")
      downPost(postLink)
    elif M == 3:
      reelLink = input("Enter Reel Link To Download : ")
      downPost(reelLink)
    elif M == 4:
      break
