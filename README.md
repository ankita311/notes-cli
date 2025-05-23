# Notes CLI

A simple and intuitive command-line tool for managing your notes efficiently. Built with Python and designed for ease of use.

## ✨ Features

- 📝 Create and manage notes from the command line
- 🔍 Search and organize your notes
- 💾 Persistent storage of your notes
- 🎨 Beautiful terminal interface with Rich formatting
- ⚡ Fast and lightweight

## 🚀 Quick Start (No Installation Required!)

You can run this tool directly without installing it using `pipx`:

```bash
pipx run ankita-notes-cli
```

This will download and run the latest version of the CLI tool without cluttering your system with permanent installations.

### Example Usage

```bash
# Run the CLI
pipx run ankita-notes-cli

# Add a new note
pipx run ankita-notes-cli add --title "Remember to buy groceries"

# List all notes
pipx run ankita-notes-cli list

# Search notes by id
pipx run ankita-notes-cli get-one-note 1
```

## 📦 Alternative Installation Methods

### Using pipx (Recommended)

If you want to install it permanently:

```bash
pipx install ankita-notes-cli
ankita-notes-cli --help
```

### Using pip

```bash
pip install ankita-notes-cli
ankita-notes-cli --help
```

## 🛠️ Usage

```bash
ankita-notes-cli [COMMAND] [OPTIONS]
```

### Available Commands

| Command | Description | Example |
|---------|-------------|---------|
| `add` | Add a new note | `ankita-notes-cli add "My note content"` |
| `list` | List all notes | `ankita-notes-cli list` |
| `get-one-note` | Search notes by id| `ankita-notes-cli get-one-note 1` |
| `delete` | Delete a note | `ankita-notes-cli delete 1` |
| `edit` | Edit an existing note | `ankita-notes-cli edit 1` |
| `help` | Show help information | `ankita-notes-cli --help` |

### Examples

```bash
# Add a note
ankita-notes-cli add "Meeting with team at 3 PM"

# List all notes with formatting
ankita-notes-cli list

# Search for notes containing "meeting"
ankita-notes-cli get-one-note 1

# Delete note with ID 1
ankita-notes-cli delete 1
```

## 🔧 Requirements

- Python 3.6 or higher
- No additional dependencies needed when using `pipx run`

## 🏗️ Development

### Local Development Setup

1. Clone the repository:
```bash
git clone https://github.com/ankita311/notes-cli.git
cd notes-cli
```

2. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install in development mode:
```bash
pip install -e .
```

4. Run the CLI:
```bash
ankita-notes-cli --help
```

### Testing with pipx

To test your local changes with pipx:

```bash
pipx run /path/to/your/notes-cli
```

## 📝 Dependencies

This project uses the following libraries:

- **FastAPI** (0.115.12) - For potential web interface features
- **httpx** (0.28.1) - For HTTP requests
- **Pydantic** (2.11.4) - For data validation
- **Rich** (14.0.0) - For beautiful terminal output
- **Typer** (0.15.4) - For building the CLI interface

## 🤝 Contributing

Contributions are welcome! Here's how you can help:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Make your changes
4. Commit your changes (`git commit -m 'Add some amazing feature'`)
5. Push to the branch (`git push origin feature/amazing-feature`)
6. Open a Pull Request

### Development Guidelines

- Follow PEP 8 style guidelines
- Add tests for new features
- Update documentation as needed
- Ensure all tests pass before submitting

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🐛 Bug Reports & Feature Requests

If you encounter any bugs or have feature requests, please create an issue on [GitHub](https://github.com/ankita311/notes-cli/issues).

## 📧 Contact

**Ankita** - ankita.av.934@gmail.com

Project Link: [https://github.com/ankita311/notes-cli](https://github.com/ankita311/notes-cli)

## 🙏 Acknowledgments

- Thanks to the Python community for the amazing libraries
- Built with ❤️ using Python, Typer, and Rich

---

⭐ If you find this tool useful, please consider giving it a star on GitHub!