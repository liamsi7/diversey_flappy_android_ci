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

# --- Icon/presplash (mag simpele PNG's zijn; maak desnoods lege files aan) ---
icon.filename = assets/icon.png
presplash.filename = assets/presplash.png

# --- Python requirements ---
requirements = python3,kivy,pillow

# --- Android instellingen (LET OP: absolute paden, geen $ENV in deze file) ---
android.api = 31
android.minapi = 21
android.ndk = 25b

# Forceer exacte SDK/NDK paden (locaties op GitHub runner)
android.sdk_path = /usr/local/lib/android/sdk
android.ndk_path = /usr/local/lib/android/sdk/ndk/25.1.8937393

# Architecturen (breed compatibel)
android.archs = arm64-v8a, armeabi-v7a

# Licenties non-interactief
android.accept_sdk_license = True

# (optioneel) permissies
android.permissions = INTERNET


[buildozer]
log_level = 2
verbose = True
bin_dir = bin
