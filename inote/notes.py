from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)
from werkzeug.exceptions import abort

from inote.auth import login_required
from inote.db import get_db

bp = Blueprint('notes', __name__)

@bp.route('/')
def index():
    db = get_db()
    posts = db.execute(
        'SELECT n.id, title, body, created, author_id, username'
        ' FROM note n JOIN user u ON n.author_id = u.id'
        ' ORDER BY created DESC'
    ).fetchall()
    return render_template('notes/index.html', posts=posts)