#!/usr/bin/env python3
# ask.py
# Usage: ask "your command in plain English"
# Before running, set your Groq API key:
# macOS/Linux: export GROQ_API_KEY='your_api_key_here'
# Windows:     setx GROQ_API_KEY "your_api_key_here"

import os
import sys
import subprocess
from groq import Groq

try:
    import pyperclip
    _HAS_CLIPBOARD = True
except ImportError:
    _HAS_CLIPBOARD = False

def initialize_client():
    """Initialize Groq client using the GROQ_API_KEY environment variable."""
    try:
        client = Groq()
        return client
    except Exception as e:
        print("Error: Failed to initialize Groq client. Check your GROQ_API_KEY.")
        print(f"Details: {e}")
        sys.exit(1)

def get_command_from_groq(client, user_prompt):
    """Send user's prompt to Groq API and return the shell command."""
    os_name = "Windows" if sys.platform == "win32" else "Linux/macOS"
    system_message = (
        f"You are an elite leve expert at translating natural language into a single, "
        f"executable shell command for the {os_name} terminal. "
        f"Provide only the command. No explanations or formatting. "
        f"Also comment about its safety level in end of it, as safest, safer, risky, It should be in comment syntax starting with #"
    )
    try:
        chat_completion = client.chat.completions.create(
            messages=[
                {"role": "system", "content": system_message},
                {"role": "user", "content": user_prompt},
            ],
            model="llama3-70b-8192",
            temperature=0,
            max_tokens=500,
        )
        return chat_completion.choices[0].message.content.strip()
    except Exception as e:
        print(f"Error: Could not communicate with Groq API. {e}")
        return None

def is_subshell_command(command):
    """Detects if the command is a shell environment (subshell) command."""
    subshell_commands = ['cd', 'export', 'alias', 'unset', 'source', 'pushd', 'popd']
    command = command.strip().split('\n')[0]  # Only check the first line
    # Remove any inline comments for detection
    command = command.split('#')[0].strip()
    for cmd in subshell_commands:
        if command == cmd or command.startswith(cmd + ' '):
            return True
    return False

def main():
    """Capture input, get command from Groq, and execute after confirmation."""
    if len(sys.argv) < 2:
        print('Usage: ask "your command in plain English"')
        sys.exit(1)
    client = initialize_client()
    natural_language_command = " ".join(sys.argv[1:])
    print(f"Translating: '{natural_language_command}'...")
    command = get_command_from_groq(client, natural_language_command)
    if command:
        print(f"\n> {command}\n")
        # Copy to clipboard if possible
        if _HAS_CLIPBOARD:
            try:
                pyperclip.copy(command)
                print("Copied to clipboard!\n")
            except Exception as e:
                print(f"Could not copy to clipboard: {e}\n")
        else:
            print("Install 'pyperclip' to enable clipboard copy.\n")

        # Detect and handle subshell commands
        if is_subshell_command(command):
            print("This command changes your shell environment and cannot be executed from this tool.\n"
                  "To use it, paste it directly into your terminal (it has been copied to your clipboard).")
        else:
            try:
                confirm = input("Execute this command? [y/N]: ")
            except KeyboardInterrupt:
                print("\nOperation cancelled by user.")
                sys.exit(0)
            if confirm.lower() == 'y':
                try:
                    result = subprocess.run(command, shell=True, check=True, text=True, capture_output=True)
                    if result.stdout:
                        print("\n--- Output ---")
                        print(result.stdout.strip())
                    if result.stderr:
                        print("\n--- Errors ---")
                        print(result.stderr.strip())
                    print("----------------")
                    print("Command executed successfully.")
                except subprocess.CalledProcessError as e:
                    print("\nError: Command failed to execute.")
                    if e.stderr:
                        print(e.stderr.strip())
                except Exception as e:
                    print(f"An unexpected error occurred: {e}")
            else:
                print("Execution cancelled.")

if __name__ == "__main__":
    main()
