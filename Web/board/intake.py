from flask import (
    Blueprint,
    redirect,
    render_template,
    request,
    url_for,
    session,
)

from board.database import get_db

bp = Blueprint("intake",__name__)

@bp.route('/intake')
def intake():
    db = get_db()
    intakes = db.execute(
        """SELECT location,GPA_Min,GPA_Max,TOEFL_Score_Min,TOEFL_Score_Max,IELTS_Score_Min,IELTS_Score_Max,Duolingo_English_Test_Score_Min,Duolingo_English_Test_Score_Max,Total_Students,Uni_Name,Type_,Year_,Images
        FROM intake i, university u 
        WHERE u.University = i.Uni_name"""
    ).fetchall()

    unique_regions = [row[0] for row in db.execute("SELECT DISTINCT Region FROM university").fetchall()]


    return render_template("pages/intake.html",intakes=intakes, unique_regions=unique_regions)


@bp.route('/intake/set_ept/<ept>')
def set_ept(ept):
    session['ept'] = ept
    return(redirect(url_for('intake.intake')))

@bp.route('/intake/filter',methods=["POST"])
def filter():
    db = get_db()
    filters = {}
    # Get filter values from the form
    filters['name'] = request.form.get('search_query')
    filters['type'] = request.form.get('type')
    filters['year'] = request.form.get('year')
    filters['gpa'] = request.form.get('gpa')
    filters['ept_type'] = request.form.get('english_test')
    filters['ept_score'] = request.form.get('english_test_score')
    filters['regions'] = request.form.get('region')

    
    query =  """SELECT location,GPA_Min,GPA_Max,TOEFL_Score_Min,TOEFL_Score_Max,IELTS_Score_Min,IELTS_Score_Max,Duolingo_English_Test_Score_Min,Duolingo_English_Test_Score_Max,Total_Students,Uni_Name,Type_,Year_,Images
    FROM intake i, university u 
    WHERE u.University = i.Uni_name"""

    check = """SELECT location,GPA_Min,GPA_Max,TOEFL_Score_Min,TOEFL_Score_Max,IELTS_Score_Min,IELTS_Score_Max,Duolingo_English_Test_Score_Min,Duolingo_English_Test_Score_Max,Total_Students,Uni_Name,Type_,Year_,Images
    FROM intake i, university u 
    WHERE u.University = i.Uni_name"""
    
    if filters['name']:    
        query += f" AND Uni_Name LIKE '%{filters['name']}%'"

    if filters['type'] != "":
        query += f" AND Type_ = '{filters['type']}'"

    if filters['gpa']:
        query += f" AND GPA_Min < {float(filters['gpa'])}"

    if filters['year'] != "":
        query += f" AND YEAR_ = {int(filters['year'])}"

    
    if (filters["ept_type"] != "" or session['ept'] != "All") and filters['ept_score']:
        if filters['ept_type'] == "ielts" or session['ept']  == "IELTS" :
            query += f" AND IELTS_Score_Min IS NOT NULL AND IELTS_Score_Min <= {float(filters['ept_score'])}"
        elif filters['ept_type'] == "toefl" or session['ept']  == "TOEFL":
            query += f" AND TOEFL_Score_Min IS NOT NULL AND TOEFL_Score_Min <= {float(filters['ept_score'])}"
        elif filters['ept_type'] == "det" or session['ept']  == "DET":
            query += f" AND Duolingo_English_Test_Score_Min IS NOT NULL AND Duolingo_English_Test_Score_Min <= '{int(filters['ept_score'])}' AND EXISTS (SELECT 1 FROM requirement r WHERE r.Uni_Name = i.Uni_Name AND r.DET IS NOT NULL"

    if filters['regions']:
        query += f" AND Region = '{filters['regions']}'"
    
    if query != check:
        unique_regions = [row[0] for row in db.execute("SELECT DISTINCT Region FROM university").fetchall()]
        intakes = db.execute(query).fetchall()
        return render_template("pages/intake.html", intakes=intakes,unique_regions=unique_regions, filters=filters,session=session)
    else:
        return intake()
