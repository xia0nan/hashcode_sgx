def parse(filename):
    with open(filename, 'r') as fi:
        num_books, num_libs, days = map(int, fi.readline().split())
        scores = list(map(int, fi.readline().split()))
        libraries = []

        for i in range(num_libs):
            lib_num_books, process_days, ship = map(int, fi.readline().split())
            lib_books = list(map(int, fi.readline().split()))
            lib_dict = {
                'id': i,
                'lib_num_books': lib_num_books,
                'process_days': process_days,
                'ship': ship,
                'lib_books': lib_books
            }
            libraries.append(lib_dict)

        dataset = {
            'num_books': num_books,
            'num_libs': num_libs,
            'days': days,
            'scores': scores,
            'libraries': libraries
        }
        return dataset