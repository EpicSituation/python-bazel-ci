load("@bazel_tools//tools/build_defs/repo:http.bzl", "http_archive")

# Load rules_python for Python package management
http_archive(
    name = "rules_python",
    url = "https://github.com/bazelbuild/rules_python/releases/download/0.25.0/rules_python-0.25.0.tar.gz",
    strip_prefix = "rules_python-0.25.0",
)

load("@rules_python//python:pip.bzl", "pip_install")

pip_install(
    name = "python_deps",
    requirements = "@//:requirements.txt",
)
