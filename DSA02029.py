
def tower(n, source, intermediate, des):
    if n == 1: 
        print (source, "->", des)
        return

    tower(n - 1, source, des, intermediate)
    print (source, "->", des)
    tower(n - 1, intermediate, source, des)

tower(3, 'A', 'B', 'C')
    