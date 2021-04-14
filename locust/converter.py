from flask import Flask

converter = {
    "DH": lambda d: d * 24,  # day to hours
    "HM": lambda h: h * 60,  # hour to minutes
    "MS": lambda m: m * 60,  # minute to seconds
    "DM": lambda d: d * 1440,  # day to minutes
    "DS": lambda d: d * 86400,  # day to seconds
    "HS": lambda h: h * 3600,
}  # hour to seconds

app = Flask(__name__)


@app.route("/<rule>/<int:value>")
def conversion(rule, value):
    try:
        return str(converter[rule.upper()](value))
    except KeyError:
        return "Rule for conversion not found", 404


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
