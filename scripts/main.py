






def main():

    stations = {}
    with open('../data/measurements.txt', 'r') as file:
        file_contents = file.read()

    for station_line in file_contents.splitlines():
        station_list = station_line.split(';')
        station_name = station_list[0]
        station_temp = float(station_list[1])
        if(stations.get(station_name) == None):
            stations[station_name] = (station_temp, 1, station_temp, station_temp)
        else:

            if(station_temp < stations[station_name][2]):
                min = station_temp
            else:
                min = stations[station_name][2]
            if(station_temp > stations[station_name][3]):
                max = station_temp
            else:
                max = stations[station_name][3]


            stations[station_name] = (stations[station_name][0] + station_temp, stations[station_name][1] + 1, min, max)


    print("{", end="")
    for station in sorted(stations.keys()):
          print(f"{station}={stations[station][2]}/{(stations[station][0] / stations[station][1]):.1f}/{stations[station][3]}", end=", ")
    print("}")

        
if __name__ == "__main__":
    main()
