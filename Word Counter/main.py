# Fairus main code here

import file_handler
import time_handler

def main():
    while True:
        file_name = input("Enter the name of the file to update: ")

        # Read the content of the file
        content = file_handler.read_file(file_name)

        # If the file was not found, prompt the user again
        if content == "":
            print("File not found. Please try again.")
            continue

        # Loop to allow adding more content to the file
        while True:
            # Get the word count of the current content
            word_count = file_handler.get_word_count(content)

            # Print the word count
            print(f"Word Count: {word_count}")

            # Ask if the user wants to add more content
            add_content = input("Do you want to add more content to the file? (yes/no): ").strip().lower()

            if add_content == 'yes':
                # Let the user add new content to the file
                new_content = input("Enter the content you want to add: ")

                # Append the new content to the file
                file_handler.append_to_file(file_name, new_content)

                # Read the updated content and loop again to count words
                content = file_handler.read_file(file_name)
            elif add_content == 'no':
                # Get the current timestamp
                timestamp = time_handler.get_current_timestamp()

                # Update the file with word count and timestamp
                file_handler.update_file(file_name, word_count, timestamp)
                break  # Exit the loop once the user is done
            else:
                print("Invalid input. Please type 'yes' or 'no'.")

        # Ask if the user wants to process another file
        continue_choice = input("Do you want to process another file? (yes/no): ").strip().lower()
        if continue_choice != 'yes':
            break

if __name__ == "__main__":
    main()
