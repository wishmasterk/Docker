# app.py
from flask import Flask, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        # Grab the submitted value; assume it’s an integer or default to 0
        try:
            n = int(request.form.get("number", "0"))
        except ValueError:
            n = 0

        # Build a simple HTML response with the table
        rows = ""
        for i in range(1, 11):
            rows += f"<tr><td>{i}</td><td>{i * n}</td></tr>"

        return f"""
        <html>
          <body>
            <h3>Multiplication Table of {n}</h3>
            <table border="1" cellpadding="5" cellspacing="0">
              <tr><th>Multiplier</th><th>Product</th></tr>
              {rows}
            </table>
            <p><a href="/">Go back</a></p>
          </body>
        </html>
        """

    # If GET, show a basic form
    return """
    <html>
      <body>
        <h3>Enter a Number:</h3>
        <form method="POST">
          <input type="number" name="number" min="1" required>
          <button type="submit">Show Table</button>
        </form>
      </body>
    </html>
    """

if __name__ == "__main__":
    # Run on http://127.0.0.1:5000/ by default
    app.run(host = "0.0.0.0", debug=True)
