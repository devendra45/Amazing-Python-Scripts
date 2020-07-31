# download profile pic of any instagram user

import instaloader

mod= instaloader.Instaloader()

profile=input("Enter the username of any user: ")

mod.download_profile(mod,profile_pic_only=True)