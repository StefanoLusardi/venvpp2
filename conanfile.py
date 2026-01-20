from conan import ConanFile
from conan.tools.cmake import CMake, CMakeToolchain, CMakeDeps, cmake_layout

PACKAGES = [
    "spdlog/1.17.0"
]

class ProjectRecipe(ConanFile):
    name = "choc_example"
    version = "1.0.0"
    description = "My project recipe"
    license = "MIT"
    settings = "os", "compiler", "build_type", "arch"

    def requirements(self):
        for package in PACKAGES:
            self.requires(package)

    def layout(self):
        cmake_layout(self)
        self.folders.generators = "build/generators"

    def generate(self):
        deps = CMakeDeps(self)
        deps.generate()

        tc = CMakeToolchain(self)
        tc.generator = "Ninja"

        if self.settings.os == "Linux":
            if self.settings.compiler == "gcc":
                tc.variables["CMAKE_CXX_COMPILER"] = f"g++-{self.settings.compiler.version}"
                tc.variables["CMAKE_C_COMPILER"] = f"gcc-{self.settings.compiler.version}"
            elif self.settings.compiler == "clang":
                tc.variables["CMAKE_CXX_COMPILER"] = f"clang++-{self.settings.compiler.version}"
                tc.variables["CMAKE_C_COMPILER"] = f"clang-{self.settings.compiler.version}"

        elif self.settings.os == "Macos":
            tc.variables["CMAKE_CXX_COMPILER"] = "clang++"
            tc.variables["CMAKE_C_COMPILER"] = "clang"

        elif self.settings.os == "Windows" and self.settings.compiler == "msvc":
            pass

        tc.generate()

    def build(self):
        cmake = CMake(self)
        cmake.configure()
        cmake.build()

    def package(self):
        cmake = CMake(self)
        cmake.install()
