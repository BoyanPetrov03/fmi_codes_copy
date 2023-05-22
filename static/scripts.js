console.log("WORKING");

const textarea = document.getElementsByClassName('textarea')
const lineNumbers = document.querySelector('.line-numbers')
const question = document.getElementsByClassName('question')

textarea[0].addEventListener('keyup', event => {
  const numberOfLines = event.target.value.split('\n').length

  lineNumbers.innerHTML = Array(numberOfLines)
    .fill('<span></span>')
    .join('')
})

textarea[0].addEventListener('keydown', event => {
  if (event.key === 'Tab') {
    const start = textarea[0].selectionStart
    const end = textarea[0].selectionEnd

    textarea[0].value = textarea[0].value.substring(0, start) + '\t' + textarea[0].value.substring(end)

    event.preventDefault()
  }
})


const jokers = [
`
#include <iostream>
using namespace std;

int factorial(int n) {
	if (n == 1) {
		return ?;
	}
	return ?;
}

int main() {
	int n;
	cin >> n;
	cout << factorial(n);
}
`,

`#include <iostream>
#include <string>
using namespace std;

int main(){
	string buff;
	getline(cin, buff);

	int i = 0;
	int j = buff.size() - 1;

	while (i ? j) {
		if (buff[i] ? buff[j]) {
			cout << "False";
			return 0;
		}
		
		++i;
		--j;
	}

	cout << "True";
}
`,

]

const questions = [
  `
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
  `,
  `
  <h1>Check if a string is a palindrome</h1>
    <ul>
      <li>I.e., aXa and aXXa are palindromes, whereas aXb and aXYa are not</li>
      <li>Use two pointers approach (see the code template)</li>
    </ul>
  `,

]



var questionsNum = ["0", "1"]

var num = 0;
console.log(num);

function refreshPage(){
  num++;
  console.log(num);
  textarea[0].innerHTML = jokers[num] 
  question[0].innerHTML = questions[num]

  fetch(`${window.origin}/questions`, {
    method: "POST",
    credentials: "include",
    body: JSON.stringify(questionsNum[num]),
    cache: "no-cache",
    headers: new Headers({
      "content-type": "application/json"
    })
  })
} 


textarea[0].innerHTML = jokers[num] 
question[0].innerHTML = questions[num]
    
fetch(`${window.origin}/questions`, {
  method: "POST",
  credentials: "include",
  body: JSON.stringify(questionsNum[num]),
  cache: "no-cache",
  headers: new Headers({
    "content-type": "application/json"
  })
})

