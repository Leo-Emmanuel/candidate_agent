import os
from dotenv import load_dotenv
load_dotenv()
AGENT_MODE = os.getenv("AGENT_MODE", "development")
from candidate import get_candidates, check_eligibility
from search import search_candidates, calculate_skill_match, get_match_level
from decision import recommend_candidate
from logger import logger


def run_agent():
    try:
        logger.info("Candidate Agent initialized")
        logger.info(f"Running in {AGENT_MODE} mode")
        candidates = get_candidates()
        logger.info("Candidate data loaded")
        required_skills = ["Python", "SQL", "ML"]
        eligible_candidates = []
        for candidate in candidates:
            if check_eligibility(candidate):
                eligible_candidates.append(candidate)
        logger.info("eligibility check completed")

        sorted_candidates = sorted(
            eligible_candidates,
            key=lambda candidate: candidate["score"],
            reverse=True 
        )
        logger.info("Candidates sorted by score")

    

        print("\nCandidate Results")
        print("--------------------------------")

        for candidate in sorted_candidates:
            match_percentage = calculate_skill_match(candidate, required_skills)
            match_level = get_match_level(match_percentage)

            print(
                f"{candidate['id']} → Score: {candidate['score']} "
                f"→ Skill Match: {match_percentage:.2f}% "
                f"→ Match Level: {match_level}"
            )

        result = search_candidates("C002")

        if result:
            logger.info("Candidate search completed")
        else:
            logger.warning("Candidate not found")

        logger.info("Matching process completed")

        recommended_candidate = recommend_candidate(sorted_candidates,required_skills)
        
        if recommended_candidate:
            logger.info(
                f"Recommended Candidate: {recommended_candidate['id']} "
                f"({recommended_candidate['name']})"
            )
            logger.info(
                "Reason: Highest score among candidates with at least 75% skill match"
            )
        else:
            logger.warning("No eligible candidates available")

        logger.info("Decision completed successfully")
        logger.info("Agent Status: COMPLETED")

    except Exception as e:
        logger.exception(f"An error occurred: {e}")