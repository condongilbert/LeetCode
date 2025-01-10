from datetime import datetime
from typing import List

def update_date(script: List[str]) -> List[str]:
    # Step 1: Get today's date in YYYY-MM-DD format
    today = datetime.now().strftime("%Y-%m-%d")
    
    # Step 2: Define the target comment prefix
    target_prefix = "# Last updated:"
    
    # Step 3: Iterate through the script to find the comment
    for i, line in enumerate(script):
        if line.startswith(target_prefix):
            # Step 4: Update the comment with today's date
            script[i] = f"{target_prefix} {today}"
            return script
    
    # Step 5: If comment not found, append it to the script
    script.append(f"{target_prefix} {today}")
    return script