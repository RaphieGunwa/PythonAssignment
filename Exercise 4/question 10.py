def repl(input_string, repetitions):
    if repetitions <= 0:
        return ""  # Return an empty string if repetitions is 0 or less
    else:
        return input_string * repetitions  # Concatenate the input_string based on repetitions

# Test the repl method
result = repl("data", 3)
print(result) 