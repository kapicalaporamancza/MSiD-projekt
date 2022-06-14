from playlist import playlist_ids

songs = playlist_ids["items"]
songs_ids = ""
for track in songs:
    songs_ids += track["track"]["id"] + ","
songs_ids = songs_ids[:-1]
with open("ids.txt", "w") as f:
    f.write(songs_ids)
