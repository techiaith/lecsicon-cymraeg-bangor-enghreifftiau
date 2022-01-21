class Trie(object):

   def __init__(self):
      self.child = {}

   def insert(self, word):
      word = word.strip()
      current = self.child
      for l in word:
         if l not in current:
            current[l] = {}
         current = current[l]
      current['#']=1

   def search(self, word):
      word = word.strip()
      current = self.child
      for l in word:
         if l not in current:
            return False
         current = current[l]
      return '#' in current

   def startsWith(self, prefix):
      prefix = prefix.strip()
      current = self.child
      for l in prefix:
         if l not in current:
            return False
         current = current[l]
      return True

   def tostring(self):
       print("Trie structure: ")
       print(self.child)

