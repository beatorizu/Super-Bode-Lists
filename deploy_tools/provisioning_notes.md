# Provisionamento de um novo site

## Pacotes necessários:

* nginx
* Python 3.6
* virtualenv + pip
* Git

Por exemplo, no Ubuntu:

```bash
sudo add-apt-repository ppa:jonathonf/python-3.6 && sudo apt-get update
sudo apt-get install nginx git python3.6 python3.6-env
```

## Config do Nginx Virtual Host

* veja nginx.template.conf
* substitua SITENAME, por exemplo, por, staging.my-domain.com

## Serviço Systemd

* veja gunicorn-systemd.template.service
* substitua SITENAME, por exemplo, por, staging.my-domain.com

## Estrutura de pastas

Suponha que temos uma conta de usuário em /home/username

```bash
/home/username
└── sites
    └── SITENAME
        ├── database
        ├── source
        ├── static
        └── virtualenv
```
