genres = ["Rock", "Pop", "Classical", "Hip Hop", "Electronic", "R&B", "Country"]

for index in range(len(genres)):
  genre = genres[index]

  if genre == "Classical":
    print(f"Skipping {genre}. Not suitable for light show.")
    continue

  track_number = index + 1
  print(f"Track {track_number}: Genre {genre} - Light show ready!")
