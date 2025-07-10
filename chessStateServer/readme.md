# Chess State Server

A high-performance chess state management server built with modern C++.

---

## 🚀 Technologies

- **[Boost](https://www.boost.org/)** - C++ libraries for networking and utilities
- **[NlohmannJson](https://github.com/nlohmann/json)** - Modern JSON library for C++
- **C++** - Core programming language

---

## 📦 Installation

### Step 1: Install Dependencies

Install the required packages using Conan package manager:

```bash
conan install . --build=missing -c tools.system.package_manager:mode=install
```

### Step 2: Build the Project

Navigate to the build directory and configure with CMake:

```bash
cd build
cmake .. -DCMAKE_TOOLCHAIN_FILE="Release/generators/conan_toolchain.cmake" -DCMAKE_BUILD_TYPE=Release
make
```

---

## ▶️ Running the Server

Execute the server from within the build folder:

```bash
./CppServer
```

---

## 📋 Prerequisites

- C++17 compatible compiler
- CMake 3.15 or higher
- Conan package manager

---
