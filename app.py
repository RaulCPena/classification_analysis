from flask import Flask, request, render_template
import pickle
# import trims 
import pandas as pd

app = Flask(__name__)

numColumns = 3

loaded_model = pickle.load(open("./Models/model_xgb_over.sav", "rb"))


@app.route('/',methods=["GET","POST"])
def home():
    message = "Welcome to my flask based web application ... !!!"
    return render_template("home.html", message = message)


@app.route('/getXGBoost',methods=["GET","POST"])
def getXGBoost():
    CurrentInterestRate = request.form["Current Interest Rate"]
    OriginalUPB = request.form["Original UPB"]
    OriginalLoanTerm = request.form["Original Loan Term"]
    LoanAge = request.form["Loan Age"]
    OriginalLoantoValueRatioLTV = request.form["Original Loan to Value Ratio (LTV)"]
    NumberofBorrowers = request.form["Number of Borrowers"]
    DebtToIncomeDTI = request.form["Debt-To-Income (DTI)"]
    FirstTimeHomeBuyerIndicator = request.form["First Time Home Buyer Indicator"]
    ModificationFlag = request.form["Modification Flag"]
    HomeReadyProgramIndicator = request.form["Home Ready Program Indicator"]
    HighBalanceLoanIndicator = request.form['High Balance Loan Indicator']
    MinimumCreditScore = request.form["Minimum Credit Score"]

    inputList = [CurrentInterestRate,
                OriginalUPB,
                OriginalLoanTerm,
                LoanAge,
                OriginalLoantoValueRatioLTV,
                NumberofBorrowers,
                DebtToIncomeDTI,
                FirstTimeHomeBuyerIndicator,
                ModificationFlag,
                HomeReadyProgramIndicator,
                HighBalanceLoanIndicator,
                MinimumCreditScore]
    
    cols= ['Current Interest Rate', 'Original UPB', 'Original Loan Term', 'Loan Age',
    'Original Loan to Value Ratio (LTV)','Number of Borrowers', 
    'Debt-To-Income (DTI)', 'First Time Home Buyer Indicator', 'Modification Flag', 
    'Home Ready Program Indicator', 'High Balance Loan Indicator', 'Minimum Credit Score']
    
    y_pred_from_pkl = loaded_model.predict(pd.DataFrame([inputList], columns = cols))
    print(y_pred_from_pkl)
    pred_res = ""
    if y_pred_from_pkl[0] == 0:
        return "Will Not Default"
    else:
        return "Will Default"
        

if __name__ == '__main__':
    app.run(debug=True)