# Genereert transparante PNG-sprites en simpele WAV-geluiden.
# Run:  python make_assets.py
from pathlib import Path
import math, wave, struct
try:
    from PIL import Image, ImageDraw
    PIL_OK = True
except Exception:
    PIL_OK = False

assets = Path("assets"); sounds = Path("sounds")
assets.mkdir(exist_ok=True); sounds.mkdir(exist_ok=True)

# ----- Sprites (gestileerd) -----
def make_rgba(w=64, h=64):
    from PIL import Image
    return Image.new("RGBA", (w,h), (0,0,0,0))

def save_png(img, path): img.save(path, format="PNG")

def draw_bottle_oxivir():
    img = make_rgba(); d = ImageDraw.Draw(img)
    d.rounded_rectangle((18, 14, 46, 56), radius=8, fill=(85,142,213,255), outline=(20,50,90,255), width=2)
    d.rectangle((26, 6, 38, 14), fill=(200,220,255,255))
    d.rounded_rectangle((20, 30, 44, 40), radius=4, fill=(250,250,255,255))
    return img

def draw_wipes_canister():
    img = make_rgba(); d = ImageDraw.Draw(img)
    d.rounded_rectangle((16, 10, 48, 56), radius=10, fill=(180,140,220,255), outline=(80,50,120,255), width=2)
    d.ellipse((20,2,44,14), fill=(140,100,190,255))
    d.rounded_rectangle((18, 30, 46, 42), radius=6, fill=(245,235,255,255))
    return img

def draw_gallon_jug():
    img = make_rgba(); d = ImageDraw.Draw(img)
    d.rounded_rectangle((14, 16, 50, 56), radius=12, fill=(255,165,0,255), outline=(140,90,0,255), width=2)
    d.rectangle((40, 18, 50, 28), fill=(255,210,120,255))
    d.ellipse((36, 20, 46, 30), fill=(220,140,60,255))
    d.rectangle((24, 8, 40, 16), fill=(240, 200, 120,255))
    d.rounded_rectangle((18, 34, 46, 46), radius=6, fill=(255,240,210,255))
    return img

def draw_spray_bottle():
    img = make_rgba(); d = ImageDraw.Draw(img)
    d.polygon([(30,56),(18,48),(18,30),(22,24),(42,24),(46,30),(46,48)], fill=(180,220,255,200), outline=(60,120,180,255))
    d.rectangle((26,18,38,24), fill=(210,230,255,255))
    d.polygon([(24,16),(40,16),(46,12),(38,12)], fill=(90,130,200,255))
    d.rectangle((28,12,36,16), fill=(120,160,220,255))
    return img

def draw_mop_green():
    img = make_rgba(); d = ImageDraw.Draw(img)
    d.rounded_rectangle((14, 36, 50, 54), radius=8, fill=(0,166,147,255), outline=(0,100,90,255), width=2)
    for x in range(16, 50, 4): d.line((x, 54, x, 60), fill=(0,140,120,255), width=2)
    d.rectangle((30, 18, 34, 36), fill=(120, 80, 40,255))
    return img

def scale(img, s=36): 
    from PIL import Image
    return img.resize((s,s), Image.LANCZOS)

if PIL_OK:
    sprites = [
        ("oxivir_five16.png", draw_bottle_oxivir()),
        ("oxivir1_wipes.png", draw_wipes_canister()),
        ("suma_grill_d9.png", draw_gallon_jug()),
        ("water_only_bottle.png", draw_spray_bottle()),
        ("taski_mymicro_green.png", draw_mop_green()),
    ]
    for name, img in sprites:
        save_png(img, assets / name)
        save_png(scale(img, 36), assets / ("mini_" + name))
else:
    print("Pillow niet beschikbaar; sla sprite-generatie over.")

# ----- Geluiden (WAV) -----
def write_tone(path, freq=440.0, duration=0.15, volume=0.5, samplerate=44100, shape="sine"):
    n = int(duration * samplerate)
    with wave.open(str(path), "w") as wf:
        wf.setnchannels(1); wf.setsampwidth(2); wf.setframerate(samplerate)
        for i in range(n):
            t = i / samplerate
            if shape == "sine":
                s = math.sin(2*math.pi*freq*t)
            elif shape == "square":
                s = 1.0 if math.sin(2*math.pi*freq*t) >= 0 else -1.0
            else:
                s = math.sin(2*math.pi*freq*t)
            wf.writeframes(struct.pack("<h", int(max(-1,min(1,s*volume))*32767)))

def write_descend(path, f0=500, f1=180, duration=0.35):
    sr=44100; n=int(duration*sr)
    with wave.open(str(path), "w") as wf:
        wf.setnchannels(1); wf.setsampwidth(2); wf.setframerate(sr)
        for i in range(n):
            t=i/sr; f=f0 + (f1-f0)*(i/n)
            s=math.sin(2*math.pi*f*t)*0.6*(1-(i/n))
            wf.writeframes(struct.pack("<h", int(max(-1,min(1,s))*32767)))

write_tone(sounds/"flap.wav", freq=700, duration=0.08, volume=0.6)
write_tone(sounds/"point.wav", freq=1200, duration=0.12, volume=0.55)
write_tone(sounds/"powerup.wav", freq=900, duration=0.09, volume=0.6)
write_descend(sounds/"gameover.wav", f0=420, f1=150, duration=0.35)

print("Assets gegenereerd in ./assets en ./sounds")
