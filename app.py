# let's import the flask
from flask import Flask, render_template, request, redirect, url_for
import os # importing operating system module
import re
import json

app = Flask(__name__, template_folder='templates')
# to stop caching static file
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0

@app.route('/') # this decorator create the home route
def home():
    techs = ['HTML', 'CSS', 'JavaScript', 'Python', 'Flask']
    name = '30 Days Of Python Programming'
    return render_template('home.html', techs=techs, name=name, title='Home')

@app.route('/about')
def about():
    name = '30 Days Of Python Programming'
    return render_template('about.html', name=name, title='About Us')

@app.route('/result')
def result():
    if 'text_analysis' not in request.args:
        return redirect(url_for('post'))
    try:
        analysis_str = request.args.get('text_analysis', '{}')
        analysis = json.loads(analysis_str)
        return render_template('result.html', analysis=analysis)
    except json.JSONDecodeError:
        return redirect(url_for('post'))

@app.route('/post', methods=['GET', 'POST'])
def post():
    name = 'Text Analyzer'
    if request.method == 'GET':
        return render_template('post.html', name=name, title=name)
    if request.method == 'POST':
        content = request.form['content']
        
        # Perform text analysis
        analysis = {
            "word_count": len(content.split()),
            "char_count": len(content),
            "char_count_no_space": len(content.replace(" ", "")),
            "sentence_count": len([s for s in content.split('.') if s.strip()]),
            "paragraph_count": len([p for p in content.split('\n\n') if p.strip()]),
            "most_common_words": [],
            "reading_time": len(re.split(r'\W+', content)) / 200  # Average reading speed of 200 words per minute
        }
        
        # Get most common words (excluding common stop words)
        words = re.split(r'\W+', content.lower())
        stop_words = set(['the', 'a', 'an', 'and', 'or', 'but', 'in', 'on', 'at', 'to', 'for', 'of', 'with', 'by'])
        word_freq = {}
        for word in words:
            if word not in stop_words and len(word) > 2:
                word_freq[word] = word_freq.get(word, 0) + 1
        # Convert tuples to lists for JSON serialization
        most_common = sorted(word_freq.items(), key=lambda x: x[1], reverse=True)[:5]
        analysis["most_common_words"] = [[word, count] for word, count in most_common]
        
        return redirect(url_for('result', text_analysis=json.dumps(analysis)))

if __name__ == "__main__":
    # for deployment we use the environ
    # to make it work for both production and development
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=True, host='0.0.0.0', port=port)