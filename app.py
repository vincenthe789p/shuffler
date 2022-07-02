
# Importing flask module in the project is mandatory
# An object of Flask class is our WSGI application.
from flask import Flask
import secrets
 


def shuffle():
    index_list = []
    for i in range(52, 0, -1):
        index_list.append(secrets.randbelow(i) + 1)
    return index_list

def find_group_index(index, group_counts):
    group = 1
    while True:
        if index <= group_counts[group]:
            return (group, index)
        index -= group_counts[group]
        group += 1

def generate_deck():
    index_list = shuffle()
    group_counts = [0, 13, 13, 13, 13]

    group_index_list = []
    for i in index_list:
        group, index = find_group_index(i, group_counts)
        group_counts[group] -= 1
        group_index_list.append((group, index))
    return group_index_list




# Flask constructor takes the name of
# current module (__name__) as argument.
app = Flask(__name__)
 
# The route() function of the Flask class is a decorator,
# which tells the application which URL should call
# the associated function.
@app.route('/')
# ‘/’ URL is bound with hello_world() function.
def hello_world():
    indexes = generate_deck()
    output = ""
    for group, index in indexes:
        output += f"<tr><td>{group}</td><td>{index}</td></tr>"
    myString = f"""<!DOCTYPE html>
    <html>
        <head>
        <meta charset="utf-8">
<meta name="viewport" 
content="width=device-width, initial-scale=1">
<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.2.0-beta1/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-0evHe/X+R7YkIZDRvuzKMRqM+OrBnVFBL6DOitfPri4tjfHxaWutUpFmBp4vmVor" crossorigin="anonymous">
        </head>
        <body id="body1">
<button id="button1" onclick="change();" type="button" class="btn btn-primary">Toggle</button>
            <table class="table table-striped table-light" id="table1">
             <tr> <th>group</th> <th>index</th>{output} </table>
        
        </body>
        <script>
        let change = () => {{
            document.getElementById('table1').classList.toggle('table-dark');
            document.getElementById('body1').classList.toggle('bg-dark');


            
        }}
        </script>
    </html>
    """
    return myString
 
# main driver function
if __name__ == '__main__':
 
    # run() method of Flask class runs the application
    # on the local development server.
    app.run(host="0.0.0.0")





