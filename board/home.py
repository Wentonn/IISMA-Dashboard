from flask import (
    Blueprint,
    redirect,
    render_template,
    request,
    url_for,
    session,
)

from board.database import get_db

bp = Blueprint("home", __name__)

@bp.route('/')
def home():
    db = get_db()
    query = """SELECT Type_,Year_,sum(total_students) as sum 
    FROM intake 
    GROUP BY Type_,Year_
    ORDER BY Year_"""
    iisma_data = db.execute(query).fetchall()
    for i in iisma_data:
        print(i["Type_"])
    return render_template('pages/home.html',iisma_data=iisma_data) 