def findMissingAndRepeatedValues(grid: list[list[int]]) -> list[int]:
        n = len(grid)
        N = n * n

        expected_sum = N * (N + 1) // 2
        expected_sq_sum = N * (N + 1) * (2 * N + 1) // 6

        actual_sum = 0
        actual_sq_sum = 0

        for row in grid:
            for num in row:
                actual_sum += num
                actual_sq_sum += num * num

        # missing - repeated
        diff = expected_sum - actual_sum

        # missing² - repeated²
        sq_diff = expected_sq_sum - actual_sq_sum

        # missing + repeated
        sum_m_r = sq_diff // diff

        # Solve the equations
        missing = (diff + sum_m_r) // 2
        repeated = sum_m_r - missing

        return [repeated, missing]


print(findMissingAndRepeatedValues([[9,1,7],[8,9,2],[3,4,6]]))