import os
import sys

# sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))


from core import create_app

app = create_app()

if __name__ == "__main__":
    app.run()

