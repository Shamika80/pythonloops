genres = ["Rock", "Pop", "Hip Hop", "Electronic", "R&B", "Country"]

index = 0
while index < len(genres):
  track_number = index + 1
  genre = genres[index]
  print(f"Track {track_number}: Now playing {genre}!")

  if genre == "Hip Hop":
    print("Ending set on Hip Hop.")
    break

  index += 1