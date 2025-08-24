[app]
title = Diversey Flappy
package.name = diverseyflappy
package.domain = org.example
source.dir = .
source.main = main.py
version = 1.0
orientation = portrait
fullscreen = 1

# GEEN icon/presplash afdwingen zolang we debuggen
# icon.filename =
# presplash.filename =

requirements = python3,kivy,pillow

android.api = 31
android.minapi = 21
android.ndk = 25b
android.archs = arm64-v8a, armeabi-v7a

# Forceer stabiele build-tools + accepteer licenties
android.build_tools_version = 35.0.0
android.accept_sdk_license = True

