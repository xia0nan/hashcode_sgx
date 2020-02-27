import glob
from solver import greedy, knapsolve, rebuild, solvemc
import parser, scorer, writer

for idx, filename in enumerate(glob.glob('datasets/*')):
    dataset = parser.parse(filename)
    solution = solvemc(dataset)
    score = scorer.score(solution, dataset)
    print('Score for %s: %s/%s (%s to perfect score)' % (filename, score, dataset['knapsize'], dataset['knapsize'] - score))
    writer.write(solution, filename.replace('datasets','solutions'))
