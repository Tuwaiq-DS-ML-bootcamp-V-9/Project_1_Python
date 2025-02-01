from flask import Flask, request, jsonify, Response
from flask_cors import CORS
import random

app = Flask(__name__)
CORS(app)

# In-memory task storage (list of dictionaries)
tasks = []

# List of motivation quotes
quotes = [
    "العلم يُصلح الأمور التي يُفسدها الجهل. – ابن خلدون",
    "من جدّ وجد، ومن زرع حصد. – المثل العربي",
    "ليس الجهل عدم العلم، إنما الجهل أن تعتقد أنك تعلم ما لا تعلم. – ابن رشد",
    "العلم بلا عمل جنون، والعمل بلا علم لا يكون. – الإمام الغزالي",
    "غاية العلم الخير. – الفارابي",
    "إذا لم تزد على الحياة شيئًا، كنت أنت زائدًا عليها. – مصطفى الرافعي",
    "إذا كنتَ ذا رأيٍ فكن ذا عزيمةٍ، فإن فسادَ الرأي أن تترددا. – المتنبي",
    "التعليم كالسراج، من أمسكه أضاء طريقه وطريق الآخرين. – عبد الرحمن الكواكبي",
    "العقل نور، والجهل ظلام. – ابن سينا",
    "من لم يتعلم في صغره لم يتقدم في كبره. – الإمام علي بن أبي طالب",
    "الحكمة أن تعرف الحق وتعمل به. – ابن حزم الأندلسي",
    "اطلبوا العلم ولو في الصين. – حديث نبوي شريف",
    "العلم لا يُعطيك بعضه حتى تُعطيه كُلَّك. – الجاحظ",
    "من لم يحركه الحب، فالميتة أولى به. – ابن سينا",
    "كل إنسان يولد عالِمًا، وإنما يذهب به الجهل إلى الضلال. – أبو حيان التوحيدي",
    "الرأي قبل شجاعة الشجعان، هو أولٌ وهي المحل الثاني. – المتنبي",
    "العلم بحر لا ساحل له، فكلما شربت منه، ازددت عطشًا. – ابن الجوزي",
    "من لم يصبر على ذل التعلم ساعة، بقي في ذل الجهل أبدًا. – ابن القيم",
    "العلم يرفع بيوتًا لا عماد لها، والجهل يهدم بيوت العز والكرم. – أحمد شوقي",
    "لا تقل قد فشلت، قل لم أنجح بعد. – أحمد زويل"
]

# Helper function to generate a unique ID for tasks
def generate_id():
    return max([task["id"] for task in tasks], default=0) + 1  # Ensure unique IDs

# Fetch all tasks
@app.route("/tasks", methods=["GET"])
def get_tasks():
    return jsonify(tasks), 200

# Add a new task
@app.route("/tasks", methods=["POST"])
def add_task():
    data = request.get_json()
    if not data or not data.get("title"):
        return jsonify({"error": "Title is required"}), 400

    new_task = {
        "id": generate_id(),
        "title": data.get("title"),
        "completed": False,
        "deadline": data.get("deadline"),
        "priority": data.get("priority"),
        "notes": data.get("notes")
    }
    tasks.append(new_task)
    return jsonify({"message": "Task added successfully!", "task": new_task}), 201

# Get a specific task
@app.route("/tasks/<int:task_id>", methods=["GET"])
def get_task(task_id):
    task = next((task for task in tasks if task["id"] == task_id), None)
    if task is None:
        return jsonify({"error": "Task not found"}), 404
    return jsonify(task), 200

# Update task
@app.route("/tasks/<int:task_id>", methods=["PUT"])
def update_task(task_id):
    task = next((task for task in tasks if task["id"] == task_id), None)
    if task is None:
        return jsonify({"error": "Task not found"}), 404

    data = request.get_json()
    task["title"] = data.get("title", task["title"])
    task["deadline"] = data.get("deadline", task["deadline"])
    task["priority"] = data.get("priority", task["priority"])
    task["notes"] = data.get("notes", task["notes"])
    task["completed"] = data.get("completed", task["completed"])

    return jsonify({"message": "Task updated successfully!", "task": task}), 200

# Delete task
@app.route("/tasks/<int:task_id>", methods=["DELETE"])
def delete_task(task_id):
    global tasks
    tasks = [task for task in tasks if task["id"] != task_id]
    return jsonify({"message": "Task deleted successfully!"}), 200

# Get a random motivation quote using a lambda function
@app.route("/quote", methods=["GET"])
def get_quote():
    get_random_quote = lambda: random.choice(quotes)  # Lambda function to get a random quote
    random_quote = get_random_quote()
    return jsonify({"quote": random_quote})

if __name__ == "__main__":
    app.run(debug=True)