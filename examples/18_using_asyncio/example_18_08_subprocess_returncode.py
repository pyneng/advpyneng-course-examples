import asyncio


async def ping_ip(ip):
    # cmd = f"ping -c 3 -n {ip}".split()
    proc = await asyncio.create_subprocess_exec(
        "ping", "-c", "3", "-n", ip,
        # *cmd
        stdout=asyncio.subprocess.DEVNULL,
        stderr=asyncio.subprocess.DEVNULL,
    )
    returncode = await proc.wait()
    return returncode == 0


async def ping_ip_list(ip_list):
    coroutines = [ping_ip(ip) for ip in ip_list]
    results = await asyncio.gather(*coroutines)
    return results


if __name__ == "__main__":
    ip_list = ["192.168.100.1", "192.168.100.2", "8.8.8.8"]
    results = asyncio.run(ping_ip_list(ip_list))
    print(results)

