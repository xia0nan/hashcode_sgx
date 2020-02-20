def score(solution, dataset):
    processed_books = set()
    accumu_signup_days = 0
    max_days = dataset['days']
    # sort based on signup order
    libs = sorted(solution['libraries'], key=lambda k: k['signup_order'])

    for lib in libs:
        date = 0
        accumu_signup_days += lib['process_days']
        remaining_days = max_days - accumu_signup_days
        for item in lib['books_order']:
            if remaining_days > 0:
                processed_books.add(item)
            remaining_days -= 1

    processed_book_ids = list(processed_books)
    book_scores = dataset['scores']
    chosen_scores = [book_scores[index] for index in processed_books]
    return sum(chosen_scores)