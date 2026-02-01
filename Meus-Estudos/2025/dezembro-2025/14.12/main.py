import os
import shutil

music_base = r"C:/Users/ismae/Music/mscs_do_cll"  # Todas suas músicas aqui
playlists_base = r"C:/Users/ismae/Music/Playlists_Musicolet"  
output_base = r"C:/Users/ismae/Music/Musicas_do_celular"

def find_music_by_name(filename):
    """Procura MP3 por nome em TODA pasta Music"""
    for root, dirs, files in os.walk(music_base):
        if filename in files:
            return os.path.join(root, filename)
    return None

for playlist_file in os.listdir(playlists_base):
    if playlist_file.endswith('.m3u'):
        playlist_name = os.path.splitext(playlist_file)[0]
        playlist_folder = os.path.join(output_base, playlist_name)
        os.makedirs(playlist_folder, exist_ok=True)
        
        print(f"=== {playlist_name} ===")
        copied = 0
        
        with open(os.path.join(playlists_base, playlist_file), 'r', encoding='utf-8', errors='ignore') as f:
            for line in f:
                line = line.strip()
                if line and not line.startswith('#'):
                    # Pega só o nome do arquivo do .m3u
                    filename = os.path.basename(line)
                    
                    # Procura por qualquer lugar na pasta Music
                    song_path = find_music_by_name(filename)
                    if song_path:
                        dest = os.path.join(playlist_folder, os.path.basename(song_path))
                        shutil.copy2(song_path, dest)
                        copied += 1
                        print(f"✓ {os.path.basename(song_path)}")
                    else:
                        print(f"✗ {filename} não encontrado")
        
        print(f"Total: {copied} músicas")

print("✅ PRONTO!")