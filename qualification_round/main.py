import glob

import parsr, solver, scorer, writer

for idx, filename in enumerate(glob.glob('datasets/*')):
    dataset = parsr.parse(filename)
    solution = solver.solve(dataset)
    score = scorer.score(solution, dataset)
    total_score = sum(dataset['scores'])
    print(
        'Score for %s: %s/%s (%s to total score)' % (filename, score, 
            total_score, total_score - score)
    )
    writer.write(solution, filename.replace('datasets','solutions'))