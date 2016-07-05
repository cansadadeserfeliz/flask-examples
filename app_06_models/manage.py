import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from flask_script import Manager

from run import create_app


app = create_app()
manager = Manager(app)

if __name__ == '__main__':
    manager.run()
