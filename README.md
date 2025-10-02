# Hacktoberfest-2025-Python-Utils

# SecurePy Check: Password Strength Evaluator

**Repository Name Suggestion:** `Hacktoberfest-2025-Python-Utils`

**SecurePy Check** is a simple, command-line utility written in Python that evaluates the strength of a user-provided password based on common security criteria like length, complexity, and character variety (uppercase, lowercase, digits, and symbols).

This project is specifically designed to be **beginner-friendly** and is an excellent starting point for new contributors participating in **Hacktoberfest 2025!**

## ✨ Features

* **Secure Input:** Uses the `getpass` module to hide password input in the terminal.

* **Detailed Feedback:** Provides a score and a list of specific checks (e.g., missing digits, good length).

* **Colorized Output:** Uses ANSI escape codes for visually clear results (Strong, Moderate, Weak).

* **Portable:** Single file, zero dependencies outside of the Python standard library.

## 🚀 Getting Started

### Prerequisites

You only need Python 3.6 or newer installed on your system.

### Installation & Usage

git clone https://github.com/YourUsername/Hacktoberfest-2025-Python-Utils.git
cd Hacktoberfest-2025-Python-Utils

**Run the Script:**

python password_checker.py

3. The script will prompt you to enter a password (the input will be invisible).

## 💖 Contributing to Hacktoberfest 2025

We welcome contributions of all sizes! SecurePy Check is designed with new contributors in mind. We aim to merge all constructive Pull Requests (PRs) that adhere to the guidelines and help improve the project.

### Easy Contribution Ideas (Great for First PRs!):

1. **Enhance Feedback Messages:** Improve the clarity or friendliness of the `feedback` strings in `check_password_strength`.

2. **Add a New Criteria:** Implement a check for a new rule (e.g., checking for common dictionary words or consecutive characters).

3. **Add Unit Tests:** Write simple tests using Python's built-in `unittest` module to verify the scoring logic.

4. **Refactor Scoring:** Suggest and implement a more granular or weighted scoring system.

5. **Documentation:** Improve comments, type hinting, or update this README.

### How to Contribute

1. **Fork** this repository.

2. **Clone** your forked repository: `git clone https://github.com/YourUsername/Hacktoberfest-2025-Python-Utils.git`

3. **Create a new branch** for your feature or fix: `git checkout -b fix/issue-name` or `git checkout -b feature/new-check`

4. **Make your changes** in `password_checker.py`.

5. **Commit** your changes: `git commit -m "feat: added new check for dictionary words"` (Use descriptive commit messages!)

6. **Push** to your branch: `git push origin feature/new-check`

7. **Open a Pull Request** against the `main` branch of the original repository.

**Thank you for your contribution!**

