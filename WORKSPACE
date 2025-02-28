workspace(name = "basic_bazel_project")

load("@bazel_tools//tools/build_defs/repo:http.bzl", "http_archive")

# Load Python Rules (rules_python v1.1.0)
http_archive(
    name = "rules_python",
    sha256 = "9c6e26911a79fbf510a8f06d8eedb40f412023cf7fa6d1461def27116bff022c",
    strip_prefix = "rules_python-1.1.0",
    url = "https://github.com/bazelbuild/rules_python/releases/download/1.1.0/rules_python-1.1.0.tar.gz",
)

# Register Python Toolchains
load("@rules_python//python:repositories.bzl", "py_repositories", "python_register_toolchains")
py_repositories()

python_register_toolchains(
    name = "python_3_12_8",
    python_version = "3.12.8",
)

# Install dependencies using pip_parse with requirements_lock
load("@rules_python//python:pip.bzl", "pip_parse")

pip_parse(
    name = "pip_deps",
    requirements_lock = "//:requirements.lock",
)

load("@pip_deps//:requirements.bzl", "install_deps")
install_deps()