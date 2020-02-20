import glob

import parsr, solver, scorer, writer

file_names = [
              "a_example.txt",
              "b_read_on.txt",
              "c_incunabula.txt",
              "d_tough_choices.txt",
              "e_so_many_books.txt",
              "f_libraries_of_the_world.txt"
]

for idx, filename in enumerate(glob.glob('data/*')):
    dataset = parsr.parse(filename)
    solution = solver.solve(dataset)
    score = scorer.score(solution, dataset)
    total_score = sum(dataset['scores'])
    print(
        'Score for %s: %s/%s (%s to total score)' % (filename, score, 
            total_score, total_score - score)
    )
    writer.write(solution, filename.replace('data','solutions'))
