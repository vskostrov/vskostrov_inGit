import pytest
import datetime

@pytest.fixture
def time_start():
    start_time = datetime.datetime.now()
    print(f"\nВремя начала тестов класса: {start_time.strftime('%H:%M:%S')}")
    yield
    end_time = datetime.datetime.now()
    print(f"\n Время окончания тестов класса: {end_time.strftime('%H:%M:%S')}")

@pytest.fixture
def time_stop():
    start_time = datetime.datetime.now()
    yield
    end_time = datetime.datetime.now()
    exec_time = end_time - start_time
    return print(f"\n Время выполнения теста: {round(exec_time.microseconds/10**6 , 3)} секунд.")