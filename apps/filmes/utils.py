import unicodedata

def normalize(value):
  return unicodedata.normalize('NFKD', value).encode('ASCII', 'ignore').decode('utf-8')