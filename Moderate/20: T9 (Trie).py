import collections

def find_letters(c):
    if c == "2":
        return "abc"
    elif c == "3":
        return "def"
    elif c == "4":
        return "ghi"
    elif c == "5":
        return "jkl"
    elif c == "6":
        return "mno"
    elif c == "7":
        return "pqrs"
    elif c == "8":
        return "tuv"
    elif c == "9":
        return "wxyz"

class Trie:
    def __init__(self):
        self.trie = {}
    
    def insert_word(self, word):
        trie = self.trie

        idx = 0
        while idx < len(word):
            if word[idx] not in trie:
                trie[word[idx]] = {}

            trie = trie[word[idx]]
            idx += 1

        trie["*"] = 0

    def search_words(self, code, words):
        idx = 0
        combos = []
        queue = collections.deque([("", 0, self.trie)])

        while len(queue) > 0:
            s, idx, trie = queue.popleft()

            if idx == len(code):
                combos.append(s)
                continue

            letters = find_letters(code[idx])

            for c in letters:
                if c in trie:
                    queue.append((s+c, idx+1, trie[c]))
        return combos
    
def phoneCode(Words, Sequence, W):
	# Write Your Code Here.
    
    trie = Trie()

    for word in Words:
        trie.insert_word(word)

    combos = trie.search_words(Sequence, W)
    return combos
