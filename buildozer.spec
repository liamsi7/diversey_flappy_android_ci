[app]

# --- App info ---
title = Diversey Flappy
package.name = diverseyflappy
package.domain = org.example

# --- Code ---
source.dir = .
source.main = main.py

# --- Versie & scherm ---
version = 1.0
orientation = portrait
fullscreen = 1

# --- Icon/presplash (mag simpele png zijn) ---
icon.filename = assets/icon.png
presplash.filename = assets/presplash.png

# --- Python requirements ---
requirements = python3,kivy,pillow

# --- Android instellingen (let op: ABSOLUTE PADEN, geen $ENV) ---
android.api = 31
android.minapi = 21

# Gebruik stabiele NDK 25b
android.ndk = 25b

# >>> BELANGRIJK: absolute paden ivm Buildozer variabele-expansie <<<
# Dit is waar setup-android de SDK neerzet op GitHub runners:
android.sdk_path = /usr/local/lib/android/sdk
# Zet de NDK-path expliciet naar de 25.1.8937393 map:
android.ndk_path = /usr/local/lib/android/sdk/ndk/25.1.8937393

# Architecturen
android.archs = arm64-v8a, armeabi-v7a

# Licenties niet interactief
android.accept_sdk_license = True

# Permissies (voeg toe indien nodig)
android.permissions = INTERNET


[buildozer]
log_level = 2
verbose = True
bin_dir = bin
