"""
Naive solution:
Rank library and books by natural order
"""
def solve(dataset):
    accu_signup_days = 0
    max_dates = dataset['days']
    libs = []
    for lib in dataset["libraries"]:
        if accu_signup_days < max_dates:
            item = dict()
            item['id'] = lib['id']
            item['signup_order'] = lib['id']
            item['num_book'] = lib['lib_num_books']
            item['process_days'] = lib['process_days']
            item['books_order'] = lib['lib_books']
            libs.append(item)

    solution = dict()
    solution['num_libraries'] = len(libs)
    solution['libraries'] = libs
    return solution