import os


def is_path_valid(folder_path: str) -> bool:
    return os.path.isdir(folder_path)



def display_last_scan_results(last_scan_results: dict) -> None:
    if last_scan_results:
        print(f"Directory: {last_scan_results['directory']}")
        print(f"Total Files: {last_scan_results['total_files']}")
        print("All Files:")
        for file_path in last_scan_results['all_files']:
            print(f"\t{file_path}")
    else:
        print("Nothing to display")