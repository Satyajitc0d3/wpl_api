Steps install and execute

   Steps:
   ------
    pip3/brew install virtualenv
    virtualenv myEnv -p python3
    source myEnv/bin/activate
    pip install flask
    pip install pymysql
    pip freeze - to check env dependencies
    
    either
    -----
    export FLASK_APP=index.py  
    export FLASK_DEBUG=1
    flask run

    or
    ---
    place 
    if __name__=="__main__":
    app.run(debug=True)

    run>> python index.py
