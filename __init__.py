import click
import yaml
import os
import json
from os import path
from one.__init__ import CONFIG_FILE
from one.docker.container import Container
from one.docker.image import Image
from one.utils.environment.aws import EnvironmentAws
from one.utils.config import get_config_value
from one.one import cli


container = Container()
image = Image()
environment = EnvironmentAws()
SHELL_IMAGE = image.get_image('shell')


def make_callback(image, command, ports, entrypoint, volumes, environment):
    def callback():
        container.create(
            image=image,
            command=command,
            ports=ports,
            entrypoint=entrypoint,
            volumes=volumes,
            environment=environment
        )
    return callback


def __init__():
    if not path.exists('.one'):
        os.mkdir('.one')
    commands = []

    try:
        with open(CONFIG_FILE) as file:
            docs = yaml.load(file, Loader=yaml.FullLoader)

        envs = environment.build().get_env()

        for cmd in docs['commands']:
            func = make_callback(
                image = cmd.get('image', SHELL_IMAGE),
                command = cmd.get('command', None),
                ports = cmd.get('ports', []),
                entrypoint = cmd.get('entrypoint', None),
                volumes = cmd.get('volumes', []),
                environment = envs
            )

            command = click.Command(
                name = list(cmd.keys())[0],
                help = cmd.get('help', ''),
                callback = func
            )

            cli.add_command(command)
    except KeyError:
        pass
    except TypeError:
        pass
    except AttributeError:
        click.echo(
            click.style('WARN ', fg='yellow') +
            'Commands block declared but empty.\n'
        )
    except Exception:
        pass