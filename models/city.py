class City:
    
    def __init__(self, name, country, visited = True, notes ,id = None):
        self.name = name
        self.country = country
        self.visited = visited
        self.notes = notes
        self.id = id

    def mark_visited(self):
        self.visited = True