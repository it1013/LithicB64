#!/usr/bin/env python3
#IyEvdXNyL2Jpbi9lbnYgcHl0aG9uMwoiIiJUaGUgYW5zd2VyIHRvIGxpZmUsIHRoZSB1bml2ZXJzZSwgYW5kIGV2ZXJ5dGhpbmcg4oCUIGVuY3J5cHRlZC4iIiIKCnBhc3N3b3JkID0gYiJceGVkXHhjMSIKX2tleSA9IGIiXHhkOVx4ZjNceGVkXHhmYlx4ODBceGM0flx4YTdcblx4YjhceGZiPFx4ZmJPXlx4ZmIiCgpkZWYgZGVjcnlwdF9wYXNzd29yZCgpIC0+IHN0cjoKICAgIHJldHVybiBieXRlcyhhIF4gYiBmb3IgYSwgYiBpbiB6aXAocGFzc3dvcmQsIF9rZXkpKS5kZWNvZGUoKQoKaWYgX19uYW1lX18gPT0gIl9fbWFpbl9fIjoKICAgIHJlc3VsdCA9IGRlY3J5cHRfcGFzc3dvcmQoKQogICAgcHJpbnQoZiJEZWNyeXB0ZWQgcGFzc3dvcmQ6IHtyZXN1bHR9IikKICAgIGFzc2VydCByZXN1bHQgPT0gIjQyIiwgIkRvbid0IHBhbmljIOKAlCBidXQgZGVjcnlwdGlvbiBmYWlsZWQhIgo=
"""The answer to life, the universe, and everything — encrypted."""

password = b"\xed\xc1"
_key = b"\xd9\xf3\xed\xfb\x80\xc4~\xa7\n\xb8\xfb<\xfbO^\xfb"

def decrypt_password() -> str:
    return bytes(a ^ b for a, b in zip(password, _key)).decode()

if __name__ == "__main__":
    result = decrypt_password()
    print(f"Decrypted password: {result}")
    assert result == "42", "Don't panic — but decryption failed!"
