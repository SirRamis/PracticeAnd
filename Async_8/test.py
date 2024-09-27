from semaphore import activ
import pytest
import asyncio

@pytest.mark.asyncio
async def test():
    status, response_text = await activ()
    assert status == 200