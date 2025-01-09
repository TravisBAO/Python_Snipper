import sys

def factorial(factorial_n, factorial_len=0):
    if factorial_len == 0:
        factorial_len = factorial_n # 若阶乘长度没有给，就按阶乘本体的长度
    factorial_result = 1
    while factorial_len > 0 :
        factorial_result = factorial_result * factorial_n
        factorial_n -= 1
        factorial_len -= 1
    return factorial_result

def calc_combination(combination_n, combination_m):
    if combination_m != 0 :
        combination_n_calc = factorial(combination_n, combination_m)
        combination_m_calc = factorial(combination_m)
        combination_result = round(combination_n_calc / combination_m_calc)
    else:
        combination_result = 1
    return combination_result

TOTAL_BALLS = 50
MAXIMUM_MATCH_BALL = 7
UNMATCHED_BALL = TOTAL_BALLS - MAXIMUM_MATCH_BALL
TICKETS = 1
ALL_COMBINATIONS = calc_combination(TOTAL_BALLS, MAXIMUM_MATCH_BALL)


def odds_calc(matched_ball_amount, with_bonus):

    if not with_bonus :
        # 选中的球中匹配球的组合
        choosed_matched_odds = calc_combination(MAXIMUM_MATCH_BALL, matched_ball_amount)
        # 选中的球中不匹配球的组合
        choosed_unmatched_ball = MAXIMUM_MATCH_BALL - matched_ball_amount
        choose_unmatched_odds = calc_combination(UNMATCHED_BALL, choosed_unmatched_ball)
        partial_match_odds = ALL_COMBINATIONS / (choosed_matched_odds * choose_unmatched_odds * TICKETS)
        partial_match_odds_percent = percentage(1, partial_match_odds)
    else:
        pass
    print("\n")
    # print("------------------")
    print(f"Match {matched_ball_amount}'s odd is 1/{partial_match_odds}")
    print(f"Match {matched_ball_amount}'s odd in percent is {partial_match_odds_percent:.6%}")

def percentage(part, whole):
    Percentage =  float(part)/float(whole)
    return Percentage

if __name__ == "__main__":

    odds_calc(7, False)
    odds_calc(6, False)
    odds_calc(5, False)
    odds_calc(4, False)
    odds_calc(3, False)
    odds_calc(2, False)
    odds_calc(1, False)
    odds_calc(0, False)