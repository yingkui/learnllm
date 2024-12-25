def print_separator():
    print("\n" + "="*50 + "\n")

def format_results(results, indent=2):
    """Format dictionary results for better readability"""
    formatted = ""
    for key, value in results.items():
        formatted += " " * indent + f"{key}: {value}\n"
    return formatted