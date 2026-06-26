import os
import re
import csv

def extract_difficulty(file_path):
    """Attempt to extract difficulty from a markdown file if it has a ## Difficulty header."""
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            content = f.read()
        # Find ## Difficulty followed by some lines
        match = re.search(r"## Difficulty\s*\n\s*([a-zA-Z]+)", content, re.IGNORECASE)
        if match:
            return match.group(1).strip()
        
        # Also check compact header format: **Difficulty:** Easy or similar
        match_compact = re.search(r"\*\*Difficulty:\*\*\s*([a-zA-Z]+)", content, re.IGNORECASE)
        if match_compact:
            return match_compact.group(1).strip()
    except Exception:
        pass
    return ""

def main():
    dsa_dir = os.path.join(".", "DSA-Knowledge")
    tracker_file = os.path.join(".", "DSA_Tracker.csv")
    
    rows = []
    
    # Recursively scan
    for root, dirs, files in os.walk(dsa_dir):
        # Skip CheatSheets directory
        if "00_CheatSheets" in root:
            continue
            
        for file in files:
            # Match files like 062_Largest_Element.md
            match = re.match(r"^(\d+)_(.+)\.md$", file)
            if match:
                problem_id = match.group(1)
                # Replace underscores with spaces for readability
                raw_name = match.group(2)
                problem_name = raw_name.replace("_", " ")
                
                # Parent folder name is the Topic. Handle nested Md/ folders.
                parts = root.replace("\\", "/").split("/")
                if parts[-1] in ("Md", "Code", "Miscellaneous"):
                    topic = parts[-2]
                else:
                    topic = parts[-1]
                
                # Check for difficulty in file
                full_path = os.path.join(root, file)
                difficulty = extract_difficulty(full_path)
                
                # Create a relative file path hyperlink formula for Excel/Sheets
                rel_path = os.path.relpath(full_path, ".").replace("\\", "/")
                hyperlink = f'=HYPERLINK("{rel_path}", "Open")'
                
                rows.append({
                    "ID": problem_id,
                    "Problem": problem_name,
                    "Topic": topic,
                    "Difficulty": difficulty,
                    "Pattern": "",
                    "Time_Bucket": "",
                    "Status": "Not Started" if not difficulty else "In Progress", # Simple heuristic
                    "Mistake": "",
                    "Edge_Case": "",
                    "File_Path": hyperlink
                })
                
    # Sort by ID numerically
    rows.sort(key=lambda x: int(x["ID"]))
    
    headers = ["ID", "Problem", "Topic", "Difficulty", "Pattern", "Time_Bucket", "Status", "Mistake", "Edge_Case", "File_Path"]
    
    with open(tracker_file, "w", newline="", encoding="utf-8") as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=headers)
        writer.writeheader()
        for row in rows:
            writer.writerow(row)
            
    print(f"Generated tracker for {len(rows)} problems at {tracker_file}")

if __name__ == "__main__":
    main()
