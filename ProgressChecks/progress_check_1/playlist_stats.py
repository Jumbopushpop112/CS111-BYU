import os
def computeFileData(filename):
    print(filename)
    numSongs = 0
    listTitles = []
    listArtists = []
    listPlays = []
    listDurations = []
    file = open(filename, "r")
    for line in file.readlines():
        numSongs += 1
        line = line.strip().split(",")
        listTitles.append(line[0])
        listArtists.append(line[1])
        listPlays.append(int(line[5]))
        listDurations.append(line[3])
    print(f"The playlist has {numSongs} songs.")
    print(f"The first song is {listTitles[0]} by {listArtists[0]}")
    print(f"The last song is {listTitles[len(listTitles)-1]} by {listArtists[len(listArtists)-1]}")
    maxPlays = listPlays[0]
    numHours = 0
    numMinutes = 0
    numSeconds = 0
    print(listDurations)
    i = 0
    mostPlayed = ""
    while i < len(listPlays):
        if listPlays[i] > maxPlays:
            maxPlays = listPlays[i]
            mostPlayed = listTitles[i]
        i += 1

    print(f"{mostPlayed} was played the most times at {maxPlays} plays")
    for duration in listDurations:
        if int(duration[duration.index(":") + 1:duration.index(":") + 2]) == 0:
            numSeconds += int(duration[duration.index(":") + 2:duration.index(":") + 3])
        else:
            numSeconds += int(duration[duration.index(":") + 1:len(duration)])
        numMinutes += int(duration[0:duration.index(":")])
    numSeconds += numMinutes * 60
    totalHours = numSeconds // 3600
    totalMinutes = (numSeconds % 3600) // 60
    totalSeconds = numSeconds % 60
    if totalSeconds < 10:
        print(f"The playlist is {totalHours}:{totalMinutes}:0{totalSeconds} long")
    else:
        print(f"The playlist is {totalHours}:{totalMinutes}:{totalSeconds} long")
def main():
    fileName = os.getcwd() + "/" + input("Enter the filename of the playlist in .csv format:")
    computeFileData(fileName)
if __name__ == "__main__":
    main()