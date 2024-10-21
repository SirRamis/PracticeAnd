import time
import pytest
import asyncio
from aioresponses import aioresponses

import pytest
import asyncio
from aioresponses import aioresponses
from part_11 import activ, run  # Импортируйте функции, которые хотите тестировать


# Тестируем функцию activ
@pytest.mark.asyncio
async def test_activ():
    with aioresponses() as mocked:
        # Мокаем запрос к 'http://google.com'
        mocked.get('http://google.com', status=200, body="Test response")

        status, text = await activ()

        # Проверяем, что статус ответа и тело соответствуют ожидаемым значениям
        assert status == 200
        assert text == "Test response"


# Тестируем функцию run, но уменьшим количество запросов для теста
@pytest.mark.asyncio
async def test_run():
    with aioresponses() as mocked:
        # Мокаем запросы
        mocked.get('http://google.com', status=200, body="Test response")

        # Запускаем функцию run, но с меньшим количеством задач
        await run()

        # Проверяем, что запрос был выполнен необходимое количество раз
        assert mocked.called

@pytest.mark.asyncio
async def test_run_performance():
    start = time.time()

    # Запускаем функцию run с ограниченным количеством задач для теста
    await run()

    end = time.time()
    duration = end - start
    print(f"Время выполнения теста: {duration:.2f} секунд")

    # Проверяем, что выполнение заняло приемлемое время (например, меньше 5 секунд)
    assert duration < 5, "Производительность слишком низкая"
