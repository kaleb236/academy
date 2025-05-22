import dns.resolver

try:
    answers = dns.resolver.resolve('localamr.local')
    ip = answers[0].to_text()
    print(f"Resolved IP: {ip}")
except Exception as e:
    print("DNS lookup failed:", e)
