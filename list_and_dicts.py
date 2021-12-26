def run():
    my_list = [1, "Hello", True, 4.5]
    my_dict = {"firstname": "Víctor", "lastname": "Ramírez"}

    super_list = [
        {"firstname": "Víctor", "lastname": "Ramírez"},
        {"firstname": "Miguel", "lastname": "Torres"},
        {"firstname": "Pepe", "lastname": "Rodelo"},
        {"firstname": "Susana", "lastname": "Martinez"},
        {"firstname": "José", "lastname": "Ramírez"},
    ]
    super_dict = {
        "natural_nums": [1, 2, 3, 4, 5],
        "integer_nums": [-1,-2, 0, 1, 2],
        "floating_nums": [1.1, 4.5, 6.43],
    }

    for key, value in super_dict.items():
        print(key, "-", value)

    for elem in super_list:
        for key, value in elem.items():
            print(key, " -> ", value);

if __name__ == "__main__":
    run()