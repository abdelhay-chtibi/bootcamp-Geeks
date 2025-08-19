import math

class Pagination:
    def __init__(self, items=None, page_size=10):
        if items is None:
            items = []
        self.items = items
        self.page_size = page_size
        self.current_idx = 0  
        self.total_pages = math.ceil(len(self.items) / self.page_size)


    def get_visible_items(self):
        start = self.current_idx * self.page_size
        end = start + self.page_size
        return self.items[start:end]
    

    def go_to_page(self, page_num):
        if page_num < 1 or page_num > self.total_pages:
            raise ValueError("Page number out of range")
        self.current_idx = page_num - 1

    def first_page(self):
        self.current_idx = 0
        return self

    def last_page(self):
        self.current_idx = self.total_pages - 1
        return self

    def next_page(self):
        if self.current_idx < self.total_pages - 1:
            self.current_idx += 1
        return self

    def previous_page(self):
        if self.current_idx > 0:
            self.current_idx -= 1
        return self
    
    def __str__(self):
        return "\n".join(str(item) for item in self.get_visible_items())
    

alphabetList = list("abcdefghijklmnopqrstuvwxyz")

p = Pagination(alphabetList, 4)

# ✅ Test 1 : Affiche les éléments de la page actuelle (page 1)
print(p.get_visible_items())  # ['a', 'b', 'c', 'd']

# ✅ Test 2 : Passer à la page suivante
p.next_page()  # Déplace de la page 1 à la page 2
print(p.get_visible_items())  # ['e', 'f', 'g', 'h']

# ✅ Test 3 : Aller à la dernière page
p.last_page()  # Déplace à la dernière page (7)
print(p.get_visible_items())  # ['y', 'z'] (car il reste 2 éléments)

# ✅ Test 4 : Aller à une page spécifique (exemple : page 3)
p.go_to_page(3)  # Déplace à la page 3
print(p.get_visible_items())  # ['i', 'j', 'k', 'l']

# ✅ Test 5 : Vérifier la position actuelle (doit être 3)
print(p.current_idx + 1)  # 3 (ajoute 1 car current_idx est basé sur 0)

# ✅ Test 6 : Cas d'erreur (aller à la page 0, invalide)
try:
    p.go_to_page(0)  # Doit lever une exception
except ValueError as e:
    print(e)  # "Invalid page number"

# ✅ Test 7 : Afficher la page actuelle avec __str__ (page 3)
print(p)  
# Affiche :
# i
# j
# k
# l

