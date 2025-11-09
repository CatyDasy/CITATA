# print("Loading...")
# from todos import load_todos
# from flask import Flask, render_template
# import datetimes as dts
# import datetimeInfo as dtinfo

# app = Flask(__name__)
# import json
# from datetime import datetime


# def grep_todos(name):
        
#     with open(f"static/json/todos-{name}.json", "r", encoding="utf-8") as f:
#         data = json.load(f)

#     day = dts.Day("Asia/Jakarta")

#     time_string = dtinfo.DetailedDatetime("Asia/Jakarta", format_="%I:%M %p")
#     requested = datetime.strptime(time_string, "%I:%M %p").time()

#     # Convert schedule keys to time objects
#     schedule = []
#     for t_str in data["TODOS"][day]:
#         t = datetime.strptime(t_str, "%I:%M %p").time()
#         schedule.append((t, t_str))

#     # sort by time
#     schedule.sort(key=lambda x: x[0])

#     # find the latest time <= requested
#     last_key = None
#     for t, t_str in schedule:
#         if t <= requested:
#             last_key = t_str
#         else:
#             break

#     # if no earlier slot exists, return None (or choose behavior)
#     if last_key is None:
#         return None
    
#     # Filter out rest/meal items
#     todos = data["TODOS"][day][last_key]
#     filtered_todos = [
#         todo for todo in todos 
#         if not any(word in todo.lower() for word in ['istirahat', 'makan', 'tidur'])
#     ]
    
#     return filtered_todos

# @app.route("/")
# def home():
#     return render_template(
#         "index.html",
#         date=dts.Day("Asia/Jakarta"),
#         todos=load_todos("samil"),
#     )


# @app.route("/musa")
# def musa():
#     tdosa = grep_todos("musa")
#     return render_template(
#         "musa.html",
#         day=dts.Day("Asia/Jakarta"),
#         date=dtinfo.DetailedDatetime("Asia/Jakarta", format_="%I:%M %p"),
#         todos=tdosa,
#     )


# @app.route("/samil")
# def samil():
#     tdosa = grep_todos("samil")
#     return render_template(
#         "samil.html",
#         day=dts.Day("Asia/Jakarta"),
#         date=dtinfo.DetailedDatetime("Asia/Jakarta", format_="%I:%M"),
#         todos=tdosa,
#     )


# @app.route("/yusa")
# def yusa():
#     tdosa = grep_todos("yusa")
#     return render_template(
#         "yusa.html",
#         day=dts.Day("Asia/Jakarta"),
#         date=dtinfo.DetailedDatetime("Asia/Jakarta", format_="%I:%M"),
#         todos=tdosa,
#     )

# @app.route("/trials/7248fn/admin/")
# def admin():
#     tdosa = grep_todos("yusa")
#     return render_template(
#         "admin.html",
#         day=dts.Day("Asia/Jakarta"),
#         date=dtinfo.DetailedDatetime("Asia/Jakarta", format_="%I:%M"),
#         todos=tdosa,
#     )               




# if __name__ == "__main__":
#     app.run(debug=True)


#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

print("Loading...")
from todos import load_todos
from flask import Flask, render_template, request, redirect
import datetimes as dts
import datetimeInfo as dtinfo
import json
from datetime import datetime

app = Flask(__name__)

def grep_todos(name):
    with open(f"static/json/todos-{name}.json", "r", encoding="utf-8") as f:
        data = json.load(f)

    day = dts.Day("Asia/Jakarta")
    time_string = dtinfo.DetailedDatetime("Asia/Jakarta", format_="%I:%M %p")
    requested = datetime.strptime(time_string, "%I:%M %p").time()

    schedule = []
    for t_str in data["TODOS"][day]:
        t = datetime.strptime(t_str, "%I:%M %p").time()
        schedule.append((t, t_str))

    schedule.sort(key=lambda x: x[0])

    last_key = None
    for t, t_str in schedule:
        if t <= requested:
            last_key = t_str
        else:
            break

    if last_key is None:
        return None
    
    # Filter out rest/meal items
    todos = data["TODOS"][day][last_key]
    filtered_todos = [
        todo for todo in todos 
        if not any(word in todo.lower() for word in ['istirahat', 'makan', 'tidur'])
    ]
    
    return filtered_todos

def load_completed_todos(name):
    """Load completed todos from JSON file"""
    try:
        with open(f"static/json/completed-{name}.json", "r", encoding="utf-8") as f:
            data = json.load(f)
            day = dts.Day("Asia/Jakarta")
            date = dtinfo.DetailedDatetime("Asia/Jakarta", format_="%Y-%m-%d")
            key = f"{day}_{date}"
            return data.get(key, [])
    except FileNotFoundError:
        return []

def save_completed_todos(name, completed_list):
    """Save completed todos to JSON file"""
    day = dts.Day("Asia/Jakarta")
    date = dtinfo.DetailedDatetime("Asia/Jakarta", format_="%Y-%m-%d")
    key = f"{day}_{date}"
    
    try:
        with open(f"static/json/completed-{name}.json", "r", encoding="utf-8") as f:
            data = json.load(f)
    except FileNotFoundError:
        data = {}
    
    data[key] = completed_list
    
    with open(f"static/json/completed-{name}.json", "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)
def get_all_todos_for_day(name):
    """Bir günün TÜM görevlerini getir (tüm saat dilimleri)"""
    with open(f"static/json/todos-{name}.json", "r", encoding="utf-8") as f:
        data = json.load(f)
    
    day = dts.Day("Asia/Jakarta")
    all_todos = []
    
    # O günün tüm saat dilimlerini topla
    for time_slot, todos in data["TODOS"][day].items():
        # Istirahat/Makan/Tidur hariç
        filtered = [
            todo for todo in todos 
            if not any(word in todo.lower() for word in ['istirahat', 'makan', 'tidur'])
        ]
        all_todos.extend(filtered)
    
    return all_todos


def calculate_completion(name):
    """Kullanıcının bugünkü tamamlama yüzdesini hesapla"""
    day = dts.Day("Asia/Jakarta")
    
    # Toplam görevler
    all_todos = get_all_todos_for_day(name)
    total = len(all_todos)
    
    # Tamamlananlar
    try:
        with open(f"static/json/completed-{name}.json", "r", encoding="utf-8") as f:
            data = json.load(f)
            completed_count = 0
            
            # O günün tüm tamamlananları say
            for key, todos in data.items():
                if key.startswith(day):  # "Senin_04:30 AM", "Senin_02:55 PM"
                    completed_count += len(todos)
            
            percentage = (completed_count / total) * 100 if total > 0 else 0
            
            return {
                "total": total,
                "completed": completed_count,
                "percentage": round(percentage, 1)
            }
    except FileNotFoundError:
        return {"total": total, "completed": 0, "percentage": 0}
    

import pandas as pd

def export_to_excel():
    """Bugünkü performansı Excel'e yaz"""
    users = ["yusa", "musa", "samil"]
    data = []
    
    day = dts.Day("Asia/Jakarta")
    date = dtinfo.DetailedDatetime("Asia/Jakarta", format_="%Y-%m-%d")
    
    for user in users:
        stats = calculate_completion(user)
        data.append({
            "İsim": user.capitalize(),
            "Gün": day,
            "Tarih": date,
            "Toplam Görev": stats["total"],
            "Tamamlanan": stats["completed"],
            "Tamamlanmayan": stats["total"] - stats["completed"],
            "Yüzde (%)": stats["percentage"]
        })
    
    df = pd.DataFrame(data)
    df.to_excel(f"kayitlar_{day}_{date}.xlsx", index=False)

    return f"kayitlar_{day}_{date}.xlsx"
@app.route("/")
def home():
    return render_template(
        "index.html",
        date=dts.Day("Asia/Jakarta"),
        todos=load_todos("samil"),
    )

@app.route("/yusa", methods=["GET", "POST"])
def yusa():
    if request.method == "POST":
        # Get checked items from form
        checked_todos = []
        for key in request.form:
            if key.startswith("checked_"):
                # This checkbox was checked
                index = key.split("_")[1]  # Get the index
                checked_todos.append(index)
        
        # Save to file or variable (you decide where)
        save_completed_todos("yusa", checked_todos)
        
        return redirect("/yusa")
    
    # GET request - show the page
    tdosa = grep_todos("yusa")
    completed = load_completed_todos("yusa")
    return render_template(
        "yusa.html",
        day=dts.Day("Asia/Jakarta"),
        date=dtinfo.DetailedDatetime("Asia/Jakarta", format_="%I:%M"),
        todos=tdosa,
        completed_todos=completed
    )

@app.route("/musa", methods=["GET", "POST"])
def musa():
    if request.method == "POST":
        checked_todos = []
        for key in request.form:
            if key.startswith("checked_"):
                index = key.split("_")[1]
                checked_todos.append(index)
        save_completed_todos("musa", checked_todos)
        return redirect("/musa")
    
    tdosa = grep_todos("musa")
    completed = load_completed_todos("musa")
    return render_template(
        "musa.html",
        day=dts.Day("Asia/Jakarta"),
        date=dtinfo.DetailedDatetime("Asia/Jakarta", format_="%I:%M %p"),
        todos=tdosa,
        completed_todos=completed
    )

@app.route("/samil", methods=["GET", "POST"])
def samil():
    if request.method == "POST":
        checked_todos = []
        for key in request.form:
            if key.startswith("checked_"):
                index = key.split("_")[1]
                checked_todos.append(index)
        save_completed_todos("samil", checked_todos)
        print("LAKU BROO!")
        return redirect("/samil")
    
    tdosa = grep_todos("samil")
    completed = load_completed_todos("samil")
    return render_template(
        "samil.html",
        day=dts.Day("Asia/Jakarta"),
        date=dtinfo.DetailedDatetime("Asia/Jakarta", format_="%I:%M"),
        todos=tdosa,
        completed_todos=completed
    )
@app.route("/trials/7248fn/admin/")
def admin():
    tdosa = grep_todos("yusa")
    return render_template(
        "admin.html",
        day=dts.Day("Asia/Jakarta"),
        date=dtinfo.DetailedDatetime("Asia/Jakarta", format_="%I:%M"),
        todos=tdosa,
    )               


@app.route("/save_todos/<name>", methods=["POST"])
def save_todos(name):
    """Handle form submission and save checked todos"""
    completed_todos = []
    
    # Get all checked checkboxes from the form
    for key, value in request.form.items():
        if key.startswith("todo_"):
            completed_todos.append(value)
    
    # Save to JSON file
    save_completed_todos(name, completed_todos)
    
    # Redirect back to the user's page
    return redirect(f"/{name}")

from flask import send_file

@app.route("/export")
def export():
    """Excel dosyasını indir"""
    filename = export_to_excel()
    return send_file(filename, as_attachment=True)


if __name__ == "__main__":
    app.run(debug=True)
