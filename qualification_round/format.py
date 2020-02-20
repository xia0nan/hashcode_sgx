"""
parser & output data format
"""
dataset_format = {
    "num_books": 6,                     # Number of books
    "num_libs": 2,                      # Number of libraries
    "days": 7,                          # Number of days
    "scores": [1,2,3,6,5,4],            # Score of each book
    "libraries": [              
        {                               # library 0
            "id": 0,
            "lib_num_books": 5,         # currently has 5 books
            "process_days": 2,          # sign up takes 2 days
            "ship": 2,                  # ship 2 books per day
            "lib_books": [0,1,2,3,4]    # current books
        },
        {                               # library 1
            "id": 1,
            "lib_num_books": 4,         # currently has 4 books
            "process_days": 3,          # sign up takes 3 days
            "ship": 1,                  # ship 1 book per day
            "lib_books": [3,2,5,0]      # current books
        }
    ]
}

solution_format = {
    "num_libraries": 2,                 # Number of libraries used
    "libraries": [
        {
            "id": 0,
            "signup_order": 1,
            "num_book": 3,
            "process_days": 2,
            "books_order": [5,2,3]
        },
        {
            "id": 1,
            "signup_order": 0,
            "num_book": 5,
            "process_days": 3,
            "books_order": [0,1,2,3,4]
        }
    ]
}