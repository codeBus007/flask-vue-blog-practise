from app import create_app, db
from app.models import User

app = create_app()

# shell 测试
@app.shell_context_processor
def make_shell_context():
    return {"db": db, "User": User}
