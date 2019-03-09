
import unittest
import datetime
import genetic

def get_fitness(genes):
    return genes.count(1)


def display(candidate, startTime):
    timeDiff = datetime.datetime.now() - startTime
    print("{0}...{1}\t{2:3.2f}\t{3}".format( \
        "".join(map(str, candidate.Genes[:15])), \
        "".join(map(str, candidate.Genes[-15:])), \
        candidate.Fitness, str(timeDiff)))
    result = []
    for i in candidate.Genes:
        result += str(candidate.Genes[i])
    return result

class OneMaxTests(unittest.TestCase):
    
    def test_benchmark(self):
        genetic.Benchmark.run(lambda: self.test(4000))

    def test(self, length=100):
        geneset = [0, 1]
        startTime = datetime.datetime.now()
        def fnDisplay(candidate):
            display(candidate, startTime)
        def fnGetFitness(genes):
            return get_fitness(genes)
        optimalFitness = length
        best = genetic.get_best(fnGetFitness, length, optimalFitness, geneset, fnDisplay)
        self.assertEqual(best.Fitness, optimalFitness)




#EOF
