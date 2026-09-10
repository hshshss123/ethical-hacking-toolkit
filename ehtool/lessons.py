"""Beginner-friendly explanations for EHTool modules."""

LESSONS = {
    "system": {
        "name": "Local System Information",
        "category": "Orientation",
        "what": "Shows basic information about the computer running EHTool.",
        "why": "Security work starts with knowing your own environment. This is useful when documenting a lab machine or troubleshooting a security check.",
        "learn": [
            "Hostname is the computer's local name.",
            "FQDN is the fully qualified domain name when one is available.",
            "The Python and OS values tell you which runtime environment produced the result.",
        ],
        "safe": "Runs locally and does not probe another device.",
    },
    "connectivity": {
        "name": "Connectivity / DNS",
        "category": "Networking Basics",
        "what": "Checks whether a hostname resolves and whether TCP port 80 is reachable.",
        "why": "This teaches the difference between name resolution and network connectivity.",
        "learn": [
            "DNS converts a hostname such as example.com into an IP address.",
            "A host can resolve in DNS even when a particular TCP port is closed.",
            "TCP connectivity means a connection to a specific port succeeded; it does not prove the service is secure.",
        ],
        "safe": "Use your own machine, a lab, or a target you are explicitly authorized to test.",
    },
    "port": {
        "name": "TCP Port Check",
        "category": "Networking Basics",
        "what": "Attempts a TCP connection to one host and one port.",
        "why": "Open ports are entry points where network services may be listening. Learning to identify them is a basic security skill.",
        "learn": [
            "A port number identifies a TCP service endpoint.",
            "OPEN means the connection succeeded from your machine.",
            "CLOSED/UNREACHABLE can mean the service is not listening, a firewall is blocking it, or the path is unavailable.",
        ],
        "safe": "Check only systems you own or have permission to assess.",
    },
    "http": {
        "name": "HTTP Inspection",
        "category": "Web Basics",
        "what": "Makes an HTTP GET request and displays a few response details.",
        "why": "It helps beginners understand what a web server sends back before learning deeper web-security testing.",
        "learn": [
            "The status code tells you whether the request succeeded or was redirected or rejected.",
            "Content-Type describes the kind of data returned.",
            "The Server header, when present, may identify software but should not be treated as definitive inventory.",
        ],
        "safe": "Prefer your own website, local lab, or a service where testing is authorized.",
    },
    "tls": {
        "name": "TLS Certificate Inspection",
        "category": "Web Security",
        "what": "Connects to a TLS service and shows certificate metadata and the negotiated TLS version.",
        "why": "TLS protects data in transit. Certificate inspection teaches how encrypted web connections establish identity and trust.",
        "learn": [
            "The issuer is the certificate authority that signed the certificate.",
            "notBefore and notAfter describe the certificate's validity period.",
            "The TLS version is the protocol version negotiated for the connection.",
        ],
        "safe": "This is an observation tool; it does not attempt to break encryption.",
    },
    "headers": {
        "name": "HTTP Security Headers",
        "category": "Web Security",
        "what": "Checks for several common HTTP response security headers.",
        "why": "Security headers can reduce common browser-side risks and are useful in defensive web reviews.",
        "learn": [
            "HSTS helps browsers prefer HTTPS after policy is received.",
            "Content-Security-Policy can restrict which content sources a browser may load.",
            "X-Content-Type-Options reduces MIME-type sniffing behavior.",
            "X-Frame-Options can restrict framing by other pages.",
            "Referrer-Policy controls how much referrer information browsers send.",
        ],
        "safe": "This is a passive defensive check; it does not exploit missing headers.",
    },
    "password": {
        "name": "Password Strength Estimator",
        "category": "Identity Basics",
        "what": "Rates a password locally using length and character variety heuristics.",
        "why": "It teaches why longer passwords and passphrases are generally harder to guess.",
        "learn": [
            "Longer passwords increase the number of possible guesses.",
            "Character variety can increase the search space, but length is especially important.",
            "This is a simple educational heuristic, not a breach database or password-cracking estimate.",
        ],
        "safe": "Evaluation happens locally. Do not enter a real password you use elsewhere.",
    },
    "hash": {
        "name": "SHA-256 / SHA-512 Hashing",
        "category": "Cryptography Basics",
        "what": "Creates cryptographic hash values from text.",
        "why": "Hashing is widely used for integrity checks, identifiers, and secure storage designs when used appropriately.",
        "learn": [
            "A cryptographic hash is a one-way function designed to make it difficult to recover the original input.",
            "The same input produces the same digest for the same algorithm.",
            "A tiny input change produces a very different digest, making hashes useful for detecting changes.",
        ],
        "safe": "This operation is local and does not send the text to a network service.",
    },
}


def get_lesson(key: str):
    return LESSONS[key]
