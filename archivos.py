def read():
    numbers = []
    with open("archivos/numbers.txt", "r", encoding="utf-8") as f:
        for line in f:
            numbers.append(int(line))       
    print(numbers)


def write():
    names = ["facundo", "Miguel", "Pepe", "Christian", "Víctor"]
    with open("archivos/names.txt", "w", encoding="utf-8") as f:
    #para no sobreescribir
    #with open("archivos/names.txt", "a", encoding="utf-8") as f:
        for name in names:
            f.write(name)
            f.write("\n")

def run():
    write()
    


if __name__ == "__main__":
    run()