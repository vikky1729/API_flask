"""Converting multiple entries in postman to individual entries in SQL
 names = [Vignesh , Sampath, Vishal]
 numbers = [1,2,3]  to
 {1:'Vignesh , 2:'Sampath', 3:'Vishal'}"""

from flask import Flask,request,jsonify

app = Flask(__name__)
# /test is the url/function name
@app.route('/test1',methods =['POST'])

def test():
    if (request.method == 'POST'):
        try:
            names = request.json["names"]
            ids = request.json["id"]
            d = {}
            if type(names) == list:
                for i in range(0, len(names)):
                    d[names[i]] = ids[i]
                return jsonify(str(d))
            elif type(names) == str:
                d[names] = ids
                return jsonify(str(d))

        except Exception as e:
            return jsonify(str(e))

if __name__== '__main__':
#by default the port=1000
    app.run(port=2000)