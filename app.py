from flask import Flask, request, Response, render_template
from pathlib import Path

app = Flask(__name__)

DATA_DIR = Path("./subtitle")
DATA_DIR.mkdir(exist_ok=True)


# =========================
# 首页
# =========================
@app.route("/")
def index():
    return render_template("index.html")


# =========================
# 获取字幕
# =========================
@app.route("/subtitle/read/<video_id>")
def get_subtitle(video_id):

    path = DATA_DIR / f"{video_id}.txt"

    if not path.exists():
        return Response("not found", status=404)

    return Response(
        path.read_text(encoding="utf-8"),
        mimetype="text/plain"
    )


# =========================
# 保存字幕
# =========================
@app.route("/subtitle/save/<video_id>", methods=["POST"])
def save_subtitle(video_id):

    content = request.data.decode("utf-8")

    path = DATA_DIR / f"{video_id}.txt"

    path.write_text(content, encoding="utf-8")

    return {
        "ok": True
    }


if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=8000,
        debug=True
    )