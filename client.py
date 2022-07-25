import os
import shutil
import sys
import threading
import random
import traceback

import client_helper
import time
import fairy
import argparse
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
program_version = "1.2"
model_version = -1
Debug = False
generate_amount = 10000
parser = argparse.ArgumentParser(description="分布式生成棋谱")
parser.add_argument("--user", default="VinXiangQi", type=str, help="用于统计训练量的用户名")
parser.add_argument("--threads", default=-1, type=int, help="用于跑谱的核心数")
Args = parser.parse_args()
generation_params = {}
NEED_EXIT = False

param_keys_map = {
    "d": "depth",
    "el": "eval_limit",
    "edl": "eval_diff_limit",
    "rmi": "random_move_min_ply",
    "rma": "random_move_max_ply",
    "rc": "random_move_count",
    "rmp": "random_multi_pv",
    "pdi": "random_multi_pv_diff",
    "pde": "random_multi_pv_depth",
    "wmi": "write_min_ply",
    "wma": "write_max_ply",
}


param_keys_map_rev = {v: k for k, v in param_keys_map.items()}


def params_decompress(params_compressed):
    new_params = {}
    for k, v in params_compressed.items():
        if k in param_keys_map:
            new_params[param_keys_map[k]] = v
        else:
            new_params[k] = v
    return new_params


def params_compress(params):
    new_params = {}
    for k, v in params.items():
        if k in param_keys_map_rev:
            new_params[param_keys_map_rev[k]] = v
        else:
            new_params[k] = v
    return new_params


def params_to_str(params):
    return "*".join([f"{k}-{v}" for k, v in params.items()])


def check_update():
    global generation_params, NEED_EXIT
    info = client_helper.get_model_info()
    while info is None:
        print("获取版本失败")
        time.sleep(1)
        info = client_helper.get_model_info()
    if program_version != info["program_version"]:
        print(f"发现新版本客户端: {info['program_version']}，请更新客户端！")
        NEED_EXIT = True
        sys.exit(1)
    generation_params = params_decompress(info["params"])
    update_book(info["book_urls"])
    update_model(info["weight_version"], info["urls"])


def update_model(ver, urls):
    global model_version
    if Debug:
        return
    if ver != model_version:
        print(f"发现新模型: {ver}")
        if urls is None or len(urls) == 0:
            print("未找到下载地址，更新失败！")
            return
        st = time.time()
        client_helper.download_file_multiurl_retry(urls, "xiangqi-weights.nnue")
        time.sleep(0.2)
        file_size = os.path.getsize("xiangqi-weights.nnue")
        if file_size < 1024 * 1024:
            with open("xiangqi-weights.nnue", "r") as f:
                print(f.read())
            print("文件下载错误！")
        model_version = ver
        print(f"更新模型成功！耗时: {round(time.time() - st, 1)}s")


def update_book(urls):
    if urls is not None and len(urls) > 0:
        print("正在下载开局库")
        st = time.time()
        client_helper.download_file_multiurl_retry(urls, "xiangqi-book.epd")
        print(f"下载成功！耗时: {round(time.time()-st, 1)}s")


def upload_data():
    global generation_params, NEED_EXIT
    with open(FILE_NAME_UPLOAD, "rb") as f:
        result = client_helper.upload_data(f.read(), model_version, Args.user,
                                           params_to_str(params_compress(generation_params)))
        if "params" in result:
            generation_params = params_decompress(result["params"])
        if result[1] == "客户端版本不正确":
            print("客户端版本不正确，请更新客户端")
            NEED_EXIT = True
            sys.exit(1)
    shutil.rmtree(FILE_NAME_UPLOAD, ignore_errors=True)
    update_model(result[0], result[1])
def upload_data2():
    global generation_params
    with open(FILE_NAME_UPLOAD2, "rb") as f:
        result = client_helper.upload_data(f.read(), model_version, Args.user,
                                           params_to_str(params_compress(generation_params)))
        if "params" in result:
            generation_params = params_decompress(result["params"])
        if result[1] == "客户端版本不正确":
            print("客户端版本不正确，请更新客户端")
            sys.exit(1)
    shutil.rmtree(FILE_NAME_UPLOAD2, ignore_errors=True)
    update_model(result[0], result[1])
def upload_data3():
    global generation_params
    with open(FILE_NAME_UPLOAD3, "rb") as f:
        result = client_helper.upload_data(f.read(), model_version, Args.user,
                                           params_to_str(params_compress(generation_params)))
        if "params" in result:
            generation_params = params_decompress(result["params"])
        if result[1] == "客户端版本不正确":
            print("客户端版本不正确，请更新客户端")
            sys.exit(1)
    shutil.rmtree(FILE_NAME_UPLOAD3, ignore_errors=True)
    update_model(result[0], result[1])
def upload_data4():
    global generation_params
    with open(FILE_NAME_UPLOAD4, "rb") as f:
        result = client_helper.upload_data(f.read(), model_version, Args.user,
                                           params_to_str(params_compress(generation_params)))
        if "params" in result:
            generation_params = params_decompress(result["params"])
        if result[1] == "客户端版本不正确":
            print("客户端版本不正确，请更新客户端")
            sys.exit(1)
    shutil.rmtree(FILE_NAME_UPLOAD4, ignore_errors=True)
    update_model(result[0], result[1])
def upload_data5():
    global generation_params
    with open(FILE_NAME_UPLOAD5, "rb") as f:
        result = client_helper.upload_data(f.read(), model_version, Args.user,
                                           params_to_str(params_compress(generation_params)))
        if "params" in result:
            generation_params = params_decompress(result["params"])
        if result[1] == "客户端版本不正确":
            print("客户端版本不正确，请更新客户端")
            sys.exit(1)
    shutil.rmtree(FILE_NAME_UPLOAD5, ignore_errors=True)
    update_model(result[0], result[1])
def upload_data6():
    global generation_params
    with open(FILE_NAME_UPLOAD6, "rb") as f:
        result = client_helper.upload_data(f.read(), model_version, Args.user,
                                           params_to_str(params_compress(generation_params)))
        if "params" in result:
            generation_params = params_decompress(result["params"])
        if result[1] == "客户端版本不正确":
            print("客户端版本不正确，请更新客户端")
            sys.exit(1)
    shutil.rmtree(FILE_NAME_UPLOAD6, ignore_errors=True)
    update_model(result[0], result[1])
def upload_data7():
    global generation_params
    with open(FILE_NAME_UPLOAD7, "rb") as f:
        result = client_helper.upload_data(f.read(), model_version, Args.user,
                                           params_to_str(params_compress(generation_params)))
        if "params" in result:
            generation_params = params_decompress(result["params"])
        if result[1] == "客户端版本不正确":
            print("客户端版本不正确，请更新客户端")
            sys.exit(1)
    shutil.rmtree(FILE_NAME_UPLOAD7, ignore_errors=True)
    update_model(result[0], result[1])
def upload_data8():
    global generation_params
    with open(FILE_NAME_UPLOAD8, "rb") as f:
        result = client_helper.upload_data(f.read(), model_version, Args.user,
                                           params_to_str(params_compress(generation_params)))
        if "params" in result:
            generation_params = params_decompress(result["params"])
        if result[1] == "客户端版本不正确":
            print("客户端版本不正确，请更新客户端")
            sys.exit(1)
    shutil.rmtree(FILE_NAME_UPLOAD8, ignore_errors=True)
    update_model(result[0], result[1])
def upload_data9():
    global generation_params
    with open(FILE_NAME_UPLOAD9, "rb") as f:
        result = client_helper.upload_data(f.read(), model_version, Args.user,
                                           params_to_str(params_compress(generation_params)))
        if "params" in result:
            generation_params = params_decompress(result["params"])
        if result[1] == "客户端版本不正确":
            print("客户端版本不正确，请更新客户端")
            sys.exit(1)
    shutil.rmtree(FILE_NAME_UPLOAD9, ignore_errors=True)
    update_model(result[0], result[1])
def upload_data10():
    global generation_params
    with open(FILE_NAME_UPLOAD10, "rb") as f:
        result = client_helper.upload_data(f.read(), model_version, Args.user,
                                           params_to_str(params_compress(generation_params)))
        if "params" in result:
            generation_params = params_decompress(result["params"])
        if result[1] == "客户端版本不正确":
            print("客户端版本不正确，请更新客户端")
            sys.exit(1)
    shutil.rmtree(FILE_NAME_UPLOAD10, ignore_errors=True)
    update_model(result[0], result[1])
def upload_data11():
    global generation_params
    with open(FILE_NAME_UPLOAD11, "rb") as f:
        result = client_helper.upload_data(f.read(), model_version, Args.user,
                                           params_to_str(params_compress(generation_params)))
        if "params" in result:
            generation_params = params_decompress(result["params"])
        if result[1] == "客户端版本不正确":
            print("客户端版本不正确，请更新客户端")
            sys.exit(1)
    shutil.rmtree(FILE_NAME_UPLOAD11, ignore_errors=True)
    update_model(result[0], result[1])
def upload_data12():
    global generation_params
    with open(FILE_NAME_UPLOAD12, "rb") as f:
        result = client_helper.upload_data(f.read(), model_version, Args.user,
                                           params_to_str(params_compress(generation_params)))
        if "params" in result:
            generation_params = params_decompress(result["params"])
        if result[1] == "客户端版本不正确":
            print("客户端版本不正确，请更新客户端")
            sys.exit(1)
    shutil.rmtree(FILE_NAME_UPLOAD12, ignore_errors=True)
    update_model(result[0], result[1])

def xc():
    fairy.generate_data(generation_params, threads=Args.threads, amount=generate_amount)
def xc2():
    fairy.generate_data2(generation_params, threads=Args.threads, amount=generate_amount)
def xc3():
    fairy.generate_data3(generation_params, threads=Args.threads, amount=generate_amount)
def xc4():
    fairy.generate_data4(generation_params, threads=Args.threads, amount=generate_amount)
def xc5():
    fairy.generate_data5(generation_params, threads=Args.threads, amount=generate_amount)
def xc6():
    fairy.generate_data6(generation_params, threads=Args.threads, amount=generate_amount)
def xc7():
    fairy.generate_data7(generation_params, threads=Args.threads, amount=generate_amount)
def xc8():
    fairy.generate_data8(generation_params, threads=Args.threads, amount=generate_amount)
def xc9():
    fairy.generate_data9(generation_params, threads=Args.threads, amount=generate_amount)
def xc10():
    fairy.generate_data10(generation_params, threads=Args.threads, amount=generate_amount)
def xc11():
    fairy.generate_data11(generation_params, threads=Args.threads, amount=generate_amount)
def xc12():
    fairy.generate_data12(generation_params, threads=Args.threads, amount=generate_amount)

def wfl():
    while True:
        try:
            print("开始生成棋谱，该过程耗时较长，请耐心等待……")
            start_time = time.time()
            xc()
            time_cost = time.time() - start_time
            speed = 10000 / time_cost
            generate_amount = int(120 * speed)
            generate_amount = (generate_amount // 10000) * 10000
            generate_amount = max(generate_amount, 10000)
            print("生成完成！耗时: {0}s, 下次生成预计生成 {1} 棋谱".format(round(time_cost, 1), generate_amount))
            if not os.path.exists(FILE_NAME):
                print("棋谱文件不存在，上传失败！")
                time.sleep(1)
            shutil.move(FILE_NAME, FILE_NAME_UPLOAD)
            thread_upload = threading.Thread(target=upload_data)
            thread_upload.setDaemon(True)
            thread_upload.start()
        except Exception as ex:
            print(repr(ex))
            traceback.print_exc()
        time.sleep(0.1)

def wfl2():
    while True:
        try:
            print("开始生成棋谱，该过程耗时较长，请耐心等待……")
            start_time = time.time()
            xc2()
            time_cost = time.time() - start_time
            speed = 10000 / time_cost
            generate_amount = int(120 * speed)
            generate_amount = (generate_amount // 10000) * 10000
            generate_amount = max(generate_amount, 10000)
            print("生成完成！耗时: {0}s, 下次生成预计生成 {1} 棋谱".format(round(time_cost, 1), generate_amount))
            if not os.path.exists(FILE_NAME2):
                print("棋谱文件不存在，上传失败！")
                time.sleep(1)
            shutil.move(FILE_NAME2, FILE_NAME_UPLOAD2)
            thread_upload = threading.Thread(target=upload_data2)
            thread_upload.setDaemon(True)
            thread_upload.start()
        except Exception as ex:
            print(repr(ex))
            traceback.print_exc()
        time.sleep(0.1)

def wfl3():
    while True:
        try:
            print("开始生成棋谱，该过程耗时较长，请耐心等待……")
            start_time = time.time()
            xc3()
            time_cost = time.time() - start_time
            speed = 10000 / time_cost
            generate_amount = int(120 * speed)
            generate_amount = (generate_amount // 10000) * 10000
            generate_amount = max(generate_amount, 10000)
            print("生成完成！耗时: {0}s, 下次生成预计生成 {1} 棋谱".format(round(time_cost, 1), generate_amount))
            if not os.path.exists(FILE_NAME3):
                print("棋谱文件不存在，上传失败！")
                time.sleep(1)
            shutil.move(FILE_NAME3, FILE_NAME_UPLOAD3)
            thread_upload = threading.Thread(target=upload_data3)
            thread_upload.setDaemon(True)
            thread_upload.start()
        except Exception as ex:
            print(repr(ex))
            traceback.print_exc()
        time.sleep(0.1)

def wfl4():
    while True:
        try:
            print("开始生成棋谱，该过程耗时较长，请耐心等待……")
            start_time = time.time()
            xc4()
            time_cost = time.time() - start_time
            speed = 10000 / time_cost
            generate_amount = int(120 * speed)
            generate_amount = (generate_amount // 10000) * 10000
            generate_amount = max(generate_amount, 10000)
            print("生成完成！耗时: {0}s, 下次生成预计生成 {1} 棋谱".format(round(time_cost, 1), generate_amount))
            if not os.path.exists(FILE_NAME4):
                print("棋谱文件不存在，上传失败！")
                time.sleep(1)
            shutil.move(FILE_NAME4, FILE_NAME_UPLOAD4)
            thread_upload = threading.Thread(target=upload_data4)
            thread_upload.setDaemon(True)
            thread_upload.start()
        except Exception as ex:
            print(repr(ex))
            traceback.print_exc()
        time.sleep(0.1)

def wfl5():
    while True:
        try:
            print("开始生成棋谱，该过程耗时较长，请耐心等待……")
            start_time = time.time()
            xc5()
            time_cost = time.time() - start_time
            speed = 10000 / time_cost
            generate_amount = int(120 * speed)
            generate_amount = (generate_amount // 10000) * 10000
            generate_amount = max(generate_amount, 10000)
            print("生成完成！耗时: {0}s, 下次生成预计生成 {1} 棋谱".format(round(time_cost, 1), generate_amount))
            if not os.path.exists(FILE_NAME5):
                print("棋谱文件不存在，上传失败！")
                time.sleep(1)
            shutil.move(FILE_NAME5, FILE_NAME_UPLOAD5)
            thread_upload = threading.Thread(target=upload_data5)
            thread_upload.setDaemon(True)
            thread_upload.start()
        except Exception as ex:
            print(repr(ex))
            traceback.print_exc()
        time.sleep(0.1)

def wfl6():
    while True:
        try:
            print("开始生成棋谱，该过程耗时较长，请耐心等待……")
            start_time = time.time()
            xc6()
            time_cost = time.time() - start_time
            speed = 10000 / time_cost
            generate_amount = int(120 * speed)
            generate_amount = (generate_amount // 10000) * 10000
            generate_amount = max(generate_amount, 10000)
            print("生成完成！耗时: {0}s, 下次生成预计生成 {1} 棋谱".format(round(time_cost, 1), generate_amount))
            if not os.path.exists(FILE_NAME6):
                print("棋谱文件不存在，上传失败！")
                time.sleep(1)
            shutil.move(FILE_NAME6, FILE_NAME_UPLOAD6)
            thread_upload = threading.Thread(target=upload_data6)
            thread_upload.setDaemon(True)
            thread_upload.start()
        except Exception as ex:
            print(repr(ex))
            traceback.print_exc()
        time.sleep(0.1)

def wfl7():
    while True:
        try:
            print("开始生成棋谱，该过程耗时较长，请耐心等待……")
            start_time = time.time()
            xc7()
            time_cost = time.time() - start_time
            speed = 10000 / time_cost
            generate_amount = int(120 * speed)
            generate_amount = (generate_amount // 10000) * 10000
            generate_amount = max(generate_amount, 10000)
            print("生成完成！耗时: {0}s, 下次生成预计生成 {1} 棋谱".format(round(time_cost, 1), generate_amount))
            if not os.path.exists(FILE_NAME7):
                print("棋谱文件不存在，上传失败！")
                time.sleep(1)
            shutil.move(FILE_NAME7, FILE_NAME_UPLOAD7)
            thread_upload = threading.Thread(target=upload_data7)
            thread_upload.setDaemon(True)
            thread_upload.start()
        except Exception as ex:
            print(repr(ex))
            traceback.print_exc()
        time.sleep(0.1)

def wfl8():
    while True:
        try:
            print("开始生成棋谱，该过程耗时较长，请耐心等待……")
            start_time = time.time()
            xc8()
            time_cost = time.time() - start_time
            speed = 10000 / time_cost
            generate_amount = int(120 * speed)
            generate_amount = (generate_amount // 10000) * 10000
            generate_amount = max(generate_amount, 10000)
            print("生成完成！耗时: {0}s, 下次生成预计生成 {1} 棋谱".format(round(time_cost, 1), generate_amount))
            if not os.path.exists(FILE_NAME8):
                print("棋谱文件不存在，上传失败！")
                time.sleep(1)
            shutil.move(FILE_NAME8, FILE_NAME_UPLOAD8)
            thread_upload = threading.Thread(target=upload_data8)
            thread_upload.setDaemon(True)
            thread_upload.start()
        except Exception as ex:
            print(repr(ex))
            traceback.print_exc()
        time.sleep(0.1)

def wfl9():
    while True:
        try:
            print("开始生成棋谱，该过程耗时较长，请耐心等待……")
            start_time = time.time()
            xc9()
            time_cost = time.time() - start_time
            speed = 10000 / time_cost
            generate_amount = int(120 * speed)
            generate_amount = (generate_amount // 10000) * 10000
            generate_amount = max(generate_amount, 10000)
            print("生成完成！耗时: {0}s, 下次生成预计生成 {1} 棋谱".format(round(time_cost, 1), generate_amount))
            if not os.path.exists(FILE_NAME9):
                print("棋谱文件不存在，上传失败！")
                time.sleep(1)
            shutil.move(FILE_NAME9, FILE_NAME_UPLOAD9)
            thread_upload = threading.Thread(target=upload_data9)
            thread_upload.setDaemon(True)
            thread_upload.start()
        except Exception as ex:
            print(repr(ex))
            traceback.print_exc()
        time.sleep(0.1)

def wfl10():
    while True:
        try:
            print("开始生成棋谱，该过程耗时较长，请耐心等待……")
            start_time = time.time()
            xc10()
            time_cost = time.time() - start_time
            speed = 10000 / time_cost
            generate_amount = int(120 * speed)
            generate_amount = (generate_amount // 10000) * 10000
            generate_amount = max(generate_amount, 10000)
            print("生成完成！耗时: {0}s, 下次生成预计生成 {1} 棋谱".format(round(time_cost, 1), generate_amount))
            if not os.path.exists(FILE_NAME10):
                print("棋谱文件不存在，上传失败！")
                time.sleep(1)
            shutil.move(FILE_NAME10, FILE_NAME_UPLOAD10)
            thread_upload = threading.Thread(target=upload_data10)
            thread_upload.setDaemon(True)
            thread_upload.start()
        except Exception as ex:
            print(repr(ex))
            traceback.print_exc()
        time.sleep(0.1)

def wfl11():
    while True:
        try:
            print("开始生成棋谱，该过程耗时较长，请耐心等待……")
            start_time = time.time()
            xc11()
            time_cost = time.time() - start_time
            speed = 10000 / time_cost
            generate_amount = int(120 * speed)
            generate_amount = (generate_amount // 10000) * 10000
            generate_amount = max(generate_amount, 10000)
            print("生成完成！耗时: {0}s, 下次生成预计生成 {1} 棋谱".format(round(time_cost, 1), generate_amount))
            if not os.path.exists(FILE_NAME11):
                print("棋谱文件不存在，上传失败！")
                time.sleep(1)
            shutil.move(FILE_NAME11, FILE_NAME_UPLOAD11)
            thread_upload = threading.Thread(target=upload_data)
            thread_upload.setDaemon(True)
            thread_upload.start()
        except Exception as ex:
            print(repr(ex))
            traceback.print_exc()
        time.sleep(0.1)

def wfl12():
    while True:
        try:
            print("开始生成棋谱，该过程耗时较长，请耐心等待……")
            start_time = time.time()
            xc12()
            time_cost = time.time() - start_time
            speed = 10000 / time_cost
            generate_amount = int(120 * speed)
            generate_amount = (generate_amount // 10000) * 10000
            generate_amount = max(generate_amount, 10000)
            print("生成完成！耗时: {0}s, 下次生成预计生成 {1} 棋谱".format(round(time_cost, 1), generate_amount))
            if not os.path.exists(FILE_NAME12):
                print("棋谱文件不存在，上传失败！")
                time.sleep(1)
            shutil.move(FILE_NAME12, FILE_NAME_UPLOAD12)
            thread_upload = threading.Thread(target=upload_data)
            thread_upload.setDaemon(True)
            thread_upload.start()
        except Exception as ex:
            print(repr(ex))
            traceback.print_exc()
        time.sleep(0.1)

if __name__ == "__main__":
    print("-----------------------------------")
    print(f"----- 以 {Args.user} 身份进行训练 -----")
    print("-----------------------------------")
    check_update()
    print("启动多进程1……")
    thread1 = mp.Process(target= wfl,daemon=False)
    thread2 = mp.Process(target= wfl2,daemon=False)
    thread1.start()
    thread2.start()
