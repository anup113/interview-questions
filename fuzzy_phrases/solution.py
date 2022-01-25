import json

'''
The complexity of creating the trie data structure is O(n * k) where n is the number of phrases we have and k is the average number of words in the phrase. 

The time complexity of the searching is linear as we only run through the query words for once and look in the trie to find the match. 
'''


class Trie:
    def __init__(self):
        self.trie = {}

    # add the phrase in the trie data structure "#" represents end of phrase
    def add(self, phrase):
        phrase = phrase.split(' ')
        node = self.trie
        for i in phrase:
            if i not in node:
                node[i] = {}
            node = node[i]
        node['#'] = True

    # search the query wrods in the trie data structure
    def search(self, words):
        words = words.split(' ')
        n, curr = len(words), 0
        one = 0
        node = self.trie
        res = []
        ans = []
        while curr < n:
            word = words[curr]
            if word in node or (len(res) > 0 and one < 1):
                if word in node:
                    res.append(word)
                    node = node[word]
                    if '#' in node and node['#']:
                        ans.append(' '.join(res))
                        res = []
                        one = 0
                else:
                    res.append(word)
                    one += 1
            else:
                node = self.trie
                if one != 0:
                    curr -= 1
                res = []
                one = 0
            curr += 1
        return ans


def phrasel_search(P, Queries):

    ans = []

    # Create a trie object
    t = Trie()

    # add all the phrases in the Trie
    for phrase in P:
        t.add(phrase)

    # search all the queries
    for q in Queries:
        ans.append(t.search(q))

    return ans


if __name__ == "__main__":
    with open('fuzzy_phrases/sample.json', 'r') as f:
        sample_data = json.loads(f.read())
        P, Queries, sol = sample_data['phrases'], sample_data['queries'], sample_data['solution']
        returned_ans = phrasel_search(P, Queries)
        if sol == returned_ans:
            print('============= ALL TEST PASSED SUCCESSFULLY ===============')
