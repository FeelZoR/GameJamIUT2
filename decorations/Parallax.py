from decorations.CoucheParallax import CoucheParallax


class Parallax:
    class __Parallax:
        def __init__(self):
            self.__parallax = list()

            for i in range(1, 5):
                self.__parallax.append(CoucheParallax(i, 250 - 50 * i, 1.0))

        def deplacement_joueur(self, direction, delta):
            for parallax in self.__parallax:
                parallax.deplacement(direction, delta)

        def fin(self):
            for parallax in self.__parallax:
                parallax.fin()

    __instance = None

    def __init__(self):
        if not Parallax.__instance:
            Parallax.__instance = Parallax.__Parallax()

    def deplacement_joueur(self, direction, delta):
        self.__instance.deplacement_joueur(direction, delta)

    def fin(self):
        self.__instance.fin()
        Parallax.__instance = None
