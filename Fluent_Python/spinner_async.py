
import itertools
import time
import asyncio

async def spin(msg: str) -> None:
    for char in itertools.cycle(r'\|/-'):
        status = f'\r{char} {msg}'
        print(status, end='', flush=True)
        
async def slow() -> int:
    time.sleep(3)
    return 42


async def supervisor() -> int:
    spinner = asyncio.create_task(spin('thinking'))
    print(f'spinner object: {spinner}')
    result = await slow()
    spinner.cancel()
    return result

def main() -> None:
    result = asyncio.run(supervisor())
    print(f'\nAnswer: {result}')
    
if __name__ == '__main__':
    main()
    
    
#EOF
