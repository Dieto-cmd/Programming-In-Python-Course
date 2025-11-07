from collections import deque

class Node:
    def __init__(self, char=''):
        self.char = char  # Litera w tym węźle
        self.children = {}  # Słownik: klucz=litera, wartość=Node
        self.is_end_of_word = False  # Czy kończy się tutaj jakieś słowo?
        self.pattern = None  # Jakie słowo się kończy (jeśli is_end_of_word=True)
        self.fail_link = None  # Link fail dla algorytmu AC
        self.output_link = None  # Link do najbliższego węzła kończącego słowo
    
    def add_child(self, char):
        """Dodaje dziecko z daną literą (jeśli jeszcze nie istnieje)"""
        if char not in self.children:
            self.children[char] = Node(char)
        return self.children[char]
    
    def get_child(self, char):
        """Zwraca dziecko z daną literą lub None"""
        return self.children.get(char, None)


class AhoCorasick:
    def __init__(self):
        self.root = Node()  # Korzeń drzewa trie
    
    def add_pattern(self, pattern):
        """Dodaje wzorzec do drzewa trie"""
        current = self.root
        for char in pattern:
            current = current.add_child(char)
        current.is_end_of_word = True
        current.pattern = pattern
    
    def build_fail_links(self):
        """Buduje linki fail używając BFS (algorytm Aho-Corasick)"""
        queue = deque()
        
        # Dla dzieci korzenia fail link wskazuje na korzeń
        for child in self.root.children.values():
            child.fail_link = self.root
            queue.append(child)
        
        # BFS do budowania fail links
        while queue:
            current = queue.popleft()
            
            for char, child in current.children.items():
                queue.append(child)
                
                # Szukamy fail link dla dziecka
                fail_node = current.fail_link
                while fail_node and char not in fail_node.children:
                    fail_node = fail_node.fail_link
                
                if fail_node:
                    child.fail_link = fail_node.children.get(char, self.root)
                else:
                    child.fail_link = self.root
                
                # Ustawiamy output link
                if child.fail_link.is_end_of_word:
                    child.output_link = child.fail_link
                else:
                    child.output_link = child.fail_link.output_link
    
    def search(self, text):
        """Szuka wszystkich wystąpień wzorców w tekście"""
        results = []  # Lista tupli: (wzorzec, pozycja_końca)
        current = self.root
        
        for i, char in enumerate(text):
            # Szukamy przejścia dla aktualnego znaku
            while current != self.root and char not in current.children:
                current = current.fail_link
            
            if char in current.children:
                current = current.children[char]
            
            # Sprawdzamy czy znaleźliśmy wzorzec
            node = current
            while node:
                if node.is_end_of_word:
                    results.append((node.pattern, i - len(node.pattern) + 1))
                node = node.output_link
        
        return results


# Przykład użycia
def demo():
    patterns = ["he", "she", "his", "hers"]
    text = "ahishers"
    
    ac = AhoCorasick()
    
    # Dodajemy wzorce
    for pattern in patterns:
        ac.add_pattern(pattern)
    
    # Budujemy fail links
    ac.build_fail_links()
    
    # Szukamy wzorców w tekście
    results = ac.search(text)
    
    print(f"Tekst: {text}")
    print(f"Wzorce: {patterns}")
    print(f"\nZnalezione dopasowania:")
    for pattern, position in results:
        print(f"  '{pattern}' na pozycji {position}")

if __name__ == "__main__":
    demo()