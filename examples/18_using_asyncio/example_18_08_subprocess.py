import asyncio


async def ping(ip):
    proc = await asyncio.create_subprocess_exec(
        *f"ping -c 3 -n {ip}".split(),
        stdout=asyncio.subprocess.PIPE,
        stderr=asyncio.subprocess.PIPE,
        # encoding="utf-8",
    )

    # stdout, stderr = await proc.communicate()
    await proc.wait()

    ip_is_reachable = proc.returncode == 0
    return ip_is_reachable


async def ping_ip_list(ip_list):
    coroutines = [ping(ip) for ip in ip_list]
    result = await asyncio.gather(*coroutines)
    return result


if __name__ == "__main__":
    ip_list = ["192.168.100.1", "192.168.100.2", "8.8.8.8"]
    results = asyncio.run(ping_ip_list(ip_list))
    print(results)
