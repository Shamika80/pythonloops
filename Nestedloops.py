import random

moods = ["Happy", "Sad", "Energetic", "Calm"]

daynames = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

for day in range(7):
  print(f"\n{daynames[day]} Moods:")  

  
  for time_of_day in ["Morning", "Afternoon", "Evening"]:

    random_mood = random.choice(moods)
    print(f"\t{time_of_day}: {random_mood}")