import asyncio


async def ping_ip(ip):
    proc = await asyncio.create_subprocess_exec(
        "ping", "-c", "3", "-n", ip,
        stdout=asyncio.subprocess.PIPE,
        stderr=asyncio.subprocess.PIPE,
    )
    stdout, stderr = await proc.communicate()
    if " 0% packet loss" in stdout.decode("utf-8"):
        return True
    else:
        return False


async def ping_ip_list(ip_list):
    coroutines = [ping_ip(ip) for ip in ip_list]
    results = await asyncio.gather(*coroutines)
    return results


if __name__ == "__main__":
    ip_list = ["192.168.100.1", "192.168.100.2", "8.8.8.8"]
    results = asyncio.run(ping_ip_list(ip_list))
    print(results)

