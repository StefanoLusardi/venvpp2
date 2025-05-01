import argparse
import subprocess
import sys
import os

def check_env():
    if not os.getenv('VIRTUAL_ENV'):
        raise SystemError("\n========================================================"
                          "\nYou are not running inside a python virtual environment"
                          "\nConfigure and activate it as shown in the project README"
                          "\n========================================================\n")
    if not os.getenv('CONAN_HOME'):
        raise SystemError("\n========================================================"
                          "\nConan home is not properly configured"
                          "\nMake sure to run the env/setup.sh|bat script first"
                          "\n========================================================\n")
    
    print("CONAN_HOME:", os.getenv('CONAN_HOME'))

def parse():
    parser = argparse.ArgumentParser(formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument("build_type", help="Debug or Release", choices=['Debug', 'Release', 'RelWithDebInfo'])
    parser.add_argument("compiler", help="Compiler name", choices=['gcc', 'clang', 'visual_studio'])
    parser.add_argument("compiler_version", help="Compiler version")
    parser.add_argument("-d", "--directories", help="Specific conanfiles directories", nargs='*', required=False)
    return parser.parse_args()

def profile(profile_name):
    subprocess.run([
        'conan', 'config', 'install',
        profile_name, f'--target-folder={os.getenv('CONAN_HOME')}/profiles'

    ], check=True)

def install(profile_name, build_type):
    subprocess.run([
        'conan', 'install', '.', 
        f'--settings', f'build_type={build_type}',
        '--profile:all', profile_name,
        '--build', 'missing'
    ], check=True)

def main():
    check_env()
    args = parse()
    profile_name = f'profile_{args.compiler+args.compiler_version}'
    profile(profile_name)
    install(profile_name, args.build_type)

if __name__ == '__main__':
    sys.exit(main())
