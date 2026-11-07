from search import calculate_skill_match

def recommend_candidate(candidates,required_skills):

    if not candidates:
        return None

    eligible_candidates=[]

    for candidate in candidates:    
            if calculate_skill_match(candidate, required_skills) >= 75:
                eligible_candidates.append(candidate)
    if not eligible_candidates:
        return None

    highest = max(eligible_candidates, key=lambda candidate: candidate["score"])
    return highest

    

    