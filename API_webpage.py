from flask import Flask, request

app = Flask(__name__)

@app.route("/test")
def test():
    name = request.args.get("name")
    mobile_number = request.args.get("mobile")
    mail = request.args.get('mail')

    return "this is my first function for get {} {} {}".format(name, mobile_number, mail)


'''@app.route('/get_data')
def get_data_from():
    db = request.args.get('db')
    tn = request.args.get('tn')
    try:
        con = conn.connect(host="localhost", user="root", password="Jaijai1@11", database=db)
        cur = con.cursor(dictionary=True)
        cur.execute(f'select * from {tn}')
        data = cur.fetchall()
        con.commit()
        con.close()
    except Exception as e:
        return jsonify(str(e))

    return jsonify(data)
'''

if __name__ == "__main__":
    app.run(port=602)