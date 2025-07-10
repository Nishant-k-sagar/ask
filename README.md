# ask: Natural Language to Shell Command

**ask** is an AI-powered CLI tool that turns plain English into safe, ready-to-run shell commands.  
Powered by Groq and LLaMA 3 70B, it helps you automate the terminal—no scripting required.

---

## 🚀 Quick Start

### 1. Install with pipx (Recommended)

`pipx` keeps `ask` isolated and globally available—no Python or pip conflicts.

**Requirements:**
- Python 3.8+
- pipx (`sudo pacman -S python-pipx`, `sudo apt install pipx`, or `brew install pipx`)

**Install:**

```bash
pipx install git+https://github.com/yourusername/ask.git
```

Or, if you’ve cloned the repo:

```bash
cd ask
pipx install .
```

---

### 2. Set Your Groq API Key

**Linux/macOS:**

```bash
export GROQ_API_KEY="your_api_key_here"
# Add this to ~/.zshrc or ~/.bashrc for future sessions
```

**Windows:**

```cmd
setx GROQ_API_KEY "your_api_key_here"
```

*Restart your terminal after setting.*

---

## 🛠️ Usage

Just type:

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
- For commands like `cd` or `export`, you’ll be prompted to paste the command yourself (since these can’t change your parent terminal’s state).

---

## 🖥️ Standalone Executable (No Python Needed)

### Linux

1. Download `ask` from [Releases](https://github.com/Nishant-k-sagar/ask/tree/master/dist).
2. Make it executable and move it to your PATH:

```bash
chmod +x ask
sudo mv ask /usr/local/bin/ask
```

### Windows

Currently packaged installer or .exe file is not availbale. Install using github repo.<!-- 1. Download `ask.exe` from [Releases](https://github.com/yourusername/ask/releases). -->
<!-- 2. Move it to a folder in your PATH (e.g., `C:\Scripts`). -->

---

## 🔍 How It Works

- Uses Groq’s LLaMA 3 70B model for high-accuracy command generation.
- Adds a safety comment: `# safest`, `# safer`, or `# risky`.
- Copies the command to your clipboard (uses `pyperclip`; Linux users may need `xclip` or `xsel`).
- Detects shell environment commands and guides you to paste them manually.

---

## 🧑‍💻 Local Development

```bash
git clone https://github.com/Nishant-k-sagar/ask.git or
git clone git@github.com:Nishant-k-sagar/ask.git
cd ask
python3 -m venv venv
source venv/bin/activate
pipx install -r requirements.txt
ask "your command in plain English"
```

---

## ❓ Troubleshooting

- **No command or API error**: Check your `GROQ_API_KEY` and internet connection.
- **Clipboard not working**: On Linux, install'pyperclip' globally.
  
- **"Command not found"**: Make sure `ask` is in your `PATH` and is executable.

---

## 🤝 Contributing

PRs are welcome! Open an issue to discuss features or bugs first.

---

## 📄 License

Non-commercial OPEN to all. See [LICENSE](LICENSE).

---

## 🙏 Credits

- [Groq API](https://console.groq.com/)
- [Meta LLaMA 3](https://ai.meta.com/llama/)
- [pyperclip](https://pypi.org/project/pyperclip/)
