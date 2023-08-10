import random
import copy


class Hat:

    def __init__(self, **args):
        self.contents = []
        for key, value in args.items():
            for _ in range(value):
                self.contents.append(key)

    def draw(self, n):
        out = []
        if n >= len(self.contents):
            out.extend(self.contents)
            return out

        for _ in range(n):
            ran = random.choice(self.contents)
            self.contents.remove(ran)
            out.append(ran)
        return out


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    count = 0
    for _ in range(num_experiments):
        outcome = True
        hatcopy = copy.deepcopy(hat)
        temp = hatcopy.draw(num_balls_drawn)
        for key, value in expected_balls.items():
            if temp.count(key) < value: outcome = False
        if outcome:
            count += 1
    return count / num_experiments