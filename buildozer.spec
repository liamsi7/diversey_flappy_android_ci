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

# --- Icon/presplash (mag leeg/simple png zijn) ---
icon.filename = assets/icon.png
presplash.filename = assets/presplash.png

# --- Python requirements ---
requirements = python3,kivy,pillow

# --- Android instellingen ---
android.api = 31
android.minapi = 21
android.ndk = 25b
# Dwing Buildozer om de vooraf geïnstalleerde SDK te gebruiken
android.sdk_path = $ANDROID_SDK_ROOT

# Architecturen
android.archs = arm64-v8a, armeabi-v7a

# Permissies (voeg toe indien nodig)
android.permissions = INTERNET


[buildozer]
log_level = 2
verbose = True
bin_dir = bin
