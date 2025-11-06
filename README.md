# Number Info Tool

This is a small OSINT (open-source intelligence) utility that gathers information for a phone number by calling a remote API.

## What it is

- A simple command-line tool implemented in `num_info.py`.
- Purpose: quickly look up publicly-available information related to a phone number.

## Quick start

Prerequisites:

- Python 3.8+ installed
- Internet connection

Install dependencies:

```powershell
pip install -r requirements.txt
```

Run the tool:

```powershell
python num_info.py
```

When prompted, enter a phone number (digits only). Enter `q` to quit or press Ctrl+C to exit.

## Contract (inputs / outputs / errors)

- Input: a phone number (without +91).
- Output: a short, human-readable summary (Name, Father, Mobile, Address, Circle, ID Number, Email) when available, or the raw JSON if the response format differs.

## Responsible use & legal

This tool performs OSINT lookups. Use it responsibly and only on Indian phone numbers for which you have a legitimate reason to query information. Respect privacy, local laws, and terms of service. The author and contributors are not responsible for misuse.

## Credits

- Script author: [@IamTechyAnimesh](https://github.com/IamTechyAnimesh/)

---
