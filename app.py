from flask import Flask, render_template, request, jsonify
import test_module

import query_on_whoosh



app = Flask(__name__)
app.config.update(JSONIFY_PRETTYPRINT_REGULAR=True)
#app.run(host="3.137.164.121",debug=True, port=8080)
#app.run(host="0.0.0.0", debug=True, port = 8080)
#if __name__ == "__main__":
#    app.run(host="0.0.0.0", debug=True, port = 8080) 


@app.route("/")
def handle_slash():
    requested_name = request.args.get("user_name")
    return render_template("index.html", user_name=requested_name)
    #return requested_name
    #return "Good bye world"

@app.route("/test/", strict_slashes=False)
def handle_test():
    input = "abc"
    return test_module.test(input)

@app.route("/fishing")
def handle_fishing():
    input = "Large Mouth Bass"
    return test_module.test_fishing_in(input)


@app.route("/query", strict_slashes=False)
def handle_query_1():
    query_term = request.args.get("q")
    return jsonify({"query_term": query_term, "search_results": query_on_whoosh.query(query_term)})
    #return jsonify(query_on_whoosh.query(query_term))  
    #search_term = request.args.get("q")
    #return query_on_whoosh.query(search_term,10,1)
    #return query_on_whoosh.query("emperor", 10,1) 
    #return jsonify(query_on_whoosh.query("40k")) 

@app.route("/query", strict_slashes=False)
def handle_query():
    query_term = request.args.get("q")
    query_n = int(request.args.get("p"))
    #return str(query_n)
    return jsonify(query_on_whoosh.query_v2(query_term, query_n))
    #return query_term
    #return jsonify({"query_term": query_term, "search_results": query_on_whoosh.query_v2(query_term, query_n)})

