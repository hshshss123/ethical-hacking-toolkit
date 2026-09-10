import hashlib
import socket
import ssl
import urllib.parse
import urllib.request


def local_info():
    return {
        "hostname": socket.gethostname(),
        "fqdn": socket.getfqdn(),
        "python": __import__("platform").python_version(),
        "os": __import__("platform").platform(),
    }


def ping_host(host: str, timeout: float = 3.0):
    try:
        with socket.create_connection((host, 80), timeout=timeout):
            return True, f"TCP connectivity to {host}:80 succeeded"
    except OSError:
        try:
            socket.gethostbyname(host)
            return True, f"DNS resolution for {host} succeeded; TCP/80 was unavailable"
        except OSError as exc:
            return False, str(exc)


def dns_lookup(host: str):
    return socket.gethostbyname_ex(host)


def port_check(host: str, port: int, timeout: float = 2.0):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.settimeout(timeout)
        return sock.connect_ex((host, port)) == 0


def http_inspect(url: str):
    req = urllib.request.Request(url, headers={"User-Agent": "EHTool/0.1"}, method="GET")
    with urllib.request.urlopen(req, timeout=8) as response:
        return {
            "url": response.geturl(),
            "status": response.status,
            "content_type": response.headers.get("Content-Type", ""),
            "server": response.headers.get("Server", ""),
        }


def security_headers(url: str):
    req = urllib.request.Request(url, headers={"User-Agent": "EHTool/0.1"}, method="HEAD")
    with urllib.request.urlopen(req, timeout=8) as response:
        headers = {k.lower(): v for k, v in response.headers.items()}
    expected = [
        "strict-transport-security",
        "content-security-policy",
        "x-content-type-options",
        "x-frame-options",
        "referrer-policy",
    ]
    return {name: headers.get(name) for name in expected}


def tls_certificate(host: str, port: int = 443):
    context = ssl.create_default_context()
    with socket.create_connection((host, port), timeout=5) as raw:
        with context.wrap_socket(raw, server_hostname=host) as sock:
            cert = sock.getpeercert()
            return {
                "subject": cert.get("subject"),
                "issuer": cert.get("issuer"),
                "version": cert.get("version"),
                "notBefore": cert.get("notBefore"),
                "notAfter": cert.get("notAfter"),
                "tls_version": sock.version(),
            }


def password_score(password: str):
    score = 0
    score += len(password) >= 12
    score += any(c.islower() for c in password)
    score += any(c.isupper() for c in password)
    score += any(c.isdigit() for c in password)
    score += any(not c.isalnum() for c in password)
    labels = ["very weak", "weak", "fair", "good", "strong", "very strong"]
    return {"score": score, "rating": labels[score]}


def hash_text(text: str, algorithm: str = "sha256"):
    if algorithm not in {"sha256", "sha512"}:
        raise ValueError("Unsupported hash algorithm")
    return hashlib.new(algorithm, text.encode("utf-8")).hexdigest()
