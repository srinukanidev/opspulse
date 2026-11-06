from pathlib import Path

def parse_log_file(log_file_path: Path) -> None:
    """
    Parses the log file and extracts relevant information.

    Args:
        log_file_path (Path): The path to the log file.
    Returns:
        None
    """
    error_count = 0
    warning_count = 0
    info_count = 0
    if not log_file_path.exists():
        raise FileNotFoundError(f"The log file {log_file_path} does not exist.")

    with log_file_path.open('r', encoding='utf-8' ) as log_file:
        for line in log_file:
            # Process each line of the log file
            #  print(line.strip())  # Example processing: print each line
            if "ERROR" in line:
                # print(f"Error found: {line.strip()}") 
                 error_count += 1
            elif "WARNING" in line:
                   # print(f"Warning found: {line.strip()}")
                    warning_count += 1
            elif "INFO" in line:
                    #print(f"Info found: {line.strip()}")
                    info_count += 1
    print(f"Errors: {error_count}")
    print(f"Warnings: {warning_count}")
    print(f"Info: {info_count}")

if __name__ == "__main__":
    log_file_path = Path("data/sample.log")  # Replace with the actual log file path
    parse_log_file(log_file_path)
