from pprint import pprint
import asyncio
import asyncssh


async def send_show(device, show):
    host = device["host"]
    print(f"Подключаюсь к {host}")
    async with asyncssh.connect(**device) as ssh:
        writer, reader, _ = await ssh.open_session()
        # stdin, stdout, stderr = await ssh.open_session()
        await reader.readuntil(">")
        writer.write("enable\n")
        await reader.readuntil("Password")
        writer.write("cisco\n")
        await reader.readuntil("#")
        writer.write("terminal length 0\n")
        await reader.readuntil("#")
        print(f"Отправляю команду {show} на {host}")
        writer.write(f"{show}\n")
        output = await reader.readuntil("#")
        print(f"Получили результат от {host}")
    return output


async def send_command_to_devices(devices, show):
    dev_output_dict = {}
    coroutines = [send_show(dev, show) for dev in devices]
    results = await asyncio.gather(*coroutines, return_exceptions=True)
    for dev, output in zip(devices, results):
        dev_output_dict[dev["host"]] = output
    return dev_output_dict


if __name__ == "__main__":
    params = {"username": "cisco", "password": "cisco", "connect_timeout": 5}
    hosts = ["192.168.139.1", "192.168.139.2", "192.168.139.3"]
    devices = [{"host": ip, **params} for ip in hosts]

    result_dict = asyncio.run(send_command_to_devices(devices, "sh ip int br"))
    pprint(result_dict, width=120)

