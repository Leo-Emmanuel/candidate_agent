from candidate import get_candidates

def search_candidates(candidate_id):

    candidates = get_candidates()

    for candidate in candidates:
        if candidate["id"]==candidate_id:
                return candidate
        
    return None

def calculate_skill_match(candidate, required_skills):
    if not required_skills:
        return 0
    
    matched_skills=0

    for skill in required_skills:
        if skill in candidate["skills"]:
            matched_skills+=1
    match_percentage=(matched_skills/len(required_skills))*100
    return match_percentage

def get_match_level(match_percentage):
    if match_percentage>=75:
        return "High Match"
    else:
        return "Partial Match"
   