'''Ballot Counting
1. We have a list of unordered votes.
2. Find votes for each candidate.
3. Find winners(possibly 2 or more)
4. Minimal use of built-in functions'''

polls = ['Ben', 'Andy', 'Ben', 'Carol', 'Andy', 'Ben', 'Ben', 'Carol', 'Andy', 'Andy', 'Andy']

#Candidate list to store new candidates
candidates = []
#votes of candidate of the same index
votes = []
for person in polls:
    if person not in candidates:
        candidates.append(person)
        votes.append(1)
    else:
        candidate_index = candidates.index(person)
        votes[candidate_index] += 1

max_vote  = 0
max_candidates = []
for i in range(len(votes)):
    if votes[i]>max_vote:
        max_vote = votes[i]
        candidate = candidates[i]
        max_candidates = []
        max_candidates.append(candidate)
    elif votes[i] == max_vote:
        candidate = candidates[i]
        max_candidates.append(candidate)
print('The highest vote goes to: ')
print(*max_candidates, sep='\n')
print('The person has ' + str(max_vote) + ' votes.')
