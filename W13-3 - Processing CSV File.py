import csv

pressures = []
num_of_lines_to_process = 1000
biggestNumber = 0
smallestNumber = 0
with open('pressure_partial.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            print(f'Column names are {", ".join(row)}')
            line_count += 1
            
        else:
          #Set biggest number to the first row of data
          if(line_count == 1):
            biggestNumber = float(row[1])

          #print(f'Pressure: \t{row[1]}')
          pressures.append([row[1],row[3]])
          #If the current value of the data is bigger than the previous biggestNumber, set biggestNumber equal to the new data value.
          if(biggestNumber<float(row[1])):
            biggestNumber = float(row[1])


          line_count += 1
          #if(line_count > num_of_lines_to_process):
            #break
    print(f'The biggest pressure (partial) is {biggestNumber}.')
#print(len(pressures))
#print(biggestNumber)
#print(f'pressure is {pressures[0][0]} at {pressures[0][1]}' )
with open('pressure_partial.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            print(f'Column names are {", ".join(row)}')
            line_count += 1
            
        else:
          #Set biggest number to the first row of data
          if(line_count == 1):
            smallestNumber = float(row[1])

          #print(f'Pressure: \t{row[1]}')
          pressures.append([row[1],row[3]])
          #If the current value of the data is bigger than the previous biggestNumber, set biggestNumber equal to the new data value.
          if(smallestNumber>float(row[1])):
            smallestNumber = float(row[1])


          line_count += 1
          #if(line_count > num_of_lines_to_process):
            #break
    print(f'The smallest pressure (partial) is {smallestNumber}.')
with open('pressure_full.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            print(f'Column names are {", ".join(row)}')
            line_count += 1
            
        else:
          #Set biggest number to the first row of data
          if(line_count == 1):
            biggestNumber = float(row[1])

          #print(f'Pressure: \t{row[1]}')
          pressures.append([row[1],row[3]])
          #If the current value of the data is bigger than the previous biggestNumber, set biggestNumber equal to the new data value.
          if(biggestNumber<float(row[1])):
            biggestNumber = float(row[1])


          line_count += 1
          #if(line_count > num_of_lines_to_process):
            #break
    print(f'The biggest pressure is {biggestNumber}.')
#print(len(pressures))
#print(biggestNumber)
#print(f'pressure is {pressures[0][0]} at {pressures[0][1]}' )
with open('pressure_full.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            print(f'Column names are {", ".join(row)}')
            line_count += 1
            
        else:
          #Set biggest number to the first row of data
          if(line_count == 1):
            smallestNumber = float(row[1])

          #print(f'Pressure: \t{row[1]}')
          pressures.append([row[1],row[3]])
          #If the current value of the data is bigger than the previous biggestNumber, set biggestNumber equal to the new data value.
          if(smallestNumber>float(row[1])):
            smallestNumber = float(row[1])


          line_count += 1
          #if(line_count > num_of_lines_to_process):
            #break
    print(f'The smallest pressure is {smallestNumber}.')

with open('temperature_full.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            print(f'Column names are {", ".join(row)}')
            line_count += 1
            
        else:
          #Set biggest number to the first row of data
          if(line_count == 1):
            biggestNumber = float(row[1])

          #print(f'Pressure: \t{row[1]}')
          pressures.append([row[1],row[3]])
          #If the current value of the data is bigger than the previous biggestNumber, set biggestNumber equal to the new data value.
          if(biggestNumber<float(row[1])):
            biggestNumber = float(row[1])


          line_count += 1
          #if(line_count > num_of_lines_to_process):
            #break
    print(f'The biggest temperature is {biggestNumber}.')
#print(len(pressures))
#print(biggestNumber)
#print(f'pressure is {pressures[0][0]} at {pressures[0][1]}' )
with open('temperature_full.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            print(f'Column names are {", ".join(row)}')
            line_count += 1
            
        else:
          #Set biggest number to the first row of data
          if(line_count == 1):
            smallestNumber = float(row[1])

          #print(f'Pressure: \t{row[1]}')
          pressures.append([row[1],row[3]])
          #If the current value of the data is bigger than the previous biggestNumber, set biggestNumber equal to the new data value.
          if(smallestNumber>float(row[1])):
            smallestNumber = float(row[1])


          line_count += 1
          #if(line_count > num_of_lines_to_process):
            #break
    print(f'The smallest temperature is {smallestNumber}.')

with open('temperature_partial.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            print(f'Column names are {", ".join(row)}')
            line_count += 1
            
        else:
          #Set biggest number to the first row of data
          if(line_count == 1):
            biggestNumber = float(row[1])

          #print(f'Pressure: \t{row[1]}')
          pressures.append([row[1],row[3]])
          #If the current value of the data is bigger than the previous biggestNumber, set biggestNumber equal to the new data value.
          if(biggestNumber<float(row[1])):
            biggestNumber = float(row[1])


          line_count += 1
          #if(line_count > num_of_lines_to_process):
            #break
    print(f'The biggest temperature (partial) is {biggestNumber}.')
#print(len(pressures))
#print(biggestNumber)
#print(f'pressure is {pressures[0][0]} at {pressures[0][1]}' )
with open('temperature_partial.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            print(f'Column names are {", ".join(row)}')
            line_count += 1
            
        else:
          #Set biggest number to the first row of data
          if(line_count == 1):
            smallestNumber = float(row[1])

          #print(f'Pressure: \t{row[1]}')
          pressures.append([row[1],row[3]])
          #If the current value of the data is bigger than the previous biggestNumber, set biggestNumber equal to the new data value.
          if(smallestNumber>float(row[1])):
            smallestNumber = float(row[1])


          line_count += 1
          #if(line_count > num_of_lines_to_process):
            #break
    print(f'The smallest temperature (partial) is {smallestNumber}.')
