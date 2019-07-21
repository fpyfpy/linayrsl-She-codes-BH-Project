from flask import Flask, request, jsonify
from _datetime import datetime


app = Flask(__name__)

my_tree = [{"ID": "1", "firstName": "Sonya", "lastName": "Beyo"}]


@app.route('/query_example')
def query_example():
    language = request.args.get('language')

    framework = request.args['framework']
    website = request.args.get('website')
    return '''<h1>
            The language is: {}.
            The framework is: {}.
            The website is: {}</h1>'''.format(language, framework, website)


@app.route('/form_example', methods=['POST', 'GET'])
def form_example():
    if request.method == 'POST':
        language = request.form.get('language')
        framework = request.form['framework']
        return '''<h1>
                The language is: {}.
                The framework is: {}.'''.format(language, framework)
    return '''<form method = "POST">
    Language<input type="text" name="language">
    Framework<input type="text" name="framework">
    <input type="submit"></form>'''


@app.route('/json_example', methods=['GET', 'POST'])
def json_example():
    req_data = request.get_json()
    now = datetime.now()
    year = now.year
    time = now.strftime("%H:%M:%S")
    day = now.day
    month = now.strftime('%b')
    date = '{} {} {}'.format(day, month.upper(), year)
    my_id = req_data['ID']
    first_name = req_data['firstName']
    last_name = req_data['lastName']

    my_gedcom = '''
    1 DATE {}\n
    2 TIME {}\n
    1 FILE base.ged.tmp\n
    1 GEDC\n
    2 VERS 5.5\n
    2 FORM LINEAGE-LINKED\n
    1 CHAR ASCII\n
    0 @{}@ INDI\n
    1 NAME {} /{}\n
    1 OBJE\n
    2 FILE'''.format(date, time, my_id, first_name, last_name)

    return my_gedcom


if __name__ == '__main__':
    app.run(debug=True, port=5000)
