# Text Analyzer Web Application

A Flask-based web application that provides detailed text analysis, including word count, character count, reading time estimation, and identification of most frequently used words.

## Features

- **Word Count Analysis**: Accurately counts words using regex pattern matching
- **Character Statistics**: 
  - Total character count
  - Character count excluding spaces
- **Structural Analysis**:
  - Sentence count
  - Paragraph count
- **Reading Time Estimation**: Based on average reading speed of 200 words per minute
- **Word Frequency Analysis**: 
  - Identifies the top 5 most common words
  - Excludes common stop words
  - Case-insensitive analysis

## Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd 26-python-web
```

2. Create a virtual environment and activate it:
```bash
python -m venv venv
# On Windows
venv\Scripts\activate
# On Unix or MacOS
source venv/bin/activate
```

3. Install the required packages:
```bash
pip install flask
```

## Usage

1. Start the application:
```bash
python app.py
```

2. Open your web browser and navigate to:
```
http://localhost:5000
```

3. Use the application:
   - Navigate to the "Text Analyzer" page
   - Paste or type your text in the input area
   - Click "Analyze Text" to see the results

## Project Structure

```
26-python-web/
├── app.py              # Main Flask application
├── static/
│   └── css/
│       └── main.css    # Application styling
├── templates/
│   ├── base.html       # Base template
│   ├── home.html       # Home page
│   ├── about.html      # About page
│   ├── post.html       # Text input page
│   └── result.html     # Analysis results page
├── .env                # Environment variables (not tracked)
├── .gitignore         # Git ignore file
└── README.md          # Project documentation
```

## Technical Details

- **Framework**: Flask
- **Frontend**: HTML, CSS
- **Text Processing**: Python's re (regex) module
- **Data Format**: JSON for data transfer between routes

## Features in Detail

### Word Count
- Uses regex pattern `\W+` to split text into words
- Ensures accurate counting by handling multiple spaces and punctuation

### Most Common Words
- Excludes common stop words (a, an, the, etc.)
- Only considers words longer than 2 characters
- Case-insensitive comparison

### Reading Time
- Calculated based on the standard reading speed of 200 words per minute
- Uses regex word splitting for accurate word count

## Contributing

Feel free to submit issues and enhancement requests!
