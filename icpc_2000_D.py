
def AireMinimale(Dimension,coordonnée):

    if Dimension <3 :
        return False

    else:
        if Dimension == 3 :




    distFinal, capacity, mpg, gasPrice, N, stations = par
    stations.sort()
    minCost = [INF]
    execute(0.0, capacity, int(gasPrice))
    return '%.2f' % (minCost[0] / 100.0)


class Gift_parsing:

    def getInput(self):
        self.numberTests = 0
        self.input = []
        while True:
            dist = float(self.fInput.readline())
            if dist < 0:
                break
            self.numberTests += 1
            capacity, mpg, gasPrice, N = map(
                float, self.fInput.readline().split())
            gasPrice *= 100
            N = int(N)
            stations = []
            for i in range(N):
                stations.append(map(float, self.fInput.readline().split()))

            self.input.append(
                (dist, capacity, mpg, gasPrice, N, stations))

    def __init__(self):
        self.fInput = open('test.txt')
        self.fOutput = open('output.txt', 'w')
        self.results = []
    def sequential_work(self):
        self.getInput()
        millis1 = int(round(time.time() * 1000))
        for i in self.input:
            self.results.append(solving_problem(i))
        millis2 = int(round(time.time() * 1000))
        print("Time in milliseconds: %d " % (millis2 - millis1))
        self.makeOutput()

    def makeOutput(self):
        for test in range(self.numberTests):
            self.fOutput.write("%s\n" % self.results[test])
        self.fInput.close()
        self.fOutput.close()

if __name__ == '__main__':
    solver = Budget_Solver()
    solver.sequential_work()