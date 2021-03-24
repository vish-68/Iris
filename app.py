#!/usr/bin/env python
# coding: utf-8

# In[1]:


#importing libraries:
import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle

# In[2]:


app=Flask(__name__)


# In[3]:


model=pickle.load(open('iris_model.pkl','rb'))


# In[4]:


@app.route('/')
def home():
    return render_template('iris.html')


# In[5]:


@app.route("/Iris", methods=['POST'])
def Iris():
    data1=request.form["sepal_length"]
    data2=request.form["sepal_width"]
    data3=request.form["petal_length"]
    data4=request.form["petal_width"]
    arr=np.array([[data1,data2,data3,data4]])
    pred=model.predict(arr)
    
    #create original output dict
    output_dict= dict()
    output_dict['Sepal Length']=data1
    output_dict['Sepal Width']=data2
    output_dict['Petal Length']=data3
    output_dict['Petal Width']=data4
    
    return render_template('result.html',original_input=output_dict,data=pred)
# In[7]:


if __name__=='__main__':
    app.run(debug=True)


# In[ ]:






# In[ ]:




