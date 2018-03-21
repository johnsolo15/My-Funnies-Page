from funnies_page import app, mongo

@app.shell_context_processor
def make_shell_context():
    return {'db': mongo.db}
