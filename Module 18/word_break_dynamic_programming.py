
# Dynamic Programming: Word Break Problem

def can_segment_words(input_string, word_dictionary):
    string_length = len(input_string)

    # dp[i] is True if the first i characters can be segmented
    dp = [False] * (string_length + 1)

    # An empty string can always be segmented
    dp[0] = True

    # Check every possible ending position
    for end_index in range(1, string_length + 1):

        # Try every possible starting position
        for start_index in range(end_index):

            # Check whether the prefix is segmentable
            # and the current substring exists in the dictionary
            if (dp[start_index] and
                    input_string[start_index:end_index] in word_dictionary):
                dp[end_index] = True
                break

    return dp[string_length]


# Example usage
if __name__ == "__main__":
    input_string = "leetcode"
    word_dictionary = ["leet", "code"]

    if can_segment_words(input_string, word_dictionary):
        print("String can be segmented into dictionary words")
    else:
        print("String cannot be segmented into dictionary words")
