class Film:
    def __init__(self, name):
        self.name = name
        
    def watch(self):
        print("Bon visionnage")
    

class FilmCassette(Film):
    def __init__(self, name):
        self.name = name
        self.magnetic_tape = True
        
    def rewind(self):
        print("c'est le long rebobinage")
        self.magnetic_tape = True                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   


film = Film("2001: l'olidyse de paris")
film_cass = FilmCassette("Ong back")

film.name
film.watch()

film_cass.name
film_cass.watch()


print(film_cass.name)
print(film_cass.magnetic_tape)
film_cass.watch()
film_cass.rewind()