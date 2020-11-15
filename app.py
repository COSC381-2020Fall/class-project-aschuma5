from flask import Flask, render_template, request, jsonify
import test_module
import config
import query_on_whoosh
import smtplib
import math
import sqlite3





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

"""
@app.route("/query", strict_slashes=False)
def handle_query_1():
    query_term = request.args.get("q")
    return jsonify({"query_term": query_term, "search_results": query_on_whoosh.query(query_term)})
    #return jsonify(query_on_whoosh.query(query_term))  
    #search_term = request.args.get("q")
    #return query_on_whoosh.query(search_term,10,1)
    #return query_on_whoosh.query("emperor", 10,1) 
    #return jsonify(query_on_whoosh.query("40k")) 
"""
"""
@app.route("/query", strict_slashes=False)
def handle_query():
    query_term = request.args.get("q")
    query_n = int(request.args.get("p"))
    #return str(query_n)
    return jsonify(query_on_whoosh.query_v2(query_term, query_n))
    #return query_term
    #return jsonify({"query_term": query_term, "search_results": query_on_whoosh.query_v2(query_term, query_n)})
"""
@app.route("/query", strict_slashes=False)
def handle_query():
    query_term = request.args.get("q")
    page_index = int(request.args.get("p"))
    return jsonify({"query_term": query_term, "search_results": query_on_whoosh.query(query_term, current_page=page_index)})

@app.route("/query_view", strict_slashes=False)
def handle_query_view():
    query_term = request.args.get("q")
    if not query_term:

        query_term = ""
    #page_index = int(request.args.get("p"))
    try:
        page_index = int(request.args.get("p"))
    except:
        page_index = 1

    conn = sqlite3.connect('history.db')
    c = conn.cursor()
    #INSERT INTO search_terms (id, term, search_time) VALUES (1, 
    #3.131.112.93:5000/query_view?q=marine',strftime('%s', 'now'));delete from search_terms;insert into search_terms (id, term, search_time) values (1, 'garbage
    #, strftime('%s', 'now'))"
    #http://3.131.112.93:5000/query_view?q=mars%27,%20strftime(%27%s%27,%20%27now%27));delete%20from%20search_terms;insert%20into%20search_terms%20(id,%20term,%20search_time)%20values%20(1,%20%27garbage
    #c.executescript(f"INSERT INTO search_terms (id, term, search_time) VALUES (1, '{query_term}', strftime('%s', 'now'));")
    #c.execute("INSERT INTO search_terms (id, term, search_time) VALUES (?, ?, strftime('%s', 'now'));", (1, query_term))
    c.execute("INSERT INTO search_terms(term, search_time) VALUES (?, strftime('%s', 'now'));", [query_term])
    c.execute("SELECT * FROM search_terms;")
    rows = c.fetchall()
    conn.commit()
    conn.close()
    query_results = query_on_whoosh.query(query_term, current_page=page_index)
    search_results = query_results[0]
    results_cnt = int(query_results[1])
    page_cnt = math.ceil(results_cnt / 10 )


    return render_template("query.html", 
                            results = search_results, 
                            page_cnt=page_cnt,
                            query_term=query_term,
                            history_list=rows)
    '''
    return render_template("query.html", 
                            results = search_results, 
                            page_cnt=page_cnt,
                            query_term=query_term)
    '''
@app.route("/about", strict_slashes=False)
def handle_about():
    return render_template("about.html")

@app.route("/success", strict_slashes=False)
def handle_request():
    new_data = request.args.get("new_data")
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    #server.login("aschuma5@emich.edu", config.gmail_password )
    server.login("aschuma5@emich.edu", config.gmail_password )
    #message = 'Subject: {}\n\n'.format('Request to add new data', 'request to add: ' + new_data)
    message = "request to add -- > " + new_data
    server.sendmail("aschuma5@emich.edu", "aschuma5@emich.edu", message)
    return render_template("success.html", new_data=new_data)

    server.sendmail("aschuma5@emich.edu", "aschuma5@emich.edu", "request " + new_data)
    return render_template("success.html", new_data=new_data)
