# Download Instagram Profile Photo
This Python script `Download Instagram Profile Photo.py` utilizes the Instaloader library to download profile photos from Instagram.

## Prerequisites
Before using the script, ensure you have Python installed on your system. Additionally, you'll need to install the Instaloader library. You can install it using pip:

pip install instaloader

## Instructions
1. Clone or download the script to your local machine.
2. Open the script in your preferred Python editor or IDE.
3. Modify the `username` variable to the desired Instagram username whose profile photo you want to download.
4. Run the script.

## Usage
The script downloads the profile photo of the specified Instagram user. It utilizes the `download_profile` method from the Instaloader library. By setting `profile_pic_only` to `True`, it only downloads the profile picture.

## Example
python
import instaloader

# Create an instance of Instaloader
k = instaloader.Instaloader()

# Specify the Instagram username
username = 'keerthi_dhanush'

# Download the profile photo
print(k.download_profile(username, profile_pic_only=True))

## Disclaimer
This script is provided as-is without any warranty. Use it responsibly and respect Instagram's terms of service and user privacy.

Feel free to reach out with any questions, suggestions, or improvements!
