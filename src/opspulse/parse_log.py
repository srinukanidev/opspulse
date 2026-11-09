from datetime import datetime
from pathlib import Path

def parse_log_file(log_file_path: Path) -> None:
    """
    Parses the log file and extracts relevant information.

    Args:
        log_file_path (Path): The path to the log file.
    Returns:
        None
    """
    if not log_file_path.exists():
            raise FileNotFoundError(f"The log file {log_file_path} does not exist.")
    with log_file_path.open("r", encoding='utf-8') as log_file:
        for line in log_file:
            # Example parsing logic: print each line (you can customize this)
            line = line.strip()
            #print(line)
            if not line:
                continue  # Skip empty lines
            timestamp_text = line[:19]
            remaining_text = line[20:]
            timestamp = datetime.strptime(timestamp_text, "%Y-%m-%d %H:%M:%S")
            parts = remaining_text.split(maxsplit=1)
            #parts = remaining_text.split(" ", 1)
            severity = parts[0]
            message = parts[1] if len(parts) > 1 else ""
            print(f"Timestamp: {timestamp}")
            print(f"Severity Level: {severity}")
            print(f"Message: {message}")
            print("-" * 40)  # Separator for readability
            
            
            

if __name__ == "__main__":
    log_file_path = Path("data/sample.log")  # Replace with the actual log file path
    parse_log_file(log_file_path)
