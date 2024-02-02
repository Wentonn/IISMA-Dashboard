from flask import (
    Blueprint,
    redirect,
    render_template,
    request,
    url_for,
)
from board.database import get_db

bp = Blueprint("requirement", __name__)

@bp.route("/requirement")
def requirement():
    db = get_db()
    requirements = db.execute(
        """SELECT Uni_Name,Location, GPA, IELTS, TOEFL, DET,Images, Period
        FROM requirement r, University u
        WHERE u.University = r.Uni_Name 
        """
    ).fetchall()

    courses_query = """SELECT University, Course FROM course"""
    courses = db.execute(courses_query).fetchall()

    university_courses = {}
    for course in courses:
        university_name = course["University"]
        if university_name not in university_courses:
            university_courses[university_name] = []
        university_courses[university_name].append(course["Course"])

    unique_regions = [row[0] for row in db.execute("SELECT DISTINCT Region FROM university").fetchall()]
    return render_template("pages/requirement.html",requirements=requirements,unique_regions=unique_regions, university_courses=university_courses)

@bp.route('/requirement/filter',methods=['POST'])
def filter():
    db = get_db()
    filters = {}
    filters['name'] = request.form.get('search_query')
    filters['region'] = request.form.get('region')
    filters['gpa'] = request.form.get('gpa')
    filters['ept_type'] = request.form.get('english_test')
    filters['ept_score'] = request.form.get('english_test_score')
    filters['accept_det'] = request.form.get('accept_det')

    query = """SELECT Uni_Name,Location, GPA, IELTS, TOEFL, DET,Images, Period
        FROM requirement r, University u
        WHERE u.University = r.Uni_Name 
        """
    
    check = """SELECT Uni_Name,Location, GPA, IELTS, TOEFL, DET,Images, Period
        FROM requirement r, University u
        WHERE u.University = r.Uni_Name 
        """
    
    courses_query = """SELECT University, Course FROM course"""
    courses = db.execute(courses_query).fetchall()

    university_courses = {}
    for course in courses:
        university_name = course["University"]
        if university_name not in university_courses:
            university_courses[university_name] = []
        university_courses[university_name].append(course["Course"])

    if filters['name']:    
        query += f" AND Uni_Name LIKE '%{filters['name']}%'"
    
    if filters['region'] != "":
        query += f" AND Region = '{filters['region']}'"
    
    if (filters["ept_type"] != "") and filters['ept_score']:
        if filters['ept_type'] == "ielts":
            query += f" AND IELTS IS NOT NULL AND IELTS < {float(filters['ept_score'])}"
        elif filters['ept_type'] == "toefl":
            query += f" AND TOEFL IS NOT NULL AND TOEFL < {float(filters['ept_score'])}"
        elif filters['ept_type'] == "det":
            query += f" AND DET IS NOT NULL AND DET < '{int(filters['ept_score'])}'"
    
    if filters['gpa']:
        query += f" AND GPA < {float(filters['gpa'])}"
    
    if filters['accept_det'] != "":
        if filters['accept_det'] == 'det-only':
            query += "AND DET IS NOT NULL"
        elif filters["accept_det"] == 'no-det':
            query += "AND DET IS NULL"

    if query != check:
        unique_regions = [row[0] for row in db.execute("SELECT DISTINCT Region FROM university").fetchall()]
        requirements = db.execute(query).fetchall()
        return render_template("pages/requirement.html",requirements=requirements,filters=filters,unique_regions=unique_regions, university_courses=university_courses)
    else:
        return requirement()
