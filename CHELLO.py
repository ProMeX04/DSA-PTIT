with open("result.txt", mode = "w") as out:
    out.write("Hello PTIT.")
with open("result.txt", mode = "r") as inp:
    tex = inp.read()
    print(tex)
