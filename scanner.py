import os
import hasher

def scan(folder_path: str) -> tuple[bool, dict]:
    scan_results = {
        "directory": folder_path
    }

    scan_results["all_files"] = get_all_files(folder_path)

    if scan_results["all_files"] is None:
        return False, scan_results
    
    scan_results["total_files"] = len(scan_results["all_files"])
    
    scan_results["hash_map"] = build_hash_map(scan_results["all_files"])

    if scan_results["hash_map"] is None:
        return False, scan_results
    
    scan_results["duplicates"] = find_duplicates(scan_results["hash_map"])
    
    return True, scan_results



def get_all_files(folder_path: str) -> list | None :
    try:
        all_files = []

        for root, dirs, files in os.walk(folder_path):
            for file in files:
                full_path = os.path.join(root, file)
                all_files.append(full_path)

        return all_files

    except Exception:
        return None



def build_hash_map(all_files: list) -> dict | None:
    try:
        hash_map = {}

        for file_path in all_files:
            file_hash = hasher.calculate_hash(file_path)

            if file_hash not in hash_map:
                hash_map[file_hash] = []

            hash_map[file_hash].append(file_path)

        return hash_map
    
    except Exception:
        return None



def find_duplicates(hash_map: dict) -> list:
    duplicates = []

    for files in hash_map.values():
        if len(files) > 1:
            duplicates.append(files)

    return duplicates