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
    int_features=[float(x) for x in request.form.values()]
    final_features=[np.array(int_features)]
    prediction=model.predict(final_features)
       
    if prediction==0:
        output="Iris-Setosa"
    elif prediction==1:
        output="Iris-Versicolour"
    else:
        output="Iris-Virginica"
    return render_template('iris.html',prediction_text="{}".format(output))

# In[7]:


if __name__=='__main__':
    app.run(debug=True)


# In[ ]:






# In[ ]:




