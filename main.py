from website import create_app
# as website is now a python package - since we have an __init__.py in this folder. 

app = create_app()

if __name__ == '__main__':
    #app.run()
    app.run(host='0.0.0.0', port=8080)
    
