import os
import sys
import shutil
import multiprocessing

def wc(filename):
    try:
        with open(filename, 'r') as f:
            content = f.read()
            lines = content.count('\n')
            words = len(content.split())
            chars = len(content)
        print(f"{lines} {words} {chars} {filename}")
    except FileNotFoundError:
        print(f"wc: {filename}: No such file")

def ls(directory):
    try:
        for item in os.listdir(directory):
            print(item)
    except FileNotFoundError:
        print(f"ls: cannot access '{directory}': No such file or directory")

def cat(filename):
    try:
        with open(filename, 'r') as f:
            print(f.read(), end='')
    except FileNotFoundError:
        print(f"cat: {filename}: No such file")

def pwd():
    print(os.getcwd())

def cp(src, dest):
    try:
        shutil.copy(src, dest)
        print(f"Copied {src} to {dest}")
    except FileNotFoundError:
        print(f"cp: cannot stat '{src}': No such file or directory")

def rm(filename):
    try:
        os.remove(filename)
        print(f"Removed {filename}")
    except FileNotFoundError:
        print(f"rm: cannot remove '{filename}': No such file or directory")

def mkdir(directory):
    try:
        os.makedirs(directory, exist_ok=True)
        print(f"Directory '{directory}' created")
    except Exception as e:
        print(f"mkdir: {e}")

def mv(src, dest):
    try:
        shutil.move(src, dest)
        print(f"Moved {src} to {dest}")
    except FileNotFoundError:
        print(f"mv: cannot stat '{src}': No such file or directory")

def head(filename, n=10):
    try:
        with open(filename, 'r') as f:
            for i, line in enumerate(f):
                if i < n:
                    print(line, end='')
                else:
                    break
    except FileNotFoundError:
        print(f"head: {filename}: No such file")

def tail(filename, n=10):
    try:
        with open(filename, 'r') as f:
            lines = f.readlines()
            for line in lines[-n:]:
                print(line, end='')
    except FileNotFoundError:
        print(f"tail: {filename}: No such file")

def main():
    if len(sys.argv) < 2:
        print("Usage: python linux_commands.py <command> [arguments...]")
        sys.exit(1)

    command = sys.argv[1]
    args = sys.argv[2:]

    commands = {
        'wc': lambda: multiprocessing.Process(target=wc, args=(args[0],)),
        'ls': lambda: multiprocessing.Process(target=ls, args=(args[0] if args else '.',)),
        'cat': lambda: multiprocessing.Process(target=cat, args=(args[0],)),
        'pwd': lambda: multiprocessing.Process(target=pwd),
        'cp': lambda: multiprocessing.Process(target=cp, args=(args[0], args[1])),
        'rm': lambda: multiprocessing.Process(target=rm, args=(args[0],)),
        'mkdir': lambda: multiprocessing.Process(target=mkdir, args=(args[0],)),
        'mv': lambda: multiprocessing.Process(target=mv, args=(args[0], args[1])),
        'head': lambda: multiprocessing.Process(target=head, args=(args[0], int(args[1]) if len(args) > 1 else 10)),
        'tail': lambda: multiprocessing.Process(target=tail, args=(args[0], int(args[1]) if len(args) > 1 else 10)),
    }

    if command in commands:
        process = commands[command]()
        process.start()
        process.join()
    else:
        print(f"Unknown command: {command}")

if __name__ == '__main__':
    main()
