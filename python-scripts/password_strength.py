#!/usr/bin/env python3
"""
password_strength.py
Simple password strength checker for educational purposes.
Usage: python password_strength.py
"""

import re

def score_password(pw: str) -> int:
    score = 0
    if len(pw) >= 8:
        score += 2
    elif len(pw) >= 6:
        score += 1

    if re.search(r"[a-z]", pw):
        score += 1
    if re.search(r"[A-Z]", pw):
        score += 1
    if re.search(r"\d", pw):
        score += 1
    if re.search(r"[!@#\$%\^&\*\(\)_\+\-=\[\]\{\};:'\",\.<>\/\?\\\|`~]", pw):
        score += 2
    if len(set(pw)) < len(pw) // 2:  # too many repeated chars
        score -= 1

    return max(score, 0)

def grade(score: int) -> str:
    if score >= 6:
        return "Strong"
    if score >= 4:
        return "Moderate"
    return "Weak"

def suggestions(pw: str) -> list:
    tips = []
    if len(pw) < 12:
        tips.append("Use a longer password (12+ characters recommended).")
    if not re.search(r"[A-Z]", pw):
        tips.append("Include at least one uppercase letter.")
    if not re.search(r"[a-z]", pw):
        tips.append("Include at least one lowercase letter.")
    if not re.search(r"\d", pw):
        tips.append("Include at least one digit.")
    if not re.search(r"[!@#\$%\^&\*\(\)_\+\-=\[\]\{\};:'\",\.<>\/\?\\\|`~]", pw):
        tips.append("Include at least one special character (e.g. !, #, $).")
    if len(set(pw)) < len(pw) // 2:
        tips.append("Avoid repeating the same character many times.")
    if not tips:
        tips.append("Looks good — consider using a passphrase or a password manager.")
    return tips

def main():
    print("Password Strength Checker (educational)")
    pw = input("Enter a password to check: ").strip()
    if not pw:
        print("No password entered. Exiting.")
        return
    s = score_password(pw)
    print(f"\nScore: {s} / 8")
    print(f"Grade: {grade(s)}\n")
    print("Suggestions:")
    for t in suggestions(pw):
        print(" -", t)

if __name__ == "__main__":
    main()
Add password_strength example
