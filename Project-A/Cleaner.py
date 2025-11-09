def clean_output(func):
    """
    Decorator function that adds clean spacing before and after any function output.
    Can be used at start, middle, or end of your project.
    
    Usage:
    @clean_output
    def your_function():
        # your code here
    """
    def wrapper(*args, **kwargs):
        print("\n" + "="*50)  # Clean start spacing
        result = func(*args, **kwargs)
        print("="*50 + "\n")  # Clean end spacing
        return result
    return wrapper

def add_spacing(message="", before_lines=2, after_lines=2):
    """
    Simple function to add spacing around any message or section.
    
    Args:
        message: Text to display (optional)
        before_lines: Number of empty lines before (default: 2)
        after_lines: Number of empty lines after (default: 2)
    """
    print("\n" * before_lines, end="")
    if message:
        print(message)
    print("\n" * after_lines, end="")

def section_break(title="", width=50, char="="):
    """
    Creates a clean section break with optional title.
    
    Args:
        title: Section title (optional)
        width: Width of the separator line
        char: Character to use for separator
    """
    print(f"\n{char * width}")
    if title:
        # Center the title
        padding = (width - len(title) - 2) // 2
        print(f"{char}{' ' * padding} {title} {' ' * padding}{char}")
        print(f"{char * width}")
    print()

# Example usage demonstrations:

# Method 1: Using decorator
@clean_output
def main_process():
    print("This is the main process running...")
    print("Processing data...")
    print("Task completed!")

# Method 2: Using spacing function
def another_function():
    add_spacing("Starting secondary process", 1, 1)
    print("Secondary process running...")
    add_spacing("Secondary process completed", 1, 2)

# Method 3: Using section breaks
def demo_sections():
    section_break("PROJECT START")
    print("Welcome to the project!")
    
    section_break("PROCESSING DATA")
    print("Processing important data...")
    
    section_break("PROJECT END")
    print("Project completed successfully!")

# Quick usage examples:
if __name__ == "__main__":
    # You can call these anywhere in your project:
    
    # At the start
    section_break("PROGRAM INITIALIZATION")
    print("Program starting...")
    
    # In the middle
    add_spacing("Middle section processing...", 1, 1)
    
    # Using the decorator
    main_process()
    
    # More middle content
    another_function()
    
    # At the end
    section_break("PROGRAM COMPLETE")
    print("All tasks finished!")
    
    # Final clean spacing
    add_spacing("", 0, 3)