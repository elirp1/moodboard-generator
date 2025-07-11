# Moodboard & Color Palette Generator 🎨

A Streamlit app for interior designers to create moodboards, extract color palettes, and predict design styles from inspiration images.

## Setup

1. Clone the repo:
   ```bash
   git clone https://github.com/yourusername/moodboard-app.git
   cd moodboard-app
   ```

2. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # or venv\Scripts\activate on Windows
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Run the app:
   ```bash
   streamlit run app.py
   ```

The app will open at `http://localhost:8501`.

## Features

- Extract full color palettes from images
- Create moodboards in a horizontal layout
- Export moodboards and palettes as PDFs
- Detect interior design style from uploaded images (prototype)

## Future Improvements

- Advanced layout options (grid, collage)
- Save and reload project sessions
- Improve style detection using machine learning

# .gitignore

__pycache__/
*.pyc
moodboard.jpg
moodboard.pdf
temp_*.jpg
.env
venv/
saved_projects/
