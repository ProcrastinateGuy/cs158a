#!/usr/bin/env python3
"""
secureget.py
Connect to www.google.com:443 using TLS, request '/', and save the response HTML to response.html.
"""

import socket
import ssl
import gzip
import zlib

HOST = "www.google.com"
PORT = 443
OUTFILE = "response.html"

def main():
    # Build a simple HTTP/1.1 request. Connection: close ensures the server will close the socket
    # after sending the response so we can read until EOF.
    request = (
        "GET / HTTP/1.1\r\n"
        f"Host: {HOST}\r\n"
        "User-Agent: secureget/1.0\r\n"
        "Accept: */*\r\n"
        "Connection: close\r\n"
        "\r\n"
    ).encode("ascii")

    context = ssl.create_default_context()  # use system CA certs

    # create TCP connection then wrap with TLS
    with socket.create_connection((HOST, PORT)) as sock:
        with context.wrap_socket(sock, server_hostname=HOST) as ssock:
            # send request
            ssock.sendall(request)

            # read until the server closes the connection
            response_chunks = []
            while True:
                chunk = ssock.recv(4096)
                if not chunk:
                    break
                response_chunks.append(chunk)

    response_bytes = b"".join(response_chunks)

    # Separate headers and body
    header_end = response_bytes.find(b"\r\n\r\n")
    if header_end == -1:
        print("Warning: no HTTP header separator found; saving raw response.")
        headers_raw = b""
        body = response_bytes
    else:
        headers_raw = response_bytes[:header_end].decode("iso-8859-1")  # headers are ASCII-ish
        body = response_bytes[header_end + 4 :]

    # Parse headers into a dict for ease of use
    headers = {}
    for line in headers_raw.splitlines():
        if ":" in line:
            k, v = line.split(":", 1)
            headers[k.strip().lower()] = v.strip()

    # If Content-Encoding indicates compression, try to decompress common encodings
    content_encoding = headers.get("content-encoding", "").lower()
    final_body = body
    try:
        if content_encoding == "gzip":
            final_body = gzip.decompress(body)
        elif content_encoding in ("deflate", "zlib"):
            # try raw zlib inflate; if it fails try raw DEFLATE (wbits=-15)
            try:
                final_body = zlib.decompress(body)
            except zlib.error:
                final_body = zlib.decompress(body, -zlib.MAX_WBITS)
        elif content_encoding == "br":
            # brotli not in standard library; if needed, user can install brotli and handle it.
            print("Note: response uses brotli (br) encoding — saved compressed body as-is.")
        else:
            # no or unknown encoding -> keep as-is
            pass
    except Exception as e:
        print(f"Warning: failed to decompress body ({content_encoding}): {e}. Saving raw body.")

    # Write the (decompressed if possible) body to file
    with open(OUTFILE, "wb") as f:
        f.write(final_body)

    print(f"Saved {len(final_body)} bytes to {OUTFILE}")
    # Optionally print status line
    if headers_raw:
        first_line = headers_raw.splitlines()[0] if headers_raw.splitlines() else ""
        print("HTTP status:", first_line)

if __name__ == "__main__":
    main()
