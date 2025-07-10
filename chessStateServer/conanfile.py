from conan import ConanFile
from conan.tools.cmake import CMake, CMakeDeps, CMakeToolchain, cmake_layout

class chessStateServer(ConanFile):
    settings = 'os', 'compiler', 'build_type', 'arch'

    def requirements(self):
        self.requires("boost/1.88.0")
        self.requires("nlohmann_json/3.12.0")

    def generate(self):
        deps = CMakeDeps(self)
        deps.generate()
        tc = CMakeToolchain(self)
        tc.generate()

    def layout(self):
        cmake_layout(self)

    def build(self):
        cmake = CMake(self)
        cmake.configure()
        cmake.build()