from pathlib import Path
from opspulse.parse_log import parse_log_file

def main() -> None:
    log_file_path = Path("data/sample.log")  # Replace with the actual log file path
    parse_log_file(log_file_path)
if __name__ == "__main__":
    main()
