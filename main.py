import messages
import scanner
import utils


def main():
    print(messages.WELCOME_MESSAGE)
        
    last_scan_results ={}

    while True:
        print(messages.MAIN_MENU)

        choice = input("Choose an option: ").strip()

        if choice == "1":
            while True:
                folder_path = input("Enter the source folder path you want to scan (main for main menu): ").strip()
                if folder_path.lower() == "main":
                    break
                elif utils.is_path_valid(folder_path):
                    success, scan_results = scanner.scan(folder_path)
                    if success:
                        last_scan_results = scan_results
                        print(messages.SUCCESS_MESSAGE)
                    else:
                        print(messages.ERROR_MESSAGE)
                    break
                else:
                    print("Invalid path entered.")

        elif choice == "2":
            utils.display_last_scan_results(last_scan_results)

        elif choice == "3":
            print(messages.ABOUT_TWINSCAN)

        elif choice == "4":
            print(messages.GOODBYE_MESSAGE)
            break

        else:
            print("Invalid choice. Please select a valid menu option.")


if __name__ == "__main__":
    main()