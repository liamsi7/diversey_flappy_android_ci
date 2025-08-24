[app]
title = Diversey Flappy
package.name = diverseyflappy
package.domain = org.example
source.dir = .
source.main = main.py
version = 1.0
orientation = portrait
fullscreen = 1
requirements = python3,kivy,pillow
android.api = 31
android.minapi = 21
android.ndk = 25b
android.sdk_path = $ANDROID_SDK_ROOT
android.archs = arm64-v8a, armeabi-v7a
icon.filename = assets/icon.png
presplash.filename = assets/presplash.png

[buildozer]
log_level = 2
verbose = True
bin_dir = bin

