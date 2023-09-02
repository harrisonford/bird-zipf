import asyncio
import xenocanto

# check github to get an idea how to use the params input to filter species
params = ["Common Swift"]
timeout_seconds = 600

# wrap download in async function
async def download_task():
    await xenocanto.download(filt=params)

def main():
    asyncio.run(asyncio.wait_for(download_task(), timeout_seconds))
    return 1


if __name__ == '__main__':
    main()
