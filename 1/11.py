

def process_string(s):
    # Find the first and last digits in the string
    first_digit = int(next(filter(str.isdigit, s)))
    last_digit = int(next(filter(str.isdigit, s[::-1])))

    # Connect the two numbers to form a single digit
    combined_digit = (first_digit * 10) + last_digit

    return combined_digit

def main():
    with open('11.txt', 'r') as f:
        data = f.read().split('\n')

    # Part 1
        digit_sum = 0
        for line in data:    
            result = process_string(line)       
            digit_sum += result  # Add result to digit_sum
            print(digit_sum)

main()
