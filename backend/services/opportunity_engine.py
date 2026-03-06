# 机会评分计算逻辑
def calculate_opportunity(trend_score, demand_score, competition_score, difficulty_score):
    return trend_score + demand_score - competition_score - difficulty_score
