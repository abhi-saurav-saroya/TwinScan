import os

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

        return True, scan_results

    except Exception:
        return False, {}