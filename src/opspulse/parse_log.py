from pathlib import Path

def parse_log_file(log_file_path: Path) -> None:
    """
    Parses the log file and extracts relevant information.

    Args:
        log_file_path (Path): The path to the log file.
    Returns:
        None
    """
    ErrorCount = 0
    WarningCount = 0
    InfoCount = 0
    if not log_file_path.exists():
        raise FileNotFoundError(f"The log file {log_file_path} does not exist.")

    with log_file_path.open('r', encoding='utf-8' ) as log_file:
        for line in log_file:
            # Process each line of the log file
            #  print(line.strip())  # Example processing: print each line
            if "ERROR" in line:
                # print(f"Error found: {line.strip()}") 
                 ErrorCount += 1
            elif "WARNING" in line:
                   # print(f"Warning found: {line.strip()}")
                    WarningCount += 1
            elif "INFO" in line:
                    #print(f"Info found: {line.strip()}")
                    InfoCount += 1
    print(f"Errors: {ErrorCount}")
    print(f"Warnings: {WarningCount}")
    print(f"Info: {InfoCount}")

if __name__ == "__main__":
    log_file_path = Path("data/sample.log")  # Replace with the actual log file path
    parse_log_file(log_file_path)
