from funnies_page import app, db
from funnies_page.models import User, Comic

@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'User': User, 'Comic': Comic}
