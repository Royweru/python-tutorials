def solution(P, Q):
    N = len(P)
    
    # Check if we can use just one letter
    all_letters = set(P + Q)
    for letter in all_letters:
        can_use_one = True
        for i in range(N):
            if P[i] != letter and Q[i] != letter:
                can_use_one = False
                break
        if can_use_one:
            return 1
    
    # Build the set of options for each position
    position_options = [set() for _ in range(N)]
    for i in range(N):
        position_options[i].add(P[i])
        position_options[i].add(Q[i])
    
    # Build the bipartite graph: letters -> positions they can cover
    letter_to_positions = {}
    for letter in all_letters:
        letter_to_positions[letter] = set()
    
    for i in range(N):
        for letter in position_options[i]:
            letter_to_positions[letter].add(i)
    
    # Greedy algorithm to find minimum set cover
    remaining_positions = set(range(N))
    letters_used = set()
    
    while remaining_positions:
        # Find the letter that covers the most remaining positions
        best_letter = None
        max_coverage = 0
        
        for letter in all_letters:
            if letter in letters_used:
                continue
            
            coverage = len(remaining_positions.intersection(letter_to_positions[letter]))
            if coverage > max_coverage:
                max_coverage = coverage
                best_letter = letter
        
        if best_letter is None:
            # No letter covers any remaining position - this shouldn't happen
            # given the problem constraints
            break
        
        # Add this letter to our solution
        letters_used.add(best_letter)
        
        # Remove positions that are now covered
        remaining_positions -= letter_to_positions[best_letter]
    
    return len(letters_used)

# Test cases
test_cases = [
    ("abc", "bcd"),  # Should return 2
    ("axxz", "yzwy"),  # Should return 2
    ("bacad", "abada"),  # Should return 1
    ("amz", "amz"),  # Should return 3
]

for P, Q in test_cases:
    print(f"P={P}, Q={Q}, result={solution(P, Q)}")