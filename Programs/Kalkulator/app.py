from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html", numbers=["", ""], result=None)

@app.route("/calculate", methods=["POST"])
def calculate():
    action = request.form["action"]

    # RESET
    if action == "reset":
        return render_template("index.html", numbers=["", ""], result=None)

    numbers_raw = request.form.getlist("numbers")

    numbers = []
    for n in numbers_raw:
        n = n.strip()
        if n == "":
            numbers.append("")
        else:
            numbers.append(float(n))

    # STRONA STARTOWA
    if numbers == ["", ""]:
        return render_template("index.html", numbers=numbers, result=None)

    nums = [x for x in numbers if isinstance(x, float)]

    if not nums:
        return render_template("index.html", numbers=numbers, result=None)

    if action == "add":
        result = sum(nums)
    elif action == "sub":
        result = nums[0] - sum(nums[1:])
    elif action == "mul":
        result = 1
        for n in nums:
            result *= n
    elif action == "div":
        result = nums[0]
        for n in nums[1:]:
            result /= n

    return render_template("index.html", numbers=numbers, result=result)

if __name__ == "__main__":
    app.run(debug=True)
