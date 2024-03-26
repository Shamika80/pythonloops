import random

moods = ["Happy", "Sad", "Energetic", "Calm"]

for day in range(7):
  
  random_mood = random.choice(moods)

  
  if day == 0:
    print("Today (Monday) I am feeling", random_mood)
  elif day == 1:
    print("Tomorrow (Tuesday) I am feeling", random_mood)
  elif day == 2:
    print("Wednesday I am feeling", random_mood)
  elif day == 3:
    print("Thursday I am feeling", random_mood)
  elif day == 4:
    print("Friday I am feeling", random_mood)
  elif day == 5:
    print("Saturday I am feeling", random_mood)
  else:
    print("Sunday I am feeling", random_mood)