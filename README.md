
# Iris

As we know that their are different kinds of species in Iris 
flower like Setosa, Virginica and Versicolour. We recognised all 
of them by some parameters like Petal length, Petal width, 
Sepal length & Sepal width. After giving al this input we will get 
output.
## Data Analysis

In Iris dataset we are provided 5 features(including target 
variable)
* Petal Length
* Petal Width
* Sepal Length
* Sepal Width
All the independent features are contains continous numerical 
values & dependent variable is contains categorical numerical 
value like Setosa=0, Versicolour=1, Virginica=2.
  
## Approach

Our Main goal is to know that whether which species 
it belong to Setosa, Versicolour or Virginica.

* Data Exploration : Exploring dataset using pandas,numpy,matplotlib and seaborn.
* Data visualization : Ploted graphs to get insights about dependend and independed variables.
* Model Selection I : Tested all base models to check the base accuracy. Also ploted and calculate Performance Metrics to check whether a model is a good fit or not.
* Pickle File : Selected model as per best accuracy and created pickle file using pickle library.
* Webpage & deployment : Created a webform that takes all the necessary inputs from user and shows output. After that I have deployed project on Herokuapp 
## Technologies Used

* Jupyter notebook, Spyder, VScode Is Used For IDE.
* For Visualization Of The Plots Matplotlib , Seaborn Are Used.
* Herokuapp is Used For Model Deployment.
* Front End Deployment Is Done Using HTML, CSS, Bootstrap.
* Flask is for creating the application server and pages.
* Git Hub Is Used As A Version Control System.
* os is used for creating and deleting folders.
* csv is used for creating .csv format file.
* numpy is for arrays computations and mathematical operations
* pandas is for Manipulation and wrangling structured data
* scikit-learn is used for machine learning tool kit
* pickle is used for saving model
* SVM is used for SVC(Support Vector Classifier) Implementation.
* Decision Tree is used for DecisionTreeClassifier Implementation.
* Extras Trees is used for ExtraTreesClassifier Implementation.
* Random Forest is used for RandomForestClassifier Implementation.
  
## Deployment

**Herokuapp Link:** https://iris-prediction-webapp.herokuapp.com/
  
## Deployment

To Clone this project run

```bash
git clone https://github.com/vish-68/Iris
```
Go to Project directory
```bash
cd Iris
```
Install dependencies
``` bash
pip install -r requirements.txt
```  
Run the app.py
```bash
python app.py
```
## Conclusion
We have developed Iris Predictive model which is capable for
predicting types of Iris whether it is Setosa or Viginica or
Vesicolour. After importing dataset we have to handle missing
, but in this case misssing values are absent. So move further
for data visualization. We have done boxplot for checking outliers
and here also outliers were absent. As we have plot linear plot 
so we conclude that class 0 i.e. Setosa has small Petal length, 
Petal width, Sepal length & Sepal width. After that we have build
for model SVC, Decision Tree, ExtraTree, Random Forest.
Out of all RandomforestClassifier is working great so we have use 
RandomforestClassifier for Model deployment. After deployment we
we have to give all four input and you will get the output that
whether it is Setosa, Versicolour, Virginica.