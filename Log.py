from collections import Counter

def analyze_log(file_name):
    try:
        with open(file_name, "r") as file:
            lines = file.readlines()

        error_count = 0
        warning_count = 0
        message_counter = Counter()

        for line in lines:
            if "ERROR" in line:
                error_count += 1
            elif "WARNING" in line:
                warning_count += 1

            message_counter[line.strip()] += 1

        print("\n--- Log Analysis Report ---")
        print(f"Total Entries: {len(lines)}")
        print(f"Errors: {error_count}")
        print(f"Warnings: {warning_count}")

        print("\nMost Common Messages:")
        for message, count in message_counter.most_common(5):
            print(f"{count}x - {message}")

    except FileNotFoundError:
        print("Log file not found.")

file_name = input("Enter log file name: ")
analyze_log(file_name)
