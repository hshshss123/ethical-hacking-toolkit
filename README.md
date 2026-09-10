# EHTool — Ethical Hacking Learning Lab

A **beginner-friendly, terminal-first cybersecurity learning toolkit** for authorized testing and defensive practice. It is designed to run on **Windows PowerShell** and **Android Termux** with Python 3.

> ⚠️ **AUTHORIZED USE ONLY:** Test only systems, networks, applications, and accounts you own or have explicit permission to assess.

## What makes EHTool different?

EHTool is not just a collection of commands. It is designed to **teach while you use it**.

Every module explains:

1. **What it does** — the purpose of the tool.
2. **Why it matters** — how the concept is used in cybersecurity.
3. **Key ideas** — beginner-friendly networking, web, TLS, identity, and cryptography concepts.
4. **Safety** — what kind of target is appropriate for practice.
5. **The result** — the actual check output after you understand what you are looking at.

The terminal UI uses clear sections, icons, spacing, and a built-in **Lesson Browser** so beginners can learn without needing a separate manual.

## Tools

| Tool | What it teaches |
|---|---|
| System Information | Understanding your own machine and environment |
| Connectivity / DNS | Hostnames, IP addresses, and basic network connectivity |
| TCP Port Check | Services, ports, and reachable network endpoints |
| HTTP Inspection | Status codes, content types, and web-server responses |
| TLS Certificate | Certificates, certificate authorities, and TLS versions |
| Security Headers | Defensive browser/web security controls |
| Password Strength | Password length, complexity, and safer testing habits |
| SHA-256 / SHA-512 | Cryptographic hashing and data integrity |

## Quick start

### Windows PowerShell

```powershell
git clone https://github.com/hshshss123/ethical-hacking-toolkit.git
cd ethical-hacking-toolkit
py -3 main.py
```

### Android Termux

```bash
pkg install git python -y
git clone https://github.com/hshshss123/ethical-hacking-toolkit.git
cd ethical-hacking-toolkit
python main.py
```

No root access is required for the current modules.

## Menu design

The main menu is organized into two parts:

```text
╔══════════════════════════════════════════════════════════════════════╗
║              EHTOOL — ETHICAL HACKING LEARNING LAB                 ║
║           Learn first • Check second • Stay authorized              ║
╚══════════════════════════════════════════════════════════════════════╝

  BEGINNER TOOLS

  1  System information       — Know your machine
  2  Connectivity / DNS       — Understand networking
  3  TCP port check            — Find one reachable service
  4  HTTP inspection            — Read a web response
  5  TLS certificate            — Inspect encrypted connections
  6  Security headers           — Review defensive web settings
  7  Password strength          — Learn password basics
  8  SHA-256 / SHA-512          — Learn hashing

  LEARNING
  9  Browse lessons             — Read what each tool does
  0  Exit
```

Choosing a tool first shows its lesson, then runs the check. Option **9** opens a module-by-module lesson browser.

## Project structure

```text
ethical-hacking-toolkit/
├── main.py
├── requirements.txt
├── README.md
└── ehtool/
    ├── __init__.py
    ├── ui.py
    ├── checks.py
    └── lessons.py
```

## Learning path

A good beginner sequence is:

**1. System → 2. DNS/Connectivity → 3. Ports → 4. HTTP → 5. TLS → 6. Security Headers → 7. Passwords → 8. Hashing**

This moves from basic computer/network concepts toward web security and cryptography.

## Safety boundary

This project intentionally avoids malware, credential theft, persistence, exploit delivery, phishing kits, DDoS functionality, password cracking, stealth, and unauthorized-access features.

It is intended for:

- Your own computer and phone
- Local test environments
- Purpose-built cybersecurity labs
- Systems where you have explicit authorization to test

The toolkit performs basic observation and defensive checks; a result such as **OPEN**, **reachable**, or **missing header** is not by itself proof of a vulnerability.

## License

MIT License.
