import asyncio
from rich import inspect


async def ping(ip):
    cmd = f"ping -c 3 -n {ip}".split()
    proc = await asyncio.create_subprocess_exec(
        *cmd,
        stdout=asyncio.subprocess.DEVNULL,
        stderr=asyncio.subprocess.DEVNULL,
        # encoding="utf-8",
    )
    returncode = await proc.wait()
    ip_is_reachable = returncode == 0
    return ip_is_reachable


async def ping_ip_list(ip_list):
    coroutines = [ping(ip) for ip in ip_list]
    result = await asyncio.gather(*coroutines)
    return result


if __name__ == "__main__":
    ip_list = ["192.168.100.1", "192.168.100.2", "8.8.8.8"]
    results = asyncio.run(ping_ip_list(ip_list))
    print(results)

