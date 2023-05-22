from flask import Flask, redirect, url_for, request, render_template
import exec_cpp
import test_cases
import random
import json

app = Flask(__name__,)

questions = [
  """
  <h1>Calculate n factorial recursively</h1>
  <ul>
    <li>Suppose you know that 5! = 120, could you derive what 6! is?</li>
      <ul>
        <details>
          <summary>Solution</summary>
          <li><p>n! = 1.2.3..n =&gt; n! = (n-1)! . n =&gt; 6! = 5!(6) = 120(6) = 720</p>

          <li>
            <p>So, basically, we use the divide and conquer approach. We know that 1! = 1 and we know how to compute the next term (n+1)! = n!(n+1), so, we know how to find nth term in general</p>
          </li>
        </details>
        </li>
      </ul>

  </ul>
  """,
  """
  <h1>Check if a string is a palindrome</h1>
    <ul>
      <li>I.e., aXa and aXXa are palindromes, whereas aXb and aXYa are not</li>
      <li>Use two pointers approach (see the code template)</li>
    </ul>
  """
]





@app.route('/questions', methods = ['POST'])
def data():
   if request.method == 'POST':
      global question
      question = request.get_json()
   return question

@app.route('/',methods = ['POST', 'GET'])
def home():
   if request.method == 'POST':
      user = request.form['solution']
      if(question == "0"):
         if(test_cases.test_factorial(user)[0] == True):
            answer = '<p style="color: green; text-align: left;">' + 'Success' + '</p>'
         if(test_cases.test_factorial(user)[0] == False):
            answer = '<p style="color: red; text-align: left;">' + test_cases.test_factorial(user)[1] + '</p>'
      if(question == "1"):
         if(test_cases.test_palindrome(user)[0] == True):
            answer = '<p style="color: green; text-align: left;">' + 'Success' + '</p>'
         if(test_cases.test_palindrome(user)[0] == False):
            answer = '<p style="color: red; text-align: left;">' + test_cases.test_palindrome(user)[1] + '</p>'
      return render_template("solution.html", results=answer, code=user, question=questions[int(question)])
   if request.method == 'GET':
      return render_template("index.html")

   


if __name__ == '__main__':
   app.run(debug = True)