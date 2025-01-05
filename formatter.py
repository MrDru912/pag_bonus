def format_string(input_string):
    """
    Convert string by replacing spaces with commas and commas with dots
    Input format example: "1   1  1  1  0,5    0,04166666667"
    Output format example: "1, 1, 1, 1, 0.5, 0.04166666667"
    """
    # Split string by any number of spaces
    parts = ' '.join(input_string.split()).split()

    # Replace commas with dots
    parts = [part.replace(',', '.') for part in parts]

    # Join with comma and space
    return ', '.join(parts)


def main():
    print("Enter strings in format '1   1  1  1  0,5    0,04166666667'")
    print("Press Ctrl+C to exit")

    try:
        while True:
            input_string = input("Enter string: ")
            formatted_string = format_string(input_string)
            print(f"Formatted: {formatted_string}")
    except KeyboardInterrupt:
        print("\nExiting program")


if __name__ == "__main__":
    main()