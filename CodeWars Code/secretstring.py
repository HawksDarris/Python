def recoverSecret(triplets):
    # Create set of unique letters
    letters = set([l for t in triplets for l in t])

    # Create dictionary where keys are letters and values are empty sets
    secret_dict = {l: set() for l in letters}

    # Update dictionary values by adding letters that come after each key
    for t in triplets:
        secret_dict[t[0]].add(t[1])
        secret_dict[t[0]].add(t[2])
        secret_dict[t[1]].add(t[2])

    # Build secret string by finding letter with no predecessors and removing it from dictionary
    secret = ''
    while secret_dict:
        for key, values in secret_dict.items():
            if not values:
                secret += key
                del secret_dict[key]
                for k, v in secret_dict.items():
                    v.discard(key)
                break

    # Reverse secret string to get correct order
    return secret[::-1]

triplets = [
  ['t','u','p'],
  ['w','h','i'],
  ['t','s','u'],
  ['a','t','s'],
  ['h','a','p'],
  ['t','i','s'],
  ['w','h','s']
]

print(recoverSecret(triplets))
