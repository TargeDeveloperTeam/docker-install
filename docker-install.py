import subprocess
import os

def install_docker():
    print("Docker kurulumu başlatılıyor...")
    subprocess.run(['curl', '-fsSL', 'https://get.docker.com', '-o', 'get-docker.sh'])
    subprocess.run(['sh', 'get-docker.sh'])
    subprocess.run(['rm', 'get-docker.sh'])
    print("Docker kurulumu tamamlandı.")

def install_specific_docker_compose(version):
    print(f"Docker Compose v{version} kurulumu başlatılıyor...")
    compose_url = f"https://github.com/docker/compose/releases/download/v{version}/docker-compose-$(uname -s)-$(uname -m)"
    subprocess.run(['curl', '-L', compose_url, '-o', '/usr/local/bin/docker-compose'])
    subprocess.run(['chmod', '+x', '/usr/local/bin/docker-compose'])
    print(f"Docker Compose v{version} kurulumu tamamlandı.")

def main():
    # Docker'ın kurulu olup olmadığını kontrol et
    if subprocess.run(['which', 'docker']).returncode != 0:
        install_docker()
    else:
        print("Docker zaten kurulu.")
    
    # Docker Compose'ın belirtilen versiyonunu kur
    install_specific_docker_compose('2.18.1')

    # Docker ve Docker Compose versiyonlarını kontrol et
    print("Kurulum sonrası versiyon kontrolü:")
    subprocess.run(['docker', '--version'])
    subprocess.run(['docker-compose', '--version'])

if __name__ == '__main__':
    if os.geteuid() == 0:
        main()
    else:
        print("Bu betik root yetkileri ile çalıştırılmalıdır. Lütfen sudo kullanın.")
