import datetime
import random

import genetic


def get_fitness(guess, target):
    return sum(1 for expected, actual in zip(target, guess) if expected == actual)


def display(candidate, startTime):
    timeDiff = datetime.datetime.now() - startTime
    print("{}\t{}\t{}".format(candidate.Genes, candidate.Fitness, timeDiff))


class GuessPassword:
    geneset = " abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!.,"

    def test_Hello_World(self):
        target = "Hello World!"
        self.guess_password(target)

    def test_For_I_am_fearfully_and_wonderfully_made(self):
        target = "For I am fearfully and wonderfully made."
        self.guess_password(target)

    def test_Random(self):
        length = 150
        target = "".join(random.choice(self.geneset) for _ in range(length))

        self.guess_password(target)

    def test_benchmark(self):
        genetic.Benchmark.run(self.test_Random)

    def guess_password(self, target):
        startTime = datetime.datetime.now()

        def fnGetFitness(genes):
            return get_fitness(genes, target)

        def fnDisplay(candidate):
            display(candidate, startTime)

        optimalFitness = len(target)
        return genetic.get_best(
            fnGetFitness, len(target), optimalFitness, self.geneset, fnDisplay
        )


if __name__ == "__main__":
    teste = GuessPassword()
    # teste.test_benchmark()
    teste.test_For_I_am_fearfully_and_wonderfully_made()

# EOF
