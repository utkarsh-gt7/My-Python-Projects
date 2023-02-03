def paint_calc(height,width,cover):
    print(f"You'll need {round((test_h*test_w)/coverage)} cans of paint.")


test_h = int(input("Height of wall: "))
test_w = int(input("Width of wall: "))
coverage = 5
paint_calc(height=test_h, width=test_w, cover=coverage)
