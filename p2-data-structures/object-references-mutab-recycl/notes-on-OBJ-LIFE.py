import weakref

if __name__ == '__main__':
    s1 = {1, 2, 3}
    s2 = s1


    def bye():
        print("... Kullu object za'ikatul mawt!")


    # track variables
    ender = weakref.finalize(s1, bye)  # this holds a weak reference to the object {1,2,3} which doesn't
    # increase the reference count
    del s1
    print("il existe toujours une reference de l'objet?", ender.alive)
    s2 = "bwahahahaha"

    print("il existe toujours une reference de l'objet?", ender.alive)
