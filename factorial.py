import sys

def factorial(total, drawing, ticket):
    # 如果输入数据不能满足最基本的条件，就直接中止退出
    if total < drawing:
        print("total should be greater or equal to drawing")
        sys.exit()

    odds = 1
    for i in range(1, drawing + 1):
        odds = round(odds * (total - i + 1) / (drawing - i + 1))
    odds = round(odds / ticket)
    print("--------------")
    print(f"odds equal to", odds)

    official_odds, another_divide = 1, 1
    for j in range(1, drawing + 1):
        official_odds = official_odds * (total - j + 1)
        another_divide = another_divide * (j)
    official_odds = round (official_odds / another_divide / ticket)
    print(">>>>>>>>>>>>>>>")
    print(f"official_odds equal to", official_odds)

if __name__ == "__main__":
    total = 5
    drawing = 7
    ticket = 3
    factorial(total,drawing, ticket)