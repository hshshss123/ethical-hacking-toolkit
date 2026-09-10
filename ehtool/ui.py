import json
import textwrap
from . import checks
from .lessons import LESSONS, get_lesson


WIDTH = 72


def clear_screen():
    print("\033[2J\033[H", end="")


def pause():
    input("\nPress Enter to return to the menu...")


def show(value):
    print(json.dumps(value, indent=2, default=str))


def line(char="═"):
    print(char * WIDTH)


def title(text):
    line()
    print(f"  {text}")
    line()


def paragraph(text):
    print(textwrap.fill(text, width=WIDTH - 4, initial_indent="  ", subsequent_indent="  "))


def bullets(items):
    for item in items:
        wrapped = textwrap.wrap(item, width=WIDTH - 6)
        if wrapped:
            print(f"  • {wrapped[0]}")
            for extra in wrapped[1:]:
                print(f"    {extra}")


def print_lesson(key):
    lesson = get_lesson(key)
    title(f"LEARN: {lesson['name']}")
    print(f"  Category: {lesson['category']}\n")
    print("  WHAT IT DOES")
    paragraph(lesson["what"])
    print("\n  WHY IT MATTERS")
    paragraph(lesson["why"])
    print("\n  KEY IDEAS")
    bullets(lesson["learn"])
    print("\n  SAFETY")
    paragraph(lesson["safe"])


def run_tool(key, tool):
    print_lesson(key)
    print("\n  RUNNING CHECK\n")
    result = tool()
    show(result)
    print("\n  TIP: Read the explanation above before interpreting the result.")


def run_menu():
    while True:
        clear_screen()
        print("╔" + "═" * (WIDTH - 2) + "╗")
        print("║" + "  EHTOOL — ETHICAL HACKING LEARNING LAB".center(WIDTH - 2) + "║")
        print("║" + "  Learn first • Check second • Stay authorized".center(WIDTH - 2) + "║")
        print("╚" + "═" * (WIDTH - 2) + "╝")
        print("\n  BEGINNER TOOLS\n")
        print("  1  System information       — Know your machine")
        print("  2  Connectivity / DNS       — Understand networking")
        print("  3  TCP port check           — Find one reachable service")
        print("  4  HTTP inspection           — Read a web response")
        print("  5  TLS certificate           — Inspect encrypted connections")
        print("  6  Security headers          — Review defensive web settings")
        print("  7  Password strength         — Learn password basics")
        print("  8  SHA-256 / SHA-512         — Learn hashing")
        print("\n  LEARNING")
        print("  9  Browse lessons            — Read what each tool does")
        print("  0  Exit")
        print("\n  ⚠ Authorized use only: test your own systems or systems you have permission to assess.\n")
        choice = input("  Select an option: ").strip()

        try:
            if choice == "1":
                run_tool("system", checks.local_info)
            elif choice == "2":
                print_lesson("connectivity")
                host = input("\n  Host/domain: ").strip()
                ok, message = checks.ping_host(host)
                print(("\n  [+] " if ok else "\n  [-] ") + message)
                if ok:
                    try:
                        print("\n  DNS details:")
                        show(checks.dns_lookup(host))
                    except OSError:
                        pass
            elif choice == "3":
                print_lesson("port")
                host = input("\n  Host (authorized target): ").strip()
                port = int(input("  TCP port: "))
                print("\n  Result:", "OPEN" if checks.port_check(host, port) else "CLOSED/UNREACHABLE")
            elif choice == "4":
                print_lesson("http")
                url = input("\n  URL (https://...): ").strip()
                show(checks.http_inspect(url))
            elif choice == "5":
                print_lesson("tls")
                host = input("\n  TLS host: ").strip()
                show(checks.tls_certificate(host))
            elif choice == "6":
                print_lesson("headers")
                url = input("\n  URL (https://...): ").strip()
                show(checks.security_headers(url))
            elif choice == "7":
                print_lesson("password")
                print("\n  Do not enter a real password you use anywhere else.")
                password = input("  Password to evaluate locally: ")
                show(checks.password_score(password))
            elif choice == "8":
                print_lesson("hash")
                text = input("\n  Text to hash: ")
                print("\n  SHA-256:", checks.hash_text(text, "sha256"))
                print("  SHA-512:", checks.hash_text(text, "sha512"))
            elif choice == "9":
                clear_screen()
                title("LESSON BROWSER")
                for index, lesson in enumerate(LESSONS.values(), start=1):
                    print(f"  {index}. {lesson['name']} — {lesson['category']}")
                print("\n  Enter a module number to learn more.")
                module = input("  Module (1-8): ").strip()
                keys = list(LESSONS.keys())
                if module.isdigit() and 1 <= int(module) <= len(keys):
                    print_lesson(keys[int(module) - 1])
                else:
                    print("\n  Invalid module number.")
            elif choice == "0":
                print("\n  Goodbye. Keep learning—and keep testing with permission.")
                return
            else:
                print("\n  Unknown option.")
        except ValueError:
            print("\n  [!] Please enter a valid number where requested.")
        except Exception as exc:
            print(f"\n  [!] Error: {exc}")
        pause()
