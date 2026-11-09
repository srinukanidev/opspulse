from datetime import datetime
from pathlib import Path

VALID_SEVERITY_LEVELS = {"INFO", "WARNING", "ERROR", "DEBUG"}

def parse_log_file(log_file_path: Path) -> None:
    """
    Parses the log file and extracts relevant information.

    Args:
        log_file_path (Path): The path to the log file.
    Returns:
        None
    """
    if not log_file_path.exists():
        raise FileNotFoundError(
            f"The log file {log_file_path} does not exist."
        )
    with log_file_path.open("r", encoding='utf-8') as log_file:
        for line_number, line in enumerate(log_file, start=1):
            # Example parsing logic: print each line (you can customize this)
            line = line.strip()
            #print(line)
            if not line:
                continue  # Skip empty lines
            if len(line) < 20:
                print(f"Invalid log entry (too short):{line_number}: {line}")
                print("-" * 40)  # Separator for readability
                continue
            timestamp_text = line[:19]
            try:
                timestamp = datetime.strptime(timestamp_text, "%Y-%m-%d %H:%M:%S")
            except ValueError:
                print(f"Invalid timestamp format: {line}")
                print("-" * 40)  # Separator for readability
                continue
            if line[19] != " ":
                            print(f"Invalid log entry (missing space after timestamp):{line_number}: {line}")
                            print("-" * 40)  # Separator for readability
                            continue
            remaining_text = line[20:]
            parts = remaining_text.split(maxsplit=1)
            #parts = remaining_text.split(" ", 1)
            if not parts:
                print(f"Invalid log entry (missing severity level):{line_number}: {line}")
                print("-" * 40)  # Separator for readability
                continue
            severity = parts[0].upper()
            if severity not in VALID_SEVERITY_LEVELS:
                print(f"Invalid severity level: {line_number}: {line}")
                print("-" * 40)  # Separator for readability
                continue
            message = parts[1] if len(parts) > 1 else ""
            print(f"Timestamp: {timestamp}")
            print(f"Severity Level: {severity}")
            print(f"Message: {message}")
            print("-" * 40)  # Separator for readability
            
if __name__ == "__main__":
    log_file_path = Path("data/sample.log")  # Replace with the actual log file path
    parse_log_file(log_file_path)
