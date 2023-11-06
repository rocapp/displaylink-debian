import os
import subprocess
import sys


def main():
    pth = os.path.abspath(os.path.dirname(__file__))
    uname = subprocess.check_output(['uname', '-r'], encoding='utf-8').strip()
    pkg_name = f'linux-headers-{uname}'
    fpath = os.path.join(pth, 'resources', 'linux-headers', pkg_name + '.ctl')
    if not os.path.exists(fpath):
        print(f"Path '{fpath}' doesn't exist! Exiting...")
        sys.exit(1)
    with open(fpath, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    pkg_found = False
    deps_found = False
    for i in range(len(lines)):
        line = lines[i].strip()
        if line.startswith('Package: ') and not pkg_found:
            lines[i] = f'Package: {pkg_name}'
            pkg_found = True
        elif '# Depends: ' in line and not deps_found:
            lines[i] = f'Depends: proxmox-headers-{uname}'
            deps_found = True
    with open(fpath, 'w', encoding='utf-8') as f:
        f.write('\n'.join([l for l in lines if l != '']).replace('\n\n', '\n'))
    print(f'...updated {fpath} successfully!')


if __name__ == '__main__':
    main()
