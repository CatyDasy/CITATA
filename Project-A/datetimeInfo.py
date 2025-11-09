from datetime import datetime
import pytz

def DetailedDatetime(WorldPath, format_="%A, %B %d, %Y %I:%M:%S %p"):
    """
    Gets the current date and time in Jakarta timezone using pytz.
    """
    # Define the Jakarta timezone
    tz_jakarta = pytz.timezone(WorldPath)
    
    # Get the current time in the specified timezone
    now_jakarta = datetime.now(tz_jakarta)
    
    # Format the date and time as a detailed string
    # Example format: "Saturday, November 8, 2025 01:45:00 AM WIB+07:00"
    detailed_format = format_
    return now_jakarta.strftime(detailed_format)

# Example usage:
detailed_date_jakarta = DetailedDatetime('Asia/Jakarta')
print(f"Detailed date in Jakarta: {detailed_date_jakarta}")
