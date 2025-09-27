# File Processor – Django Text Processing App

## Overview
This project is a Django web application that allows users to upload a text file.  
The application processes the file by shuffling the **inner letters** of each word while keeping the **first and last letters** in place.  
The processed text is then displayed back to the user.

This repository is configured with **Poetry** for dependency management.

---

## Features
- Upload a plain text file via a simple form.
- Shuffle letters inside each word (first and last letter remain unchanged).
- Display the processed text on an output page.

---

## Requirements
- Python 3.13+ (recommended)
- [Poetry](https://python-poetry.org/) for package management

---

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/file-processor.git
   cd file-processor
   ```

2. Install dependencies using Poetry:
   ```bash
   poetry install
   ```
   
3. Activate the virtual environment:
   ```bash
   poetr shell
   ```
   
---

## Usage

1. Start the development server:
   ```bash
   python manage.py runserver
   ```
   
2. Open your browser at:
   ```cpp
   http://127.0.0.1:8000/
   ```
   
3. Upload a .txt file from the homepage form.
4. View the processed text on the output page.

---

## Project structure
```bash
file_processor/
├── pyproject.toml        # Poetry project configuration
├── poetry.lock           # Dependency lock file
├── manage.py             # Django entry point
└── ...                   # Django apps and code
```

---

## Development notes
* You can extend the text processing logic or build additional features (e.g. multiple file formats, download processed file, etc.)
