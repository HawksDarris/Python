def duplicate_count(text):
  return len([char for char in set(text.lower()) if text.lower().count(char)>1])

print(duplicate_count("hello"), '\'hello\' should return 1 because \'l\' happens twice')
