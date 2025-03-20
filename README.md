# crewai-freemodel-code-examples

This repository demonstrates a working agent-task system using `crewai` and free models hosted locally via `Ollama`.

## ✅ Features
- Supports Python versions up to **3.12** (newer versions may face package compatibility issues).
- Automatically detects and loads free Ollama models.
- Provides an alternative to OpenAI API-based code examples — works completely offline with locally hosted models.
- Errors from the original `crewai` examples have been resolved and tested successfully as of **March 20, 2025**.

## 🔧 Setup Instructions

1. **Install Python (<= 3.12)**
   ```bash
   sudo apt update
   sudo apt install python3.12 python3-pip
   ```

2. **Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/crewai-freemodel-code.git
   cd crewai-freemodel-code
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Download Ollama models** from the official site: [Ollama Models](https://ollama.com/)

5. **Run the example script:**
   ```bash
   python example.py
   ```

## 📸 Screenshots
Here's a preview of the working code in action:

![CrewAI Running Example](../screenshots/image-1.png)

![CrewAI Running Example](../screenshots/image-2.png)

## 📚 References
- [CrewAI Documentation](https://learn.crewai.com/)
- [Ollama Official Site](https://ollama.com/)

## 🛠️ Troubleshooting

- If you face package errors with Python versions above **3.12**, downgrade to a compatible version.
- Ensure the Ollama models are downloaded correctly and accessible locally.
- All code blocks have been updated to handle errors from previous `crewai` examples.

## 🎯 Why This Repo?
All `crewai` code examples rely on OpenAI APIs, which is costly. This repo provides a **fully offline alternative** using free models hosted locally with Ollama — ensuring **privacy**, **reliability**, and **no API costs**.

Happy coding! 🚀

