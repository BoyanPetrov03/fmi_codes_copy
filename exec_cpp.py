from subprocess import Popen, PIPE, STDOUT, check_output
import json
import re


# Just compiles sourcecode passed to it into bin.o
# If result == b'', then it compiled successfully
# Otherwise the error will be there
def compile_code(source: str) -> str:
    p = Popen(["g++", "-g",
                "-std=c++17",
                "-fdiagnostics-parseable-fixits",
                "-Wno-format",
                "-Wfatal-errors",
                "-Wall",
                "-Wextra",
                "-Wfloat-equal",
                "-Wundef",
                "-Wshadow",
                "-Wpointer-arith",
                "-Wcast-align",
                "-Wstrict-overflow=5",
                "-Wwrite-strings",
                "-Wcast-qual",
                "-Wswitch-default",
                "-Wswitch-enum",
                "-Wunreachable-code",
                "-o", 'bin.o',
                "-x", "c++", '-'], stdout=PIPE, stdin=PIPE, stderr=PIPE)

    return p.communicate(input=source.encode("UTF-8"))[1].decode("UTF-8")


def run_compiled(input_data: str) -> (str, str):
    p = Popen(['./bin.o'], stdout=PIPE, stdin=PIPE, stderr=PIPE)
    res, ret_code = p.communicate(input=input_data.encode("UTF-8"))
    return res.decode("UTF-8"), ret_code.decode("UTF-8")


def exec_code(source: str) -> (str, bool):
    # TODO: process the casa when there is an error during comp

    res = compile_code(source)
    if res != '':
        return res, False
    return run_compiled(), True


def test(source: str, expected: str) -> (bool, str):
    output, exit_code = exec_code(source)

    # compilation failed
    if not exit_code:
        return False, output

    return output == expected


s = """
#include <iostream>
using namespace std;

int main() {
    float x = 12;
    float b = 13;
    int a = 0;
    for (int a = 0; a < 10; ++a) {
        
    }
}
"""



