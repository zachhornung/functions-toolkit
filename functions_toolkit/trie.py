class TrieNode:
    def __init__(self):
        self.children = {}

class TrieTree:
    def __init__(self):
        self.root = TrieNode()

    def search(self, word):
        current_node = self.root

        for char in word:
            #if the current node has a child key with the current character::
            if current_node.children.get(char):
                #then follow the child node
                current_node = current_node.children[char]
            else:
            
            # if the character isnt found in the children nodes, then the word must not be in the trie
                return None 

        return current_node

    def insert(self, word):
        current_node = self.root

        for char in word:
            #if the current node has a child key with the current character:
            if current_node.children.get(char):
                #follow it
                current_node = current_node.children[char]
                continue
                
            # if it isnt already a child node, then lets add it as a new node
            new_node = TrieNode()
            current_node.children[char] = new_node
            # and then follow it
            current_node = new_node
        #after we put the whole word into the trie, then add a * to indicate the end of a word
        current_node.children['*'] = None

    
    def collect_all_words(self, node=None, word='', words=[]):
        """
        this method accepts 3 arguments. node is the node whos descendants we are collecting words from.
        word is where the accumulated keys will go. words is where all of the accumulated strings of the second argument will go

        """
        
        current_node = node or self.root
        for key, child_node in current_node.children.items():
            #if the current key is * that means we hit the end of a complete word. that means we add it to the array
            if key == '*':
                words.append(word)
            else:
            
                self.collect_all_words(child_node, word+key, words)

        return words

    def autocomplete(self, prefix):
        current_node = self.search(prefix)
        if not current_node:
            return None 
        return self.collect_all_words(current_node)


