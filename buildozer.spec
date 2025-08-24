[app]

# -------------------------
# Algemene app informatie
# -------------------------
title = Diversey Flappy
package.name = diverseyflappy
package.domain = org.example

# -------------------------
# Code
# -------------------------
source.dir = .
source.main = main.py

# -------------------------
# Versie en scherm
# -------------------------
version = 1.0
orientation = portrait
fullscreen = 1

# -------------------------
# Assets (nu uitgeschakeld zodat je geen icon/presplash nodig hebt tijdens debuggen)
# icon.filename =
# presplash.filename =

# -------------------------
# Vereisten
# -------------------------
requirements = python3,kivy,pillow

# -------------------------
# Android instellingen
# -------------------------
android.api = 31
android.minapi = 21
android.ndk = 25b
android.archs = arm64-v8a, armeabi-v7a

# Forceer stabiele build-tools en accepteer licenties
android.build_tools_version = 35.0.0
android.accept_sdk_license = True


[buildozer]

# -------------------------
# Buildozer instellingen
# -------------------------
log_level = 2
verbose = True
bin_dir = bin
