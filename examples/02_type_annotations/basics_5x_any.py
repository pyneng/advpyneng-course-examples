
class MyNetmiko(CiscoIosBase):
    def send_command(self, command: str, *args: Any, **kwargs: Any):
        print(command)
        super().send_command(command, *args, **kwargs)

