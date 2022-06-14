from lastmile_class import app

def runserver():
    app.run(debug=True, host='0.0.0.0', port=5000)