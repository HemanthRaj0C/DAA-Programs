# Naive Pattern Matching Algorithm
def naive_pattern_search(text, pattern):
    text_len = len(text)
    pattern_len = len(pattern)
    
    # Loop to slide the pattern over the text
    for i in range(text_len - pattern_len + 1):
        j = 0
        # For current index i, check if the pattern matches
        while j < pattern_len and text[i + j] == pattern[j]:
            j += 1
        
        # If the pattern matches, print the index
        if j == pattern_len:
            print(f"Pattern found at index {i}")

# Example usage
text = "AABAACAADAABAABA"
pattern = "AABA"
naive_pattern_search(text, pattern)
