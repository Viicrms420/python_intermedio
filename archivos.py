def read():
    numbers = []
    with open("/Users/VictorHugoRamirezSanchez/Downloads/python_intermedio/curso/archivos/numbers.txt", "r", encoding="utf-8") as f:
        [numbers.append(int(line)) for line in f]
        
    print(numbers)


def write():
    pass

def run():
    read
    


if __name__ == "__main__":
    run()