[app]

# (str) Title of your application
title = Diversey Flappy

# (str) Package name
package.name = diverseyflappy

# (str) Package domain (must be a valid domain)
package.domain = org.example

# (str) Source code where the main.py lives
source.dir = .

# (str) The main .py file to run
source.main = main.py

# (list) Permissions
android.permissions = INTERNET

# (list) Supported orientations
orientation = portrait

# (bool) Indicate if the application should be fullscreen
fullscreen = 1

# Android API/NDK versions
android.api = 31
android.minapi = 21
android.ndk = 25b
android.sdk_path = $ANDROID_SDK_ROOT

# (str) Supported architectures
android.archs = arm64-v8a, armeabi-v7a

# (list) Application requirements
# "python3,kivy" zijn verplicht, rest is voor jouw assets
requirements = python3,kivy,pillow

# (str) Application versioning (method 1)
version = 1.0

# (bool) Use compiled bootstrap (faster)
android.allow_backup = True

# (str) Presplash screen of the application
presplash.filename = assets/presplash.png

# (str) Icon of the application
icon.filename = assets/icon.png


[buildozer]

# (str) Log level (1 = error, 2 = warning, 3 = info, 4 = debug)
log_level = 2

# (bool) Display log messages
verbose = True

# (str) Path to build output (where .apk will be saved)
bin_dir = bin


