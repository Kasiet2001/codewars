def get_winner(ballots):
    candidates = {}
    for i in range(len(ballots)):
        if ballots[i] not in candidates:
            candidates[ballots[i]] = ballots.count(ballots[i])
    all_values = candidates.values()
    max_value = max(all_values)
    return max(candidates, key=candidates.get) if ((max_value * 2) - sum(candidates.values())) >= 1 else None
print(get_winner(("A", "A", "A", "B", "B", "B")))
