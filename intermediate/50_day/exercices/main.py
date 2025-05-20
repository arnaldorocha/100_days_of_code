import time

# ✅ Função decoradora
def speed_calc_decorator(function):
    def wrapper():
        start_time = time.time()  # ⏱️ Marca o tempo antes de executar a função
        function()                # ⚙️ Executa a função
        end_time = time.time()    # ⏱️ Marca o tempo depois de executar a função
        execution_time = end_time - start_time
        print(f"velocidade de execução da função {function.__name__} : {execution_time}s")
    return wrapper

# ✅ Funções para testar
@speed_calc_decorator
def fast_function():
    for i in range(1000000):
        i * i

@speed_calc_decorator
def slow_function():
    for i in range(10000000):
        i * i

# ✅ Executando
fast_function()
slow_function()


# import time
# current_time = time.time()
# print(current_time)

# def speed_calc_decorator(function):
#     def wrapper_function():
#         start_time = time.time()
#         function()
#         end_time = time.time()
#         print(f"{function.__name__} run speed: {end_time - start_time}s")
#     return wrapper_function

# @speed_calc_decorator
# def fast_function():
#     for i in range(10000000):
#         i * i
        
# @speed_calc_decorator
# def slow_function():
#     for i in range(100000000):
#         i * i
        
# fast_function()
# slow_function()
