import instaloader

k=instaloader.Instaloader()

username='keerthi_dhanush'
print(k.download_profile(username,profile_pic_only=True))