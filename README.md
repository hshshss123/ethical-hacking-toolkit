# Ethical Hacking Toolkit

A beginner-friendly, terminal-first security toolkit for **authorized** testing and learning. Designed to work on Windows PowerShell and Android Termux with Python 3.

> ⚠️ Use only on systems, networks, applications, and accounts you own or have explicit permission to test.

## Goals

- Simple terminal UI
- Beginner explanations
- Windows PowerShell + Termux compatibility
- Safe-by-default reconnaissance and security checks
- JSON output for scripting and reports
- Minimal dependencies

## Current modules

- Local system information
- Ping/connectivity check
- DNS lookup
- TCP port connectivity check
- HTTP response inspection
- TLS certificate inspection
- HTTP security-header check
- Password-strength estimator
- SHA-256/SHA-512 hashing utilities

## Quick start

### Windows PowerShell

```powershell
py -3 main.py
```

### Termux

```bash
pkg install python -y
python main.py
```

No root access is required.

## Project structure

```text
ethical-hacking-toolkit/
├── main.py
├── requirements.txt
├── README.md
└── ehtool/
    ├── __init__.py
    ├── ui.py
    └── checks.py
```

## Legal / safety boundary

This project intentionally avoids malware, credential theft, persistence, exploit delivery, phishing kits, DDoS functionality, and unauthorized access features. It is intended for labs, owned devices, defensive checks, and authorized security assessments.

## License

MIT License.