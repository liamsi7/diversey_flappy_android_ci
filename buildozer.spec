[app]

# --- App info ---
title = Diversey Flappy
package.name = diverseyflappy
package.domain = org.example

# --- Broncode ---
source.dir = .
source.main = main.py

# --- Versie & scherm ---
version = 1.0
orientation = portrait
fullscreen = 1

# --- Assets (optioneel; laat staan ook als je deze bestanden niet hebt) ---
icon.filename = assets/icon.png
presplash.filename = assets/presplash.png

# --- Python requirements ---
# Kivy is noodzakelijk. Pillow is handig voor assets (mag blijven staan).
requirements = python3,kivy,pillow

# --- Android instellingen ---
# Forceer stabiele API’s/NDK en wijs Buildozer naar de vooraf geïnstalleerde SDK.
android.api = 31
android.minapi = 21
android.ndk = 25b
android.sdk_path = $ANDROID_SDK_ROOT

# Bouw voor 32/64-bit ARM (beide = breder compatibel)
android.archs = arm64-v8a, armeabi-v7a

# (optioneel) permissies, voeg toe indien nodig
android.permissions = INTERNET


[buildozer]
# Logging
log_level = 2
verbose = True

# Waar de APK terechtkomt
bin_dir = bin
