def is_palindrome(s):
    # Remove spaces and make lowercase for uniform comparison
    s = s.replace(" ", "").lower()
    # Check if the string is the same forwards and backwards
    return s == s[::-1]

# Example usage
input_string = "A man a plan a canal Panama"
if is_palindrome(input_string):
    print("The string is a palindrome!")
else:
    print("The string is not a palindrome.")
