from flask import Flask, render_template, request,url_for
from Contacts import Contacts

from Model import DB
from Controller import Controller


###### CREATING FLASK INSTANCE
app = Flask(__name__)

####  INDEX PAGE  ROUTE   
@app.route('/')
def main_page():
    return render_template('index.html')

#####################################################
#### create contact form  page  route
@app.route('/createForm')
def createForm():
    return render_template('createForm.html')



####    POST REQUEST AFTER SUBMITTING THE FORM
@app.route('/create', methods =  ['POST'])
def submitForm():
    obj = Controller()   
    name = request.form['name']
    #########       validating username
    tupl=obj.validateUsername(name) 
    if(tupl[0]==False):
        return render_template('createForm.html',msg = tupl[1])  
    mobile_no = request.form['mobile_no']
    
    #######   validating  mobile Number
    status = obj.validate_mobile_no(mobile_no)
    if(status[0]==False):
        return render_template('createForm.html',msg = status[1])

    
    city = request.form['city']
    profession = request.form['profession']
    contact = Contacts(name,mobile_no,city,profession)
    obj.insert_contact(contact)
    return render_template('index.html', msg = 'Contact successfully created')


#####################################################
#### show  List of contacts

@app.route('/contacts')
def showCourses():
    
    obj = Controller()
    list = obj.get_Courses()
    return render_template('showContacts.html',data=  list)





#####################################################
#### Search Contact BY  name

@app.route('/searchForm')
def search_contact_by_name():
    return render_template('searchForm.html')


########## HANDLE THE POST REQUEST FOR  THE SEARCH _ BY  NAME FUNCTION
@app.route('/search',methods=['POST'])
def show_Search_BY_Name_Results():
    
    name = request.form['name']
    obj = Controller()
    status  = obj.show_Search_BY_Name_Results(name)
    if(status==None):
        return render_template('searchForm.html', msg = 'No User found with this name ')
    else :
        return render_template('show_individual_contact.html',contact=status)





app.run(debug=True)


