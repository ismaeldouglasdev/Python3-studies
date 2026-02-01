import os

music_base = r"C:\Users\ismae\Music\mscs_do_cll\2k15 v2 _springbreak(M4A_128K).m4a" # AJUSTE
playlist_path = r"C:\Users\ismae\Music\Playlists_Musicolet\#PEAK.m3u"  # AJUSTE 1 .m3u

print("=== DEBUG ===")
print("Pasta Music existe?", os.path.exists(music_base))

with open(playlist_path, 'r', encoding='utf-8', errors='ignore') as f:
    for i, line in enumerate(f):
        line = line.strip()
        if line and not line.startswith('#') and i < 3:  # Primeiras 3 linhas
            print(f"Linha .m3u: {line}")
            print("Caminho esperado:", os.path.join(music_base, line.lstrip('/storage/emulated/0/')))