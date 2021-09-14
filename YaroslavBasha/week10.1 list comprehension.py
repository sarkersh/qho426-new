def readcsv(filename, rows, cols):
    print('Reading from', filename)
    data = []
    with open(filename, 'r') as f:
        f.readlines()
        for i in range(0, rows):
            line = f.readline().strip().split(',')
            output = []
            for x in cols:
                output.append(line[x])
            data.append(output)
            print(data)

    return data

print(readcsv('sol_data.csv', 3, [21,4]))
