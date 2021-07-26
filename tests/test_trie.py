from functions_toolkit.trie import TrieTree, TrieNode

def test_imports():
    assert TrieTree and TrieNode

def test_insert():
    trie = TrieTree()
    trie.insert('babies')
    assert trie.search('babies')

def test_collect_all_words():
    trie = TrieTree()
    trie.insert('babies')
    trie.insert('goats')
    trie.insert('chickens')
    assert trie.collect_all_words() == ['babies', 'goats', 'chickens']

def test_autocomplete():
    trie = TrieTree()
    trie.insert('babies')
    trie.insert('goats')
    trie.insert('chickens')
    trie.insert('baboons')
    trie.insert('bread')
    trie.insert('barracuda')
    trie.insert('gaudy')
    trie.insert('children')
    assert len(trie.autocomplete('c')) == 2