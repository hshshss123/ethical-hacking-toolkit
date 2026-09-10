import json
from . import checks


def pause():
    input("\nPress Enter to continue...")


def show(value):
    print(json.dumps(value, indent=2, default=str))


def run_menu():
    while True:
        print("\n" + "=" * 58)
        print("  EHTool - Beginner Ethical Hacking Toolkit")
        print("  Authorized / defensive use only")
        print("=" * 58)
        print("1. Local system information")
        print("2. Connectivity / DNS check")
        print("3. TCP port check")
        print("4. HTTP inspection")
        print("5. TLS certificate inspection")
        print("6. HTTP security headers")
        print("7. Password strength")
        print("8. SHA-256 / SHA-512 hash")
        print("0. Exit")
        choice = input("\nSelect: ").strip()

        try:
            if choice == "1":
                show(checks.local_info())
            elif choice == "2":
                host = input("Host/domain: ").strip()
                ok, message = checks.ping_host(host)
                print(("[+] " if ok else "[-] ") + message)
                if ok:
                    try:
                        show(checks.dns_lookup(host))
                    except OSError:
                        pass
            elif choice == "3":
                host = input("Host (use your lab/authorized target): ").strip()
                port = int(input("TCP port: "))
                print("OPEN" if checks.port_check(host, port) else "CLOSED/UNREACHABLE")
            elif choice == "4":
                url = input("URL (https://...): ").strip()
                show(checks.http_inspect(url))
            elif choice == "5":
                host = input("TLS host: ").strip()
                show(checks.tls_certificate(host))
            elif choice == "6":
                url = input("URL (https://...): ").strip()
                show(checks.security_headers(url))
            elif choice == "7":
                password = input("Password to evaluate locally: ")
                show(checks.password_score(password))
            elif choice == "8":
                text = input("Text: ")
                print("SHA-256:", checks.hash_text(text, "sha256"))
                print("SHA-512:", checks.hash_text(text, "sha512"))
            elif choice == "0":
                print("Goodbye.")
                return
            else:
                print("Unknown option.")
        except Exception as exc:
            print(f"[!] Error: {exc}")
        pause()
