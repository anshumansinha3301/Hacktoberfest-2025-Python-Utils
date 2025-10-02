# ----------------------------------------------------------------------
# SecurePy Check: Password Strength Checker Utility
# Project for Hacktoberfest 2025 Contribution
# ----------------------------------------------------------------------

import re
import getpass 

def check_password_strength(password):
    """
    Checks the strength of a given password based on complexity rules.

    Args:
        password (str): The password string to evaluate.

    Returns:
        tuple: (score (int), feedback (list of str))
    """
    score = 0
    feedback = []

    min_length = 12
    if len(password) >= min_length:
        score += 3
        feedback.append(f"✅ Length: Greater than or equal to {min_length} characters.")
    elif len(password) >= 8:
        score += 1
        feedback.append("⚠️ Length: Good, but consider using 12+ characters.")
    else:
        feedback.append(f"❌ Length: Too short. Must be at least {min_length} characters for strong rating.")


    has_upper = bool(re.search(r'[A-Z]', password))
    has_lower = bool(re.search(r'[a-z]', password))
    has_digit = bool(re.search(r'\d', password))
    has_symbol = bool(re.search(r'[!@#$%^&*()_+=\-{}[\]|:;"<,>.?/`~]', password))

    char_types = 0
    if has_upper:
        char_types += 1
        feedback.append("✅ Contains Uppercase Letters.")
    else:
        feedback.append("❌ Missing Uppercase Letters.")

    if has_lower:
        char_types += 1
        # Feedback already covered by has_upper/has_lower if both are present
    
    if has_digit:
        char_types += 1
        feedback.append("✅ Contains Digits.")
    else:
        feedback.append("❌ Missing Digits (0-9).")

    if has_symbol:
        char_types += 1
        feedback.append("✅ Contains Symbols/Special Characters.")
    else:
        feedback.append("❌ Missing Symbols (!@#$%...).")

    if char_types == 4:
        score += 4
    elif char_types == 3:
        score += 2
    elif char_types <= 2:
        pass

    return score, feedback

def display_results(score, feedback):
    """Prints the evaluation results in a user-friendly format."""
    
    # Define strength categories
    if score >= 7:
        strength = "💪 Very Strong"
        color = "\033[92m"  # Green
    elif score >= 5:
        strength = "⭐ Strong"
        color = "\033[96m"  # Cyan
    elif score >= 3:
        strength = "⚠️ Moderate"
        color = "\033[93m"  # Yellow
    else:
        strength = "🔥 Weak"
        color = "\033[91m"  # Red

    RESET = "\033[0m"

    print("\n" + "="*40)
    print(f"| {color}PASSWORD STRENGTH: {strength.ljust(20)}{RESET} |")
    print("="*40)
    print("\nDetailed Feedback:")
    for item in feedback:
        print(f"  - {item}")
    
    print("\n" + "-"*40)
    print(f"Overall Score: {score}/7 (Max Score possible is 7)")
    print("-"*40)


if __name__ == "__main__":
    print("\n--- SecurePy Check: Password Strength Evaluator ---")
    print("This utility will check your password complexity. Input is hidden.")

    try:
        # Use getpass to securely input the password without echoing it to the terminal
        password = getpass.getpass("Enter the password to check: ")

        if not password:
            print("\nError: Password cannot be empty.")
        else:
            final_score, final_feedback = check_password_strength(password)
            display_results(final_score, final_feedback)
            
    except Exception as e:
        print(f"\nAn error occurred: {e}")
    finally:
        print("\nThank you for using SecurePy Check.")
