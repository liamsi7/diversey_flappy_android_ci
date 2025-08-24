[app]

title = Diversey Flappy
package.name = diverseyflappy
package.domain = org.example
source.dir = .
source.main = main.py
orientation = portrait
fullscreen = 1
version = 1.0

# Vereisten (minimaal)
requirements = python3,kivy,pillow

# Android instellingen
android.api = 31
android.minapi = 21
android.ndk = 23b
android.sdk = 6609375

# Architecturen
android.archs = arm64-v8a, armeabi-v7a

# Icon en presplash (maak lege png’s als je geen echte hebt)
icon.filename = assets/icon.png
presplash.filename = assets/presplash.png

[buildozer]
log_level = 2
verbose = True
bin_dir = bin
