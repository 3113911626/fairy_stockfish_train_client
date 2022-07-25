import sys
import os
import time
import subprocess
import multiprocessing as mp

FILE_NAME = "xiangqi.bin"
FILE_NAME2 = "xiangqi2.bin"
FILE_NAME3 = "xiangqi3.bin"
FILE_NAME4 = "xiangqi4.bin"
FILE_NAME5 = "xiangqi5.bin"
FILE_NAME6 = "xiangqi6.bin"
FILE_NAME7 = "xiangqi7.bin"
FILE_NAME8 = "xiangqi8.bin"
FILE_NAME9 = "xiangqi9.bin"
FILE_NAME10 = "xiangqi10.bin"
FILE_NAME11 = "xiangqi11.bin"
FILE_NAME12 = "xiangqi12.bin"
FILE_NAME_UPLOAD = "xiangqi-upload.bin"
FILE_NAME_UPLOAD2 = "xiangqi-upload2.bin"
FILE_NAME_UPLOAD3 = "xiangqi-upload3.bin"
FILE_NAME_UPLOAD4 = "xiangqi-upload4.bin"
FILE_NAME_UPLOAD5 = "xiangqi-upload5.bin"
FILE_NAME_UPLOAD6 = "xiangqi-upload6.bin"
FILE_NAME_UPLOAD7 = "xiangqi-upload7.bin"
FILE_NAME_UPLOAD8 = "xiangqi-upload8.bin"
FILE_NAME_UPLOAD9 = "xiangqi-upload9.bin"
FILE_NAME_UPLOAD10 = "xiangqi-upload10.bin"
FILE_NAME_UPLOAD11 = "xiangqi-upload11.bin"
FILE_NAME_UPLOAD12 = "xiangqi-upload12.bin"

test_params = {
    "depth": 4,
    "eval_limit": 3000,
    "eval_diff_limit": 500,
    "random_move_min_ply": 1,
    "random_move_max_ply": 3,
    "random_move_count": 8,
    "random_multi_pv": 4,
    "random_multi_pv_diff": 100,
    "random_multi_pv_depth": 4,
    "write_min_ply": 1,
    "write_max_ply": 400,
}


def get_generation_command(data_count, threads, output_file, generation_params):
    params = f"""setoption name UCI_Variant value xiangqi
setoption name Use NNUE value true
setoption name EvalFile value ./xiangqi-weights.nnue
setoption name Threads value {threads}
setoption name Hash value 256
"""
    gen_params_str = ""
    for k, v in generation_params.items():
        gen_params_str += f"{k} {v} "
    cmd = f"generate_training_data count {data_count} book xiangqi-book.epd {gen_params_str}" \
          f"set_recommended_uci_options data_format bin output_file_name {output_file}\n"
    return params + cmd


def generate_data(params, threads=-1, amount=10000):
    if threads < 1:
        threads = mp.cpu_count()
    if os.path.exists(FILE_NAME):
        os.remove(FILE_NAME)
    while os.path.exists(FILE_NAME):
        time.sleep(0.1)
    exe_file = "fairy.exe" if os.name == "nt" else "./fairy"
    if os.name != "nt":
        os.system("chmod +x " + exe_file)
    fairy = subprocess.Popen([exe_file], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    tmp_params = get_generation_command(amount, threads, FILE_NAME, params)
    fairy.stdin.write(tmp_params.encode())
    fairy.stdin.flush()
    fairy.stdout.flush()
    output = fairy.stdout.readline()
    while output:
        output = output.decode("utf-8").replace("\r\n", "")
        if "sfen" in output or "evaluation" in output:
            print(output)
        if "finished" in output:
            print(output)
            time.sleep(1)
            fairy.terminate()
            break
        fairy.stdout.flush()
        output = fairy.stdout.readline()
    while not os.path.exists(FILE_NAME):
        time.sleep(0.1)

def generate_data2(params, threads=-1, amount=10000):
    if threads < 1:
        threads = mp.cpu_count()
    if os.path.exists(FILE_NAME2):
        os.remove(FILE_NAME2)
    while os.path.exists(FILE_NAME2):
        time.sleep(0.1)
        e=0
    exe_file = "fairy.exe" if os.name == "nt" else "./fairy"
    if os.name != "nt":
        os.system("chmod +x " + exe_file)
    fairy = subprocess.Popen([exe_file], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    tmp_params = get_generation_command(amount, threads, FILE_NAME2, params)
    fairy.stdin.write(tmp_params.encode())
    fairy.stdin.flush()
    fairy.stdout.flush()
    output = fairy.stdout.readline()
    while output:
        output = output.decode("utf-8").replace("\r\n", "")
        if "sfen" in output or "evaluation" in output:
            print(output)
        if "finished" in output:
            print(output)
            time.sleep(1)
            fairy.terminate()
            break
        fairy.stdout.flush()
        output = fairy.stdout.readline()
    while not os.path.exists(FILE_NAME2):
        time.sleep(0.1)

def generate_data3(params, threads=-1, amount=10000):
    if threads < 1:
        threads = mp.cpu_count()
    if os.path.exists(FILE_NAME3):
        os.remove(FILE_NAME3)
    while os.path.exists(FILE_NAME3):
        time.sleep(0.1)
        e=0
    exe_file = "fairy.exe" if os.name == "nt" else "./fairy"
    if os.name != "nt":
        os.system("chmod +x " + exe_file)
    fairy = subprocess.Popen([exe_file], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    tmp_params = get_generation_command(amount, threads, FILE_NAME3, params)
    fairy.stdin.write(tmp_params.encode())
    fairy.stdin.flush()
    fairy.stdout.flush()
    output = fairy.stdout.readline()
    while output:
        output = output.decode("utf-8").replace("\r\n", "")
        if "sfen" in output or "evaluation" in output:
            print(output)
        if "finished" in output:
            print(output)
            time.sleep(1)
            fairy.terminate()
            break
        fairy.stdout.flush()
        output = fairy.stdout.readline()
    while not os.path.exists(FILE_NAME3):
        time.sleep(0.1)
        e=0

def generate_data4(params, threads=-1, amount=10000):
    if threads < 1:
        threads = mp.cpu_count()
    if os.path.exists(FILE_NAME4):
        os.remove(FILE_NAME4)
    while os.path.exists(FILE_NAME4):
        time.sleep(0.1)
        e=0
    exe_file = "fairy.exe" if os.name == "nt" else "./fairy"
    if os.name != "nt":
        os.system("chmod +x " + exe_file)
    fairy = subprocess.Popen([exe_file], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    tmp_params = get_generation_command(amount, threads, FILE_NAME4, params)
    fairy.stdin.write(tmp_params.encode())
    fairy.stdin.flush()
    fairy.stdout.flush()
    output = fairy.stdout.readline()
    while output:
        output = output.decode("utf-8").replace("\r\n", "")
        if "sfen" in output or "evaluation" in output:
            print(output)
        if "finished" in output:
            print(output)
            time.sleep(1)
            fairy.terminate()
            break
        fairy.stdout.flush()
        output = fairy.stdout.readline()
    while not os.path.exists(FILE_NAME4):
        time.sleep(0.1)
        e=0

def generate_data5(params, threads=-1, amount=10000):
    if threads < 1:
        threads = mp.cpu_count()
    if os.path.exists(FILE_NAME5):
        os.remove(FILE_NAME5)
    while os.path.exists(FILE_NAME5):
        time.sleep(0.1)
        e=0
    exe_file = "fairy.exe" if os.name == "nt" else "./fairy"
    if os.name != "nt":
        os.system("chmod +x " + exe_file)
    fairy = subprocess.Popen([exe_file], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    tmp_params = get_generation_command(amount, threads, FILE_NAME5, params)
    fairy.stdin.write(tmp_params.encode())
    fairy.stdin.flush()
    fairy.stdout.flush()
    output = fairy.stdout.readline()
    while output:
        output = output.decode("utf-8").replace("\r\n", "")
        if "sfen" in output or "evaluation" in output:
            print(output)
        if "finished" in output:
            print(output)
            time.sleep(1)
            fairy.terminate()
            break
        fairy.stdout.flush()
        output = fairy.stdout.readline()
    while not os.path.exists(FILE_NAME5):
        time.sleep(0.1)
        e=0

def generate_data6(params, threads=-1, amount=10000):
    if threads < 1:
        threads = mp.cpu_count()
    if os.path.exists(FILE_NAME6):
        os.remove(FILE_NAME6)
    while os.path.exists(FILE_NAME6):
        time.sleep(0.1)
        e=0
    exe_file = "fairy.exe" if os.name == "nt" else "./fairy"
    if os.name != "nt":
        os.system("chmod +x " + exe_file)
    fairy = subprocess.Popen([exe_file], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    tmp_params = get_generation_command(amount, threads, FILE_NAME6, params)
    fairy.stdin.write(tmp_params.encode())
    fairy.stdin.flush()
    fairy.stdout.flush()
    output = fairy.stdout.readline()
    while output:
        output = output.decode("utf-8").replace("\r\n", "")
        if "sfen" in output or "evaluation" in output:
            print(output)
        if "finished" in output:
            print(output)
            time.sleep(1)
            fairy.terminate()
            break
        fairy.stdout.flush()
        output = fairy.stdout.readline()
    while not os.path.exists(FILE_NAME3):
        time.sleep(0.1)
        e=0

def generate_data7(params, threads=-1, amount=10000):
    if threads < 1:
        threads = mp.cpu_count()
    if os.path.exists(FILE_NAME7):
        os.remove(FILE_NAME7)
    while os.path.exists(FILE_NAME7):
        time.sleep(0.1)
        e=0
    exe_file = "fairy.exe" if os.name == "nt" else "./fairy"
    if os.name != "nt":
        os.system("chmod +x " + exe_file)
    fairy = subprocess.Popen([exe_file], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    tmp_params = get_generation_command(amount, threads, FILE_NAME7, params)
    fairy.stdin.write(tmp_params.encode())
    fairy.stdin.flush()
    fairy.stdout.flush()
    output = fairy.stdout.readline()
    while output:
        output = output.decode("utf-8").replace("\r\n", "")
        if "sfen" in output or "evaluation" in output:
            print(output)
        if "finished" in output:
            print(output)
            time.sleep(1)
            fairy.terminate()
            break
        fairy.stdout.flush()
        output = fairy.stdout.readline()
    while not os.path.exists(FILE_NAME7):
        time.sleep(0.1)
        e=0

def generate_data8(params, threads=-1, amount=10000):
    if threads < 1:
        threads = mp.cpu_count()
    if os.path.exists(FILE_NAME8):
        os.remove(FILE_NAME8)
    while os.path.exists(FILE_NAME8):
        time.sleep(0.1)
        e=0
    exe_file = "fairy.exe" if os.name == "nt" else "./fairy"
    if os.name != "nt":
        os.system("chmod +x " + exe_file)
    fairy = subprocess.Popen([exe_file], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    tmp_params = get_generation_command(amount, threads, FILE_NAME8, params)
    fairy.stdin.write(tmp_params.encode())
    fairy.stdin.flush()
    fairy.stdout.flush()
    output = fairy.stdout.readline()
    while output:
        output = output.decode("utf-8").replace("\r\n", "")
        if "sfen" in output or "evaluation" in output:
            print(output)
        if "finished" in output:
            print(output)
            time.sleep(1)
            fairy.terminate()
            break
        fairy.stdout.flush()
        output = fairy.stdout.readline()
    while not os.path.exists(FILE_NAME8):
        time.sleep(0.1)
        e=0

def generate_data9(params, threads=-1, amount=10000):
    if threads < 1:
        threads = mp.cpu_count()
    if os.path.exists(FILE_NAME9):
        os.remove(FILE_NAME9)
    while os.path.exists(FILE_NAME9):
        time.sleep(0.1)
        e=0
    exe_file = "fairy.exe" if os.name == "nt" else "./fairy"
    if os.name != "nt":
        os.system("chmod +x " + exe_file)
    fairy = subprocess.Popen([exe_file], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    tmp_params = get_generation_command(amount, threads, FILE_NAME9, params)
    fairy.stdin.write(tmp_params.encode())
    fairy.stdin.flush()
    fairy.stdout.flush()
    output = fairy.stdout.readline()
    while output:
        output = output.decode("utf-8").replace("\r\n", "")
        if "sfen" in output or "evaluation" in output:
            print(output)
        if "finished" in output:
            print(output)
            time.sleep(1)
            fairy.terminate()
            break
        fairy.stdout.flush()
        output = fairy.stdout.readline()
    while not os.path.exists(FILE_NAME9):
        time.sleep(0.1)
        e=0

def generate_data10(params, threads=-1, amount=10000):
    if threads < 1:
        threads = mp.cpu_count()
    if os.path.exists(FILE_NAME10):
        os.remove(FILE_NAME10)
    while os.path.exists(FILE_NAME10):
        time.sleep(0.1)
        e=0
    exe_file = "fairy.exe" if os.name == "nt" else "./fairy"
    if os.name != "nt":
        os.system("chmod +x " + exe_file)
    fairy = subprocess.Popen([exe_file], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    tmp_params = get_generation_command(amount, threads, FILE_NAME10, params)
    fairy.stdin.write(tmp_params.encode())
    fairy.stdin.flush()
    fairy.stdout.flush()
    output = fairy.stdout.readline()
    while output:
        output = output.decode("utf-8").replace("\r\n", "")
        if "sfen" in output or "evaluation" in output:
            print(output)
        if "finished" in output:
            print(output)
            time.sleep(1)
            fairy.terminate()
            break
        fairy.stdout.flush()
        output = fairy.stdout.readline()
    while not os.path.exists(FILE_NAME10):
        time.sleep(0.1)
        e=0

def generate_data11(params, threads=-1, amount=10000):
    if threads < 1:
        threads = mp.cpu_count()
    if os.path.exists(FILE_NAME11):
        os.remove(FILE_NAME11)
    while os.path.exists(FILE_NAME11):
        time.sleep(0.1)
        e=0
    exe_file = "fairy.exe" if os.name == "nt" else "./fairy"
    if os.name != "nt":
        os.system("chmod +x " + exe_file)
    fairy = subprocess.Popen([exe_file], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    tmp_params = get_generation_command(amount, threads, FILE_NAME11, params)
    fairy.stdin.write(tmp_params.encode())
    fairy.stdin.flush()
    fairy.stdout.flush()
    output = fairy.stdout.readline()
    while output:
        output = output.decode("utf-8").replace("\r\n", "")
        if "sfen" in output or "evaluation" in output:
            print(output)
        if "finished" in output:
            print(output)
            time.sleep(1)
            fairy.terminate()
            break
        fairy.stdout.flush()
        output = fairy.stdout.readline()
    while not os.path.exists(FILE_NAME11):
        time.sleep(0.1)
        e=0

def generate_data12(params, threads=-1, amount=10000):
    if threads < 1:
        threads = mp.cpu_count()
    if os.path.exists(FILE_NAME12):
        os.remove(FILE_NAME12)
    while os.path.exists(FILE_NAME12):
        time.sleep(0.1)
        e=0
    exe_file = "fairy.exe" if os.name == "nt" else "./fairy"
    if os.name != "nt":
        os.system("chmod +x " + exe_file)
    fairy = subprocess.Popen([exe_file], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    tmp_params = get_generation_command(amount, threads, FILE_NAME12, params)
    fairy.stdin.write(tmp_params.encode())
    fairy.stdin.flush()
    fairy.stdout.flush()
    output = fairy.stdout.readline()
    while output:
        output = output.decode("utf-8").replace("\r\n", "")
        if "sfen" in output or "evaluation" in output:
            print(output)
        if "finished" in output:
            print(output)
            time.sleep(1)
            fairy.terminate()
            break
        fairy.stdout.flush()
        output = fairy.stdout.readline()
    while not os.path.exists(FILE_NAME12):
        time.sleep(0.1)
        e=0

if __name__ == "__main__":
    generate_data(test_params, threads=4, amount=5000)

