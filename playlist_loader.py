from spotify_controller import pause_playlist
jukebox_playlists = []
current_jukebox = 0
debug = 1

#Playlist_loader
#main function to populate jukebox_playlist from file
def load_playlist():
    global jukebox_playlists, current_jukebox
    jukebox_playlists = []
    current_jukebox = 0

    try:
        with open("jukebox_playlists.txt", "r") as file:
            for line in file:
                playlist = line.strip()
                if playlist != "":
                    jukebox_playlists.append(playlist)
        
        if len(jukebox_playlists) < 12:
            print(f"You don't have enough playlists, you only have {len(jukebox_playlists)} but need 12 for each act of the musical\n")
        else:
            print(f"{len(jukebox_playlists)} playlists loaded\n")
            if debug:
                print(f"DEBUG: loaded {jukebox_playlists}")
            
    except FileNotFoundError:
        print("Error: jukebox_playlists.txt not found.\n")

def get_current_jukebox():
    return jukebox_playlists[current_jukebox]

def go_to_next_jukebox():
    global current_jukebox
    if current_jukebox + 1 < len(jukebox_playlists):
        current_jukebox += 1
        print("Jukebox skipping to next tracklist.\n")
    else:
        print("No more tracklists left to switch to.\n")
        pause_playlist()
    

if debug:
    load_playlist()
    print(f"DEBUG: Now Playing: Jukebox #{current_jukebox} ", get_current_jukebox())
    go_to_next_jukebox()
    print(f"DEBUG: Now Playing: Jukebox #{current_jukebox} ", get_current_jukebox())