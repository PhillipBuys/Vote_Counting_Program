candidate_A = 0
candidate_B = 0
candidate_C = 0
candidate_D = 0
candidate_E = 0
spoiled_votes = 0
total_votes = 0

while True:
    choice = int(input())
    if choice == 0:
        break
    elif choice == 1:
        candidate_A += 1
    elif choice == 2:
        candidate_B += 1
    elif choice == 3:
        candidate_C += 1
    elif choice == 4:
        candidate_D += 1
    elif choice == 5:
        candidate_E += 1
    else:
        spoiled_votes += 1
        continue

print(f"Candidate A:{candidate_A}")
print(f"Candidate B:{candidate_B}")
print(f"Candidate C:{candidate_C}")
print(f"Candidate D:{candidate_D}")
print(f"Candidate E:{candidate_E}")
print(f"Invalid:{spoiled_votes}")