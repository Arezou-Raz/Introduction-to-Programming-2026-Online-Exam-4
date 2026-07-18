def read_points():
    results = []
    
    with open("statistics.txt", "r") as file:
        for line in file:
            line = line.strip()
            if not line:
                continue
            
            # Split into team name and the scores part
            try:
                parts = line.split(":")
                team_name = parts[0]
                scores = parts[1].split("-")
                
                # Convert scores to integers
                # This will raise a ValueError if conversion fails
                wins = int(scores[0])
                losses = int(scores[1])
                ties = int(scores[2])
                
                # Calculate points: 3 per win, 1 per tie
                points = (wins * 3) + (ties * 1)
                
                results.append((team_name, points))
                
            except (ValueError, IndexError):
                # Raise the specific error message required by the exercise
                raise ValueError(f"Invalid format in the file: {line}")
                
    return results
