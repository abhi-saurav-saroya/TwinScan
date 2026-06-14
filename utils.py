import os


def is_path_valid(folder_path: str) -> bool:
    return os.path.isdir(folder_path)



def display_last_scan_results(last_scan_results: dict) -> None:
    if not last_scan_results:
        print("No scan results available.")
        return

    print("\n" + "=" * 50)
    print("            LAST SCAN RESULTS")
    print("=" * 50)

    print(f"Directory     : {last_scan_results['directory']}")
    print(f"Total Files   : {last_scan_results['total_files']}")
    print(f"Unique Hashes : {len(last_scan_results['hash_map'])}")
    print(f"Duplicate Groups Found : {len(last_scan_results['duplicates'])}")
    print(f"Dupliacte Files Found: {sum(len(group) for group in last_scan_results['duplicates'])}")

    print("\n" + "=" * 50)
    print("           DUPLICATE FILE GROUPS")
    print("=" * 50)

    if not last_scan_results['duplicates']:
        print("No duplicate files found.")
        return

    for group_number, duplicate_group in enumerate(last_scan_results['duplicates'], start=1):
        print(f"\nGroup {group_number}")

        for file_path in duplicate_group:
            print(f"  -> {file_path}")

    print("\n" + "=" * 50)
    print(f"Potential Space Wasted: {last_scan_results['space_wasted']} bytes")