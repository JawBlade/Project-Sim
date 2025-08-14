import os
from flask import Flask, render_template, request, jsonify
import openai

openai.api_key = os.getenv("OPENAI_API_KEY")
app = Flask(__name__)


@app.route('/healthz')
def healthz():
    return "OK", 200


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()
    user_message = data.get("message", "")

    try:
        response = openai.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {
                    "role": "system",
                    "content": (
                        "You are the guide for a virtual classroom simulation. "
                        "Your role is to explain in detail what each numbered object in the classroom is and what it’s used for. "
                        "When the user mentions a number, describe its location, purpose, and any interesting facts about it. "
                        "Do not answer questions unrelated to the classroom.\n\n"
                        "Classroom layout and details:\n"
                        "- 1: A UR12e Universal Robot — a large industrial robotic arm used for automation demonstrations and programming practice.\n"
                        "- 2: A Mini Universal Robot — a smaller, compact version ideal for tabletop training and precision tasks.\n"
                        "- 3: The TA’s desk — equipped with PLCs, computers, and tools for troubleshooting and helping students.\n"
                        "- 4: KUKA Robots — bright orange industrial robots used for hands-on robotics learning and simulation of real-world manufacturing tasks.\n"
                        "- 6: The electronics closet — stocked with spare parts, sensors, wiring, and various electronics for classroom projects.\n"
                        "- 7: Student workstations — desks with Festo learning kits, multimeters, PLCs, and computers for lab exercises.\n"
                        "- 8: The teacher’s desk — the instructor’s main control station with lesson materials and demonstration equipment.\n"
                        "- 9: 'Nebula' — a Boston Dynamics Spot robot used for demonstrations in mobility, automation, and advanced robotics applications.\n\n"
                        "If the user asks about a number, respond with a clear, engaging explanation that helps them visualize its role in the classroom."
                    )
                },
                {"role": "user", "content": user_message}
            ]
        )
        assistant_message = response.choices[0].message.content
        return jsonify({"response": assistant_message})

    except Exception as e:
        return jsonify({"response": f"Error: {str(e)}"}), 500


if __name__ == "__main__":
    app.run(debug=True)
