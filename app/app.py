import os
from pathlib import Path

from flask import Flask, jsonify, request, render_template

from .utils import resolve_posts_lookup

template_dir = Path('./static/templates').absolute()
static_dir = Path('./static').absolute()


app = Flask(__name__,
            template_folder=template_dir,
            static_folder=static_dir)

app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True


@app.route('/', methods=['GET', 'POST'])
def index():
    """
    root route for the website, it process the requests and returns a template or a json response
    :return: template || json
    """
    user_email = request.values.get('email', False)

    data, status_code = resolve_posts_lookup(user_email=user_email)

    if request.method == 'POST':
        return jsonify(data['response']), status_code

    return render_template('index.html', formatted_data=data['response'], status_code=status_code)


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
