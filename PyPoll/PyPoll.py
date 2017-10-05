total_voted = 0
total_candidate_list = []
uniq_candidate_list = []
vote_count_per_candidate_list = []
avrge_vote_list = []
with open('/Users/afnanchowdhury/Desktop/GW Bootcamp/Python/python-challenge/PyPoll/raw_data/election_data_2.csv', 'r') as infile:
    infile.readline()  #skipping the first line, Header
    for row in infile:  #looping between rows
        total_voted = total_voted + 1   #counting total rows or voters
        row_index = row.rstrip().split(',')   #spliting the rows to make a list
        total_candidate_list.append(row_index[2])  #puting candidates names including duplicate into a list
    for candidate in total_candidate_list:   # looping between newly created list
        if candidate not in uniq_candidate_list: #applying the condition to get the uniq name
            uniq_candidate_list.append(candidate) #creating new list with uniq names

#print(uniq_candidate_list)
print(
    '''Election Results
-------------------------''')
print ('Total Votes:', total_voted)
print('-------------------------')

for vote_count_per_candidate in uniq_candidate_list: # looping between list of candidates names including duplicate
    vote_count_per_candidate_list.append(total_candidate_list.count(vote_count_per_candidate)) #making a list of how many time candidate names came int he list to get the total vote count for each candidate
vote_count_per_candidate_dict = dict(zip(uniq_candidate_list,vote_count_per_candidate_list)) #making a dict with zip between uniq name and their respective count

for keys in vote_count_per_candidate_dict: #taking the output as mentioned on the example
    avrge_vote = (float(vote_count_per_candidate_dict[keys]))/(float(sum(vote_count_per_candidate_dict.values()))) * 100
    avrge_vote_list.append(avrge_vote)
    print(keys,': ',str("{0:.2f}".format(avrge_vote)) + '%','('+str(vote_count_per_candidate_dict[keys])+')')

for keys in vote_count_per_candidate_dict:
    if vote_count_per_candidate_dict[keys] == max(vote_count_per_candidate_dict.values()):

        print('-------------------------''')
        print ('winner:', keys)
        print('-------------------------')

#print(vote_count_per_candidate_dict)
#print(vote_count_per_candidate_dict[keys])
#print(vote_count_per_candidate_dict.get(keys))
#print(vote_count_per_candidate_dict.values())
#print(max(vote_count_per_candidate_dict.values()))

