# ask: Natural Language to Shell Command

**ask** is an AI-powered CLI tool that turns plain English into safe, ready-to-run shell commands.  
Powered by Groq and LLaMA 3 70B, it helps you automate the terminal—no scripting required.

---

## 🚀 Quick Start

### 1. Clone the Repository

Clone the latest version of the project from GitHub:

```bash
git clone https://github.com/Nishant-k-sagar/ask.git
# or using SSH
git clone git@github.com:Nishant-k-sagar/ask.git
cd ask
```

---

### 1. Install with pipx (Recommended)

`pipx` keeps `ask` isolated and globally available—no Python or pip conflicts.

**Requirements:**
- Python 3.8+
- pipx (`sudo pacman -S python-pipx`, `sudo apt install pipx`, or `brew install pipx`)

**Install directly from GitHub:**

```bash
pipx install git+https://github.com/Nishant-k-sagar/ask.git
```

### OR Clone the Repository

Clone the latest version of the project from GitHub:

```bash
git clone https://github.com/Nishant-k-sagar/ask.git
# or using SSH
git clone git@github.com:Nishant-k-sagar/ask.git
cd ask
```

```bash
pipx install .
```

---

### 2. Set Your Groq API Key

**Linux/macOS:**

```bash
export GROQ_API_KEY="your_api_key_here"
nano ~/.zshrc  or nano  ~/.bashrc (for respective terminals)
# Add this line to ~/.zshrc or ~/.bashrc for future sessions
source ~/.zshrc or source ~/.bashrc
```

**Windows:**

```cmd
setx GROQ_API_KEY "your_api_key_here"
```

*Restart your terminal after setting the API key.*

---

## 🛠️ Usage

Once installed, just type:

```bash
ask "your command in plain English"
```

**Examples:**

```bash
ask list all .txt files
ask remove all files ending with .log
ask show disk usage for /home
```

- The tool prints the shell command, copies it to your clipboard, and (if safe) offers to execute it.
- For commands like `cd` or `export`, you’ll be prompted to paste the command yourself (since child processes cannot change the parent shell's state).

---

## 🖥️ Standalone Executable (No Python Needed)

### Linux

1. Download the prebuilt binary from the [Releases](https://github.com/Nishant-k-sagar/ask/tree/master/dist) section.
2. Make it executable and move it to your system `PATH`:

```bash
chmod +x ask
sudo mv ask /usr/local/bin/ask
```

You can now run `ask` from anywhere in your terminal after setting up the groq api key.

### Windows

Currently, no `.exe` installer is available. Please use the `pipx` or local install methods for now.

---

## 🔍 How It Works

- Uses Groq’s LLaMA 3 70B model via API for accurate shell command generation.
- Tags each command with a safety comment: `# safest`, `# safer`, or `# risky`.
- Automatically copies the command to your clipboard using `pyperclip`.
- Commands that modify the shell environment are shown but not executed automatically.

---

## 🧑‍💻 Local Development

If you want to run or develop locally:

```bash
git clone https://github.com/Nishant-k-sagar/ask.git
cd ask
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python ask.py "your command in plain English"
```

> Use `python ask.py "your prompt"` for testing the tool directly.

---

## ❓ Troubleshooting

- **No command or API error**: Check that your `GROQ_API_KEY` is set correctly and your internet connection is stable.
- **Clipboard not working**: On Linux, ensure `pyperclip` works by installing `xclip` or `xsel`:
  
```bash
sudo pacman -S xclip       # Manjaro/Arch
sudo apt install xclip     # Ubuntu/Debian
```

- **"Command not found"**: Ensure `ask` is installed to a location in your system `PATH`.

---

## 🤝 Contributing

Pull Requests are welcome! If you'd like to add features or fix issues, please open an issue first to discuss it.

---

## 📄 License

Non-commercial use allowed. See [LICENSE](LICENSE) for details.

---

## 🙏 Credits

- [Groq API](https://console.groq.com/)
- [Meta LLaMA 3](https://ai.meta.com/llama/)
- [pyperclip](https://pypi.org/project/pyperclip/)
