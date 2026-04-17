import random


def generate_initial_scores(num_scores, target_average):
    scores = []
    for i in range(num_scores):
        score = random.randint(target_average - 8, target_average + 8)
        scores.append(score)
    return scores

def cap_scores_to_max(scores, max_score):
    for i in range(len(scores)):
        if scores[i] > max_score:
            scores[i] = max_score

def calculate_weighted_category_score(scores_list, weights_table, category_code):
    if len(scores_list) == 0:
        return 0.0
    average = sum(scores_list) / len(scores_list)
    weights_percentage = 0
    for item in weights_table:
        if item[0] == category_code:
            weights_percentage = item[1]
            break
    contribution = average * (weights_percentage / 100)
    return contribution



MAX_SCORE = 100
TARGET_AVG_QUIZ = 95
TARGET_AVG_HW = 93
NUM_QUIZ = 5
NUM_HW = 10

WEIGHT_TABLE = [
    [1, 40],  # Quiz Code is 1, weight is 40%
    [2, 60]  # HW Code is 2, weight 60%
]
QUIZ_CODE = 1
HW_CODE = 2

def main():
    print("--- Penn State Final Grade Calculator ---")

    # Quiz Component (Code 1, 40%)
    quiz_scores = generate_initial_scores(NUM_QUIZ, TARGET_AVG_QUIZ)
    print("Raw Quiz Scores (%d):" % NUM_QUIZ, quiz_scores)

    # cap the quiz scores to the max
    cap_scores_to_max(quiz_scores, MAX_SCORE)
    print("Capped Quiz Scores: ", quiz_scores)

    # calculate the weighted score contribution
    weighted_quiz_score = calculate_weighted_category_score(quiz_scores, WEIGHT_TABLE, QUIZ_CODE)

    print("\nQuiz Score Contribution (40%%): %.2f" % weighted_quiz_score)

    # Homework component (Code 2, 60%)
    hw_scores = generate_initial_scores(NUM_HW, TARGET_AVG_HW)
    print("Raw HW Scores (%d):" % NUM_HW, hw_scores)

    # cap the HW scores to the max
    cap_scores_to_max(hw_scores, MAX_SCORE)
    print("Capped HW Scores: ", hw_scores)

    # calculate the weighted score contribution
    weighted_hw_score = calculate_weighted_category_score(hw_scores, WEIGHT_TABLE, HW_CODE)

    print("\nHomework Score Contribution (60%%): %.2f" % weighted_hw_score)

    # final calculation
    total_score = weighted_quiz_score + weighted_hw_score

    print("\n-------------------------------------")
    print("TOTAL COURSE SCORE: %.2f" % total_score)
    print("-------------------------------------")

# Execute main()
main()