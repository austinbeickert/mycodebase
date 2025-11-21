# mycodebase
Hello, this is my collection of personal coding projects and a detailed explanation of how they work.

-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

##### data-cleanup
This is a basic data cleanup example done in SQL. These cleaned tables can now be easily analyzed in tools like Tableau.

It includes:
- creating backup raw-data tables
- converting dates
- trimming whitespace and special characters
- converting values into readable, analysis-friendly formats

-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

##### Dark Souls: The Musical
Dark Souls is my favorite game - I've played it hundreds of times. Recently, I created a playlist that loosely pairs relevant songs with where I am in the game. For example: Iron Man by Black Sabbath plays during the segment where your player fights an Iron Giant. I first did this by timing myself taking a specific, consistent route in the game and then finding relevant songs that fit in length. However, sometimes I'd accidentally die, need to retrace my steps, or take a pause. I also didn't want to manually control the music after each boss, so I created this mod to handle that for me.

This mod is written in Python and utilizes the Spotify API (and Spotipy - the Spotify Python library) to control music playback. For flexibility, ease of use, and 'Jolly Cooperation', the mod pulls playlist links from a .txt file within the mod folder, which can be edited to include any 12 playlists of your choosing.

##### -main.py
main.py is the lead controller module. It loads the current playlist and checks for new boss kills every 5 seconds. It does this by reading your PC’s virtual memory during gameplay. I used a popular free application called Cheat Engine to narrow down the exact memory values I needed. Killing a boss in Dark Souls changes multiple parts of the game. It often triggers certain dialogue options or story progressions, changes physical parts of the map, and shifts NPC locations. This means a “boss death flag” is already a value used by the game. I used this memory address to determine the playlist to queue next. 

  These flags look like this: 
    boss_flags = {"Asylum Demon": {"base_offset": 0x01C7C5F0,"offsets": [0x20, 0x0, 0x1],"bit": 7}, ....

##### -boss_flags.py
This is the bookkeeping module. It tracks boss flags and deaths for every required boss in the game, and the returned values are fed to the main controller.

Inside this module, there is one main function:
get_all_boss_statuses() - This is called by the main controller every 5 seconds. It checks each boss flag at its assigned memory segment and returns a status for each boss. This status list is saved as 'previous_status' and then compared to a new 'current_status' list every 5 seconds as the player runs through the game. When a new boss dies, the current_status now contains a new DEAD / 1 value, triggering a playlist change because it no longer matches the previous status list.

##### -playlist_loader.py & jukebox_playlists.txt
This module first vets the local jukebox_playlists.txt file to confirm there are enough playlists and then loads the first one. It contains logic to return the current playlist, skip to the next playlist, and pause playback completely. It’s important to note that this module only controls which playlist is selected - it does not trigger playback. Playback is handled by spotify_controller.py. 

##### -spotify_controller.py
This controller works in tandem with playlist_loader.py and the Spotify API to pause or resume playback. It does not control which songs or playlists are selected - only whether playback is active. As previously mentioned - playlist selectioin is handled by playlist_loader.py.

-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------   

#The Red Aisle
This is the beginning of a data scraping program using Target’s API, called “The Red Aisle.” Currently, it returns product information for a specific item from a specific ZIP code. This can be expanded with filters, automation, and a GUI to generate alerts for new deals.
