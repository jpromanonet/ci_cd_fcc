from flask import Flask, request, abort
import subprocess

app = Flask(__name__)

# Define a secret token for webhook verification
SECRET_TOKEN = 'your-secret-token'

@app.route('/pull-repo', methods=['POST'])
def pull_repo():
    # Check if the request contains the correct token
    token = request.headers.get('X-Hub-Signature')
    if token != SECRET_TOKEN:
        abort(403)  # Forbidden if the token is incorrect

    try:
        subprocess.run(["git", "-C", "/path/to/your/repository", "fetch"], check=True)
        subprocess.run(["git", "-C", "/path/to/your/repository", "reset", "--hard", "origin/test"], check=True)
        return "Force pull successful", 200
    except subprocess.CalledProcessError:
        return "Failed to force pull the repository", 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
