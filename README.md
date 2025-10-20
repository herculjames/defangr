# Defang Script

Safely obfuscate URLs, IPs, and email addresses to prevent accidental clicks, downloads, or alerts when sharing Indicators of Compromise (IOCs) in cybersecurity operations.

## What is Defanging?

Defanging is the process of intentionally modifying potentially malicious or sensitive strings (like URLs or email addresses) so they cannot be activated by clicking, previewing, or scanning. This is a best practice used by cyber defenders to safely share threat intelligence and forensic data.

**Example:**  
- Fang: `https://www.google.com`  
- Defanged: `https[:]//www[.]google[.]com`

## Features

- Defangs IPv4 addresses, URLs (including http/https), and email addresses
- Prevents accidental triggering during analysis or sharing
- Simple, lightweight Python script—ideal for SOC analysts, incident response, and cyber researchers

## Usage

1. Clone or download the repo
2. Run the script locally

python defang.py

**Sample Output:**
Defanged IP: 192[.]168[.]127[.]12
Defanged URL: https[:]//www[.]google[.]com
Defanged Email: testjohndoe1[@]gmail[.]com
Defanged URL #2: http[:]//sub[.]domain[.]com/path?query=1
Defanged Email #2: john[.]doe[@]sub[.]domain[.]com


## Why Use This Script?

- Share IOCs with security teams, vendors, or public platforms without risking accidental infection or blocking
- Standardizes the way you document findings in reports, emails, and intelligence feeds

## Contributing

Feedback, forks, and issues are welcome! Feel free to open pull requests for improvements.

## License

MIT License

---

*Built with ❤️ locally (127.0.0.1) by Hercul James Christopher, a digital guArdIan.*
