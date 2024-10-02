# KMP Pattern Matching Algorithm
def kmp_pattern_search(text, pattern):
    text_len = len(text)
    pattern_len = len(pattern)
    
    # Create the longest prefix suffix (LPS) array
    lps = [0] * pattern_len
    j = 0  # Index for the pattern
    compute_lps(pattern, lps)
    
    i = 0  # Index for the text
    while i < text_len:
        if pattern[j] == text[i]:
            i += 1
            j += 1
        
        if j == pattern_len:
            print(f"Pattern found at index {i - j}")
            j = lps[j - 1]
        
        elif i < text_len and pattern[j] != text[i]:
            if j != 0:
                j = lps[j - 1]
            else:
                i += 1

# Function to compute the LPS array
def compute_lps(pattern, lps):
    length = 0
    i = 1
    lps[0] = 0
    
    while i < len(pattern):
        if pattern[i] == pattern[length]:
            length += 1
            lps[i] = length
            i += 1
        else:
            if length != 0:
                length = lps[length - 1]
            else:
                lps[i] = 0
                i += 1

# Example usage
text = "AABAACAADAABAABA"
pattern = "AABA"
kmp_pattern_search(text, pattern)
