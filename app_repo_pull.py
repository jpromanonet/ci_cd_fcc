from flask import Flask
import subprocess

app = Flask(__name__)

@app.route('/pull-repo', methods=['POST'])
def pull_repo():
    try:
        # Fetch the latest changes from the remote repository
        subprocess.run(["git", "-C", "/path/to/your/repository", "fetch"], check=True)
        # Force reset the local branch to match the remote 'test' branch
        subprocess.run(["git", "-C", "/path/to/your/repository", "reset", "--hard", "origin/test"], check=True)  # Replace 'test' with your branch name
        return "Force pull successful", 200
    except subprocess.CalledProcessError:
        return "Failed to force pull the repository", 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
