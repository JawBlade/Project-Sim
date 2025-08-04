import openai
import os
from flask import Flask, render_template, request, jsonify

# Set your OpenAI API key
openai.api_key = os.getenv("OPENAI_API_KEY")

app = Flask(__name__)


@app.route("/healthz")
def healthz():
    return "OK", 200


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()
    user_message = data.get("message", "").strip()

    if not user_message:
        return jsonify({"response": "Please enter a question about the classroom."})

    try:
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[
                {
                    "role": "system",
                    "content": (
                        "You are a helpful assistant for a virtual classroom simulation. "
                        "When a user asks about a number, describe what that number refers to in the classroom. "
                        "Here is the classroom layout:\n"
                        "- 1: A UR12e universal robot.\n"
                        "- 2: A mini Universal Robot.\n"
                        "- 3: The TA’s desk with PLCs and computers.\n"
                        "- 4: KUKA robots used for learning.\n"
                        "- 6: A closet full of electronics and parts.\n"
                        "- 7: Student desks with Festo kits, multimeters, PLCs, and computers.\n"
                        "- 8: The teacher’s desk.\n"
                        "- 9: Another Spot robot named Nebula.\n"
                        "Always respond with helpful, clear answers about the classroom. "
                        "Do not answer questions unrelated to the classroom."
                    )
                },
                {"role": "user", "content": user_message}
            ]
        )

        assistant_message = response.choices[0].message["content"]
        return jsonify({"response": assistant_message})

    except Exception as e:
        return jsonify({"response": f"Error: {str(e)}"}), 500


if __name__ == "__main__":
    # Use host="0.0.0.0" and port=5000 for deployment
    app.run(debug=True, host="0.0.0.0", port=5000)
