In [13]: from scrapli.driver.core import IOSXEDriver

In [14]: class Custom:
    ...:     def send_command(self, command, *args, **kwargs):
    ...:         print(f"My SEND COMMAND {command=}")
    ...:         return super().send_command(command, *args, **kwargs)
    ...:

In [15]: class MyDriver(Custom, IOSXEDriver):
    ...:     pass
    ...:

In [16]: MyDriver.mro()
Out[16]:
[__main__.MyDriver,
 __main__.Custom,
 scrapli.driver.core.cisco_iosxe.sync_driver.IOSXEDriver,
 scrapli.driver.network.sync_driver.NetworkDriver,
 scrapli.driver.generic.sync_driver.GenericDriver,
 scrapli.driver.base.sync_driver.Driver,
 scrapli.driver.base.base_driver.BaseDriver,
 scrapli.driver.generic.base_driver.BaseGenericDriver,
 scrapli.driver.network.base_driver.BaseNetworkDriver,
 object]

In [17]: ssh = MyDriver("192.168.100.1", auth_username="cisco", auth_password="cisco", auth_secondary="cisco")

In [18]: ssh.open()
My SEND COMMAND command='terminal length 0'
My SEND COMMAND command='terminal width 512'

In [19]: ssh.send_command("sh clock")

