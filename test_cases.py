import exec_cpp
import random


def random_str():
    printable = " !#$%&()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\\]^_`abcdefghijklmnopqrstuvwxyz{|}~"
    out = ""
    for _ in range(random.randint(1, 50)):
        out += random.choice(printable)

    return out

# if it's ok, then returns (True, "")
# if there's difference, then returns (False, "message")
def test_factorial(source: str) -> (bool, str):
    res = exec_cpp.compile_code(source)
    if res != '':
        return False, res

    fact = 1
    for i in range(1, 13):
        fact *= i
        res, ret_code = exec_cpp.run_compiled(str(i))

        if ret_code != '':
            return False, ret_code

        if res != str(fact):
            return False, "{}! = {}, not {}".format(i, fact, res)

    return True, ""


    # if we are here, then compilation finished successfully

def test_rot13(source: str) -> (bool, str):
    res = exec_cpp.compile_code(source)
    if res != '':
        return False, res

    def rot13(s: str):
        rtr = str.maketrans(
            'ABCDEFGHIJKLMabcdefghijklmNOPQRSTUVWXYZnopqrstuvwxyz',
            'NOPQRSTUVWXYZnopqrstuvwxyzABCDEFGHIJKLMabcdefghijklm')
        return s.translate(rtr)

    for _ in range(100):
        ts = random_str()
        rs = rot13(ts)

        res, ret_code = exec_cpp.run_compiled(ts)

        if ret_code != '':
            return False, ret_code

        if res != rs:
            return False, "\"{}\" -ROT13-> \"{}\" and not \"{}\"".format(ts, rs, res)


    return True, ""


def test_palindrome(source: str) -> (bool, str):
    res = exec_cpp.compile_code(source)
    if res != '':
        return False, res

    def is_pal(s: str):
        i = 0
        j = len(s) - 1
        while i < j:
            if s[i] != s[j]:
                return False

            i += 1
            j -= 1

        return True

    for _ in range(100):
        s = random_str()
        if not is_pal(s):
            if random.choice([0, 1]) == 0:
                s = s + s[::-1]

        res, ret_code = exec_cpp.run_compiled(s)

        if ret_code != '':
            return False, ret_code

        if res != str(is_pal(s)):
            return False, "Incorrectly classified string \"{}\"".format(s)

    return True, ""


# print(test_palindrome("""
# #include <iostream>
# using namespace std;
#
# int main() {
#     string buff;
#     getline(cin, buff);
#
#     int i = 0;
#     int j = buff.size() - 1;
#
#     while (i < j) {
#         if (buff[i] != buff[j]) {
#             cout << "False";
#             return 0;
#         }
#         ++i;
#         --j;
#     }
#
#     cout << "True";
#     return 0;
# }
#
# """))

#
# print(test_palindrome("""
# #include <iostream>
# #include <string>

# using namespace std;

# void rot13(string &s) {
#     for (char &c : s) {
#         if ('a' <= c && c <= 'z') {
#             int diff = (c - 'a') + 13;
#             c = static_cast<char>(static_cast<int>('a') + (diff % 26));
#         } else if ('A' <= c && c <= 'Z') {
#             int diff = (c - 'A') + 13;
#             c = static_cast<char>(static_cast<int>('A') + (diff % 26));
#         }
#     }
# }
#
# int main() {
#     string buff;
#     getline(cin, buff);
#     rot13(buff);
#     cout << buff;
#     return 0;
# }
# """))

# print(test_rot13("""
# #include <iostream>
# #include <string>

# using namespace std;

# void rot13(string &s) {
#     for (char &c : s) {
#         if ('a' <= c && c <= 'z') {
#             int diff = (c - 'a') + 13;
#             c = static_cast<char>(static_cast<int>('a') + (diff % 26));
#         } else if ('A' <= c && c <= 'Z') {
#             int diff = (c - 'A') + 13;
#             c = static_cast<char>(static_cast<int>('A') + (diff % 26));
#         }
#     }
# }
#
# int main() {
#     string buff;
#     getline(cin, buff);
#     rot13(buff);
#     cout << buff;
#     return 0;
# }
# """))

# print(test_factorial("""
# #include <iostream>

# using namespace std;

# int factorial(int n) {
#     if (n == 0) {
#         return 1;
#     }
#     return n * factorial(n-1);
# }

# int main() {
#     int n;
#     cin >> n;
#     cout << factorial(n);
#     return 0;
# }
# """))

test_rot13("")