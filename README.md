# venvpp2
Welcome to venvpp2!

// TODO
// Descrivi cosa fa il progetto e perchè dovresti usarlo per il tuo progetto C++ moderno.

This project is an evolution of my previous [venvpp](https://github.com/TeiaCare/venvpp).

The main enhancements with respect to its predecessor are:
[Conan v2](https://conan.io/) and [CMake v4](https://cmake.org/) with the usage of *CMakePresets* as first class citizens replacing the older custom Python scripts to addressing Configure, Build, Install, Test and Package the project.

---

## Getting started
In order to spin up a fresh C++ development environment in your local repository just run the following command:

### Setup Virtual Environment

```bash
# MacOS/Linux
scripts/env/setup.sh
source .venv/bin/activate

# Windows
scripts/env/setup.bat
.venv\Scripts\activate.bat
```

## Install Conan packages
```bash
# Install packages and create CMakePresets.json + CMake toolchain file
conan install . -b=missing -pr:a=profiles/linux-clang -s build_type=Debug
```

## Configure, Build and Install
```bash
# CMake configure
cmake --preset conan-debug

# CMake build
cmake --build build/Debug

# CMake install
cmake --install build/Debug

# Run
install/venvpp2_example
```

// TODO
// Rimuovere?

## Lockfile (Dipendenze Fissate)
```bash
# Crea lockfile
conan lock create .

# Installa usando lockfile
conan install . --lockfile=conan.lock --output-folder=build/Release
```
