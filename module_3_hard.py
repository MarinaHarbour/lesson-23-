data_structure = [[1, 2, 3], {'a': 4, 'b': 5},
                  (6, {'cube': 7, 'drum': 8}),
                  "Hello",
                  ((), [{(2, 'Urban', ('Urban2', 35))}])]


def calculate_structure_sum(data_structure):
    sum_int = 0
    sum_str = 0

    def recurse(data):
        # sum_int = 0
        # sum_str = 0
        nonlocal sum_int, sum_str
        if isinstance(data, list) or isinstance(data, tuple) or isinstance(data, set):
            for i in data:
                recurse(i)
        elif isinstance(data, dict):
            for value in data.values():
                recurse(value)
            for key in data.keys():
                recurse(key)
        elif isinstance(data, str):
            sum_str += len(data)
        elif isinstance(data, int):
            sum_int += data

    recurse(data_structure)
    return sum_int + sum_str


result = calculate_structure_sum(data_structure)
print(result)



