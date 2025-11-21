import time
from playlist_loader import load_playlist, get_current_jukebox, go_to_next_jukebox
from boss_flag import get_all_boss_statuses
from spotify_controller import play_playlist

debug = 0
poll_interval = 5

def main():
    load_playlist()

    global current_jukebox

    first_playlist = get_current_jukebox()
    if debug:
        print(f"Starting with playlist: {first_playlist}")
    play_playlist(first_playlist)

    # Save initial boss states
    previous_status = get_all_boss_statuses()

    while True:
        time.sleep(poll_interval)

        current_status = get_all_boss_statuses()

        # Detect newly defeated bosses
        for boss in current_status:
            if current_status[boss] and not previous_status[boss]:
                print(f"{boss} just died! Switching playlist.")
                go_to_next_jukebox()
                play_playlist(get_current_jukebox())

        previous_status = current_status.copy()

if __name__ == "__main__":
    main()
