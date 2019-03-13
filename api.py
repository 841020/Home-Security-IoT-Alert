from flask import Flask, request, jsonify
import copayment

app = Flask(__name__)

@app.route('/register', methods=['POST'])
def register():
    case=request.json
    res=copayment.script(case)
    return jsonify(res)
if __name__ == '__main__':
    app.run(port=5000, debug=True)
