def check_log_for_errors(log_file_path):
    try:
        with open(log_file_path, 'r') as file:
            lines = file.readlines()
        errors = [line for line in lines if 'ERROR' in line]
        
        if errors:
            print("Errors found in log file:")
            for error in errors:
                print(error.strip())
        else:
            print("No errors found in log file.")
    
    except FileNotFoundError:
        print(f"Log file '{log_file_path}' not found.")

if __name__ == "__main__":
    log_file_path = "log"
    check_log_for_errors(log_file_path)