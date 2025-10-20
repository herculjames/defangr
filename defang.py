import re

def defang(input_str: str) -> str:
    """
    Defangs IPs, URLs, or email addresses to prevent accidental clicks or activation.
    Returns the defanged string.
    """
    # Defang IPv4 address
    if re.match(r"^\d{1,3}(\.\d{1,3}){3}$", input_str):
        # Only defang dots
        return input_str.replace(".", "[.]")
    
    # Defang Emails
    if re.match(r"^[^@]+@[^@]+\.[^@]+$", input_str):
        # Defang "@" and "."
        return input_str.replace(".", "[.]").replace("@", "[@]")

    # Defang URLs (http/https)
    if re.match(r"^(http[s]?://)?(www\.)?.+\..+", input_str):
        # Safely replace "." in domain and path, but preserve "://" for clarity
        defanged = input_str.replace(".", "[.]")
        defanged = defanged.replace(":", "[:]")
        return defanged

    # Default: return unchanged
    return input_str

# Test cases
test_ip = "192.168.127.12"
test_url = "https://www.google.com"
test_email = "testjohndoe1@gmail.com"
test_url2 = "http://sub.domain.com/path?query=1"
test_email2 = "john.doe@sub.domain.com"

print("Defanged IP:", defang(test_ip))
print("Defanged URL:", defang(test_url))
print("Defanged Email:", defang(test_email))
print("Defanged URL #2:", defang(test_url2))
print("Defanged Email #2:", defang(test_email2))
