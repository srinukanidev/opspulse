from pathlib import Path
from opspulse.parse_log import parse_log_file

def main() -> None:
    # print("Welcome to OpsPulse!")
    #print("My AI Engineering journey starts here.")
    #print(f"Python set __name__ to: {__name__} ")
    log_file_path = Path("data/sample.log")  # Replace with the actual log file path
    parse_log_file(log_file_path)
if __name__ == "__main__":
    main()
