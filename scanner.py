import os
import hasher

def scan(folder_path: str) -> tuple[bool, dict]:
    try:
        all_files = []

        for root, dirs, files in os.walk(folder_path):
            for file in files:
                full_path = os.path.join(root, file)
                all_files.append(full_path)

        scan_results = {
            "directory": folder_path,
            "total_files": len(all_files),
            "all_files": all_files
        }

        hash_map = {}

        for file_path in all_files:
            file_hash = hasher.calculate_hash(file_path)

            if file_hash not in hash_map:
                hash_map[file_hash] = []

            hash_map[file_hash].append(file_path)

        scan_results["hash_map"] = hash_map

        return True, scan_results

    except Exception:
        return False, {}