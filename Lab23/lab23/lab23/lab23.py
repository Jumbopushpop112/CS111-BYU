import matplotlib.pyplot as plt
def plot_histogram():
    """*** YOUR CODE HERE ***"""
    listGPAs = []
    listSATs = []
    with open("admission_algorithms_dataset.csv","r") as file:
        file.readline()
        for line in file:
                line = line.split(",")
                listGPAs.append(float(line[2]))
                listSATs.append(float(line[1]))
    plt.hist(listGPAs)
    plt.savefig("gpa.png")
    plt.clf()
    plt.hist(listSATs)
    plt.savefig("sat_score.png")
    plt.clf()
def plot_scatter():
    """*** YOUR CODE HERE ***"""
    listGPAs = []
    listSATs = []
    with open("admission_algorithms_dataset.csv", "r") as file:
        file.readline()
        for line in file:
            line = line.split(",")
            listGPAs.append(float(line[2]))
            listSATs.append(float(line[1]))
    plt.scatter(listGPAs,listSATs)
    plt.savefig("correlation.png")
    plt.clf()

def plot_spectra():
    """*** YOUR CODE HERE ***"""
    listWaveLengths1 = []
    listWaveLengths2 = []
    listFluxs1 = []
    listFluxs2 = []
    with open("spectrum1.txt","r") as file:
        for line in file:
            line = line.split()
            listWaveLengths1.append(float(line[0]))
            listFluxs1.append(float(line[1]))
    with open("spectrum2.txt","r") as file:
        for line in file:
            line = line.split()
            listWaveLengths2.append(float(line[0]))
            listFluxs2.append(float(line[1]))
    plt.plot(listWaveLengths1,listFluxs1,"b")
    plt.plot(listWaveLengths2,listFluxs2,"g")
    plt.savefig("spectra.png")
    plt.clf()


def main():
    plot_histogram()
    plot_scatter()
    plot_spectra()
    pass


if __name__ == "__main__":
    main()
