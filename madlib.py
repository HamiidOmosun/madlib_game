#madlib game 
#steps to creating this game
#ask users to input the game the want to play 
#create a list of games user can choose from

def dream_adventure():

  noun = input("noun: ").strip().lower()
  verb1 = input("verb: ").strip().lower()
  verb2 = input("verb: ").strip().lower()
  adjective = input("adjective: ").strip().lower()
  verb3 = input("verb: ").strip().lower()
  famous_person = input("famous person: ").strip().title()

  dream_adventure= f"I love it when my {noun} goes on a {verb1}.\
  One of the craziest things about {verb2} is that nobody ever understands it.\
  I just want to feel {adjective} and get {verb3} by {famous_person}."

  print(dream_adventure)

def space_mission():
  adjective = input("adjective: ").strip().lower()
  animal = input("animal: ").strip().lower()
  verb1 = input("verb: ").strip().lower()
  adjective2 = input("verb: ").strip().lower()
  noun = input("noun: ").strip().lower()
  emotion = input("emotion").strip().lower()

  space_mission = f"Yesterday, I boarded a {adjective} rocket ship with my pet {animal}.\
  We {verb1} past the moon and saw a {adjective2} alien dancing with a {noun}.\
  It was the most {emotion} thing I've ever seen."

  print(space_mission)

def hollywood_audition():
  profession = input("profession: ").strip().title()
  movie_title = input("movie title: ").strip().title()
  verb = input("verb: ").strip().lower()
  adjective = input("adjective: ").strip().lower()
  clothing_item = input("clothing item: ").strip().lower()
  celebrity = input("celebrity: ").strip().title()
  emotion = input("emotion: ").strip().lower()

  hollywood_audition = f"Today I had an audition for a role as a {profession} in a new movie called '{movie_title}'.\
  I had to {verb} while wearing a {adjective} {clothing_item}.\
  The director said I looked like {celebrity}, which made me feel {emotion}."

  print(hollywood_audition)

def wizard_school_disaster():
  verb1 = input("verb: ").strip().lower()
  magical_object = input("magical object: ").strip().lower()
  body_part = input("body part: ").strip().lower()
  animal = input("animal: ").strip().lower()
  classmate_name = input("classmate name: ").strip().title()
  adjective = input("adjective: ").strip().lower()

  wizard_school_disaster = f"At wizard school, our teacher taught us how to {verb1} a {magical_object}.\
  But I accidentally turned my {body_part} into a {animal}! Everyone laughed except {classmate_name},\
  who said I was the most {adjective} wizard they'd ever seen."

  print(wizard_school_disaster)

def choose_madlib():
  choose_madlib = input(
    "choose menu:\n"
    "dream adventure\n"
    "space mission\n"
    "hollywood audition\n"
    "wizard school disaster\n"
    "Enter choice: "
  )

  if choose_madlib == "dream adventure":
    return dream_adventure()
  elif choose_madlib == "space mission":
    return space_mission()
  elif choose_madlib == "hollywood audition":
    return hollywood_audition()
  elif choose_madlib == "wizard school disaster":
    return wizard_school_disaster()
  else:
    raise Exception("you need to choose a valid game")
  

if __name__ == "__main__":
  choose_madlib()