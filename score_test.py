def score_test(tests, right, omit, wrong):
    return tests.count(0) * right + tests.count(1) * omit - tests.count(2) * wrong
print(score_test([0, 1, 0, 0, 2, 1, 0, 2, 2, 1], 3, -1, 2))