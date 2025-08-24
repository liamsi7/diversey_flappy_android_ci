[app]

title = Diversey Flappy
package.name = diverseyflappy
package.domain = org.example

source.dir = .
source.main = main.py

version = 1.0
orientation = portrait
fullscreen = 1

# Belangrijk: geen icon/presplash hier, om PIL/placeholder gedoe te vermijden
# icon.filename =
# presplash.filename =

requirements = python3,kivy,pillow

# Android – gebruik de vooraf geïnstalleerde SDK/NDK
android.api = 31
android.minapi = 21
android.ndk = 25b
android.sdk_path = $ANDROID_SDK_ROOT

# Architecturen
android.archs = arm64-v8a, armeabi-v7a

# Permissies (pas aan indien nodig)
android.permissions = INTERNET


[buildozer]
log_level = 2
verbose = True
bin_dir = bin
