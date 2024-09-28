

def factorial(total, drawing, ticket):
    try:
        total >= drawing
    except:
        print("total should be greater or equal to drawing")
    odds = 1
    for i in range(1, drawing + 1 ):
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
    total = 50
    drawing = 7
    ticket = 3
    factorial(total,drawing, ticket)