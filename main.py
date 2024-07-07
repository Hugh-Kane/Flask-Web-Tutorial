from website import create_app
# as website is now a python package - since we have an __init__.py in this folder. 

app = create_app()

if __name__ == '__main__':
    app.run(debug=True)
    # debug=True will update the site everytime a change is saved in code 
    
