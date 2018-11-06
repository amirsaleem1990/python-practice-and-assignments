def match_ends(words):
  b = 0
  for a in words:
      if len(a) >= 2:
        if a[0] == a[-1]:
          b = b + 1  
  return b

