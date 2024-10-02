# Rabin-Karp Pattern Matching Algorithm
def rabin_karp_pattern_search(text, pattern, prime=101):
    d = 256  # Number of characters in the input alphabet (ASCII)
    n = len(text)  # Length of the text
    m = len(pattern)  # Length of the pattern
    h_pattern = 0  # Hash value for pattern
    h_text = 0  # Hash value for text substring
    h = 1  # The value of d^(m-1)
    
    # Calculate the value of h as d^(m-1) % prime
    for i in range(m - 1):
        h = (h * d) % prime

    # Calculate the hash value of the pattern and the first window of text
    for i in range(m):
        h_pattern = (d * h_pattern + ord(pattern[i])) % prime
        h_text = (d * h_text + ord(text[i])) % prime

    # Slide the pattern over the text one by one
    for i in range(n - m + 1):
        # If the hash values match, check character by character
        if h_pattern == h_text:
            # Check characters if hash values match
            match = True
            for j in range(m):
                if text[i + j] != pattern[j]:
                    match = False
                    break
            if match:
                print(f"Pattern found at index {i}")
        
        # Calculate the hash value for the next window of text
        # Remove the leading character and add the trailing character
        if i < n - m:
            h_text = (d * (h_text - ord(text[i]) * h) + ord(text[i + m])) % prime
            
            # We might get a negative value of h_text, convert it to positive
            if h_text < 0:
                h_text += prime

# Example usage
text = "GEEKS FOR GEEKS"
pattern = "GEEK"
rabin_karp_pattern_search(text, pattern)
