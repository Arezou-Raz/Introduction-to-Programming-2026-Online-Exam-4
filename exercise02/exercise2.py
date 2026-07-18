def find_allowed(wordlist, minimum):
    result = []
    vowels = "aeiouy"
    
    for word in wordlist:
        # Count how many characters in the word are in the vowels string
        count = 0
        for char in word.lower():
            if char in vowels:
                count += 1
        
        # If the count meets the minimum, add the word to the result list
        if count >= minimum:
            result.append(word)
            
    return result

# Example usage:
if __name__ == "__main__":
    wordlist = ["apple", "banana", "cherry", "orange", "peach", "pineapple"]
    minimum = 3
    result = find_allowed(wordlist, minimum)
    print(result)
