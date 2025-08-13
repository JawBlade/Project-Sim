# Project Sim: AI Classroom Assistant

#### Video Demo: <INSERT_YOUTUBE_VIDEO_URL_HERE>

---

### Description

Project Sim is a web-based AI assistant designed to help users interact with a virtual classroom environment. The way you ask question is something like: "What is number 4" or just ask about the numbers in general. Flask should take care of what the numbers should mean. Built with Flask and integrated with OpenAI’s API it allows users to type questions or commands and receive intelligent responses, simulating a helpful classroom guide.

The app features a simple and responsive user interface using Tailwind CSS, enabling smooth interaction on both desktop and mobile devices. Users can input text, submit queries, and get dynamic AI-generated answers displayed on the page, along with natural voice output powered by Eleven Labs. This project demonstrates the integration of modern web development techniques with natural language processing and speech synthesis.

---

### Features

- Flask backend serving the web app and handling API requests.
- Integration with OpenAI API for natural language processing.
- Responsive UI styled with Tailwind CSS.
- Input form with smooth animations and user-friendly design.
- Easy deployment configuration for cloud hosting (Render.com).

---

### Project Structure

- `app.py`: Main Flask application file containing route definitions and server logic.
- `templates/`: Folder containing HTML templates using Jinja2 for rendering responses.
- `static/`: Contains static assets such as CSS and JavaScript files.
- `requirements.txt`: Lists Python dependencies including Flask, OpenAI, Eleven Labs, and Tailwind CSS CDN.
- `README.md`: This documentation file explaining the project.
- `venv/`: Virtual environment (not included in repo, recommended for local dev).

---

### Design Choices & Challenges

I chose Flask for its simplicity, familiarity and flexibility as a backend framework, which fits well with my goal to quickly prototype a web app. The use of OpenAI’s API allowed me to leverage state-of-the-art AI language understanding without building complex NLP models myself.

One challenge was designing a clean and responsive UI that works well on different screen sizes. Tailwind CSS made this easier with its utility-first classes. Another challenge was managing asynchronous communication with the AI and Eleven Labs APIs and updating the frontend dynamically, which I addressed using Flask routes and Jinja templating.

---

### AI Assistance Acknowledgment

While the core logic and design of the project are my own, I used ChatGPT as a helper mainly for frontend suggestions, including the input area design and this README file. All AI assistance has been properly reviewed and integrated by me to ensure the final product reflects my understanding and effort.

---

### How to Run

1. Clone the repo
2. Create a virtual environment: `python -m venv venv`
3. Activate it: `source venv/bin/activate` (Linux/macOS) or `venv\Scripts\activate` (Windows)
4. Install dependencies: `pip install -r requirements.txt`
5. Run the app: `flask run`
6. Open `http://127.0.0.1:5000` in your browser

### OR

go [here](https://project-sim.onrender.com/)

---

Thank you for reviewing my final project for CS50! I hope Project Sim demonstrates my growth in web development and AI integration.
