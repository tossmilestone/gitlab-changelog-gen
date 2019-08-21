import yaml

class Config(object):
    CONFIG_FILE="./.chg-gen.config"

    def __init__(self, host, group, project, private_token):
        self.host = host
        self.group = group
        self.project = project
        self.private_token = private_token

    @staticmethod
    def from_prompt():
        host = input("Gitlab host: ")
        group = input("Gitlab group: ")
        project = input("Gitlab project: ")
        private_token = input("Gitlab private token: ")
        return Config(host, group, project, private_token)

    @classmethod
    def load(cls):
        try:
            with open(cls.CONFIG_FILE, "r") as f:
                cfg_yaml = yaml.load(f, Loader=yaml.SafeLoader)
                return Config(
                    cfg_yaml['host'],
                    cfg_yaml['group'],
                    cfg_yaml['project'],
                    cfg_yaml['private_token']
                )
        except FileNotFoundError:
            print("Config file '%s' not found, please run 'init' command first." % cls.CONFIG_FILE)
            exit(-1)
        except yaml.YAMLError as exc:
            print("Parse config file error: %s" % exc)
            exit(-1)
        except KeyError as exc:
            print("Config file key error: %s" % exc)
            exit(-1)

    def save(self):
        try:
            with open(self.CONFIG_FILE, "x") as f:
                yaml.dump(
                    dict(host=self.host,
                        group=self.group,
                        project=self.project,
                        private_token=self.private_token), stream=f)
        except Exception as exc:
            print("Save config to '%s' error: %s" % (self.CONFIG_FILE, exc))
            exit(-1)
