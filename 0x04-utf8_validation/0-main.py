#!/usr/bin/python3
"""
Main file for testing
"""

validUTF8 = __import__('0-validate_utf8').validUTF8

data = [65]
print(validUTF8(data))

data = [80, 121, 116, 104, 111, 110, 32, 105, 115, 32, 99, 111, 111, 108, 33]
print(validUTF8(data))

data = [229, 65, 127, 256]
print(validUTF8(data))


data = [195, 169]
print(validUTF8(data))

test_cases = [
    [[467, 133, 108], False],
    [[240, 188, 128, 167], True],
    [[235, 140], False],
    [[345, 467], False],
    [[250, 145, 145, 145, 145], False],
    [[0, 0, 0, 0, 0, 0], True],
    [[], True]
]

# Run test cases
for data, expected_result in test_cases:
    result = validUTF8(data)
    assert result == expected_result, f"Input: {data}, Expected: {expected_result}, Got: {result}"

print("All test cases passed successfully!")
