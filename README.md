# plugin-commands

This is a one-cli plugin that allow to create new commands during runtime to the CLI.

## Configuration

```yaml
# one.yaml
required_version: ">= 0.6.5"

plugins:
  commands:
    source: https://github.com/DNXLabs/plugin-commands/archive/master.tar.gz

commands:
- name: install
  command: 'npm install'
  volumes: ['.:/work']
  help: 'npm install'
- name: build
  command: 'npm run build'
  volumes: ['.:/work']
  help: 'npm run build'
- name: start
  volumes: ['.:/work']
  command: 'npm start'
  ports: ['4100:4100']
  help: 'npm start'
  environment: ['TEST': 'test']
```

## Usage

```bash
one install
one build
one start
```

## Parameters

```yaml
- name: <command_name>
  image: <string(docker_image)> # default to
  entrypoint: <string(entrypoint)> # default to None
  volumes: <list(volumes)> # ['.:/work', '.:/app']
  command: <string(command)>
  ports: <list(ports)>  # ['3000:3000', '4100:4100']
  environment: <list(environments)> # ['ENV': 'env']
  help: <string(help)>
```

## Author

Managed by [DNX Solutions](https://github.com/DNXLabs).

## License

Apache 2 Licensed. See [LICENSE](https://github.com/DNXLabs/plugin-dnx-assume/blob/master/LICENSE) for full details.