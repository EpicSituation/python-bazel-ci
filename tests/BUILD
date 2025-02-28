# Define a test for math_utils
load("@rules_python//python:defs.bzl", "py_test")

py_test(
    name = "test_math_utils",
    srcs = ["test_math_utils.py"],
    deps = [
        "//src:math_utils_lib",
         "@pip_deps//pytest",
    ],

)

# Define a test for string_utils
py_test(
    name = "test_string_utils",
    srcs = ["test_string_utils.py"],
    deps = [
        "//src:string_utils_lib",
    ],
)
