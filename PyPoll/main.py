import os
import csv


csvpath = os.path.join('Resources', 'election_data.csv')

with open(csvpath,'r')as csvfile: #reads desired csv file
    csvreader = csv.DictReader(csvfile, delimiter=',')#turns csv file to dictionary

    totalvotes = 0

    candidates = []

    candidates_dict = {"Khan":0, "Correy":0, "Li":0, "O'Tooley":0}


    for row in csvreader: # for loop that adds 1 per row to 'totalvotes'
        totalvotes = totalvotes + 1
        candidates_dict[row['Candidate']] += 1 #adds 1 vote for each ballet

        if row['Candidate'] not in candidates:
            candidates.append(row['Candidate'])#finds unique candidates
    

    
    khanpercent = round((candidates_dict['Khan']/totalvotes)*100,3)

    correypercent = round((candidates_dict['Correy']/totalvotes)*100,3)

    lipercent = round((candidates_dict['Li']/totalvotes)*100,3)

    otooleypercent = round((candidates_dict["O'Tooley"]/totalvotes)*100,3)

    khantotal = candidates_dict['Khan']

    correytotal = candidates_dict['Correy']

    litotal = candidates_dict['Li']

    otooleytotal = candidates_dict["O'Tooley"]

    winner = max(candidates_dict, key = candidates_dict.get)



file = open('pythonhw.txt','w')


print("Election Results")
print("-------------------------")
print("Total Votes: " + str(totalvotes) + )
print("-------------------------")
print("Khan: " + str(khanpercent) + "%" + "(" + str(khantotal) + ")")
print("Correy: " + str(correypercent) + "%" + "(" + str(correytotal) + ")")
print("Li: " + str(lipercent) + "%" + "(" + str(litotal) + ")")
print("O'tooley: " + str(otooleypercent) + "%" + "(" + str(otooleytotal) + ")")
print("-------------------------")
print("Winner: " + str(winner) + "")
print("-------------------------")



file.write("Election Results\n")
file.write("-------------------------\n")
file.write("Total Votes: " + str(totalvotes) + "\n")
file.write("-------------------------\n")
file.write("Khan: " + str(khanpercent) + "%" + "(" + str(khantotal) + ")\n")
file.write("Correy: " + str(correypercent) + "%" + "(" + str(correytotal) + ")\n")
file.write("Li: " + str(lipercent) + "%" + "(" + str(litotal) + ")\n")
file.write("O'tooley: " + str(otooleypercent) + "%" + "(" + str(otooleytotal) + ")\n")
file.write("-------------------------\n")
file.write("Winner: " + str(winner) + "!\n")
file.write("-------------------------\n")
