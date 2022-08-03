import os
import random
import time
import shutil

date = round(time.time() * 1000)
tmp_path = './temp/' + str(date)


def bg_photo_name_gen(tmp_path):
    bg_names = []
    os.mkdir(tmp_path)
    for i in range(0, 20):  # 6280+1
        shutil.copyfile('./scrap_data/bg/' + str(random.randint(0, 6280)),
                        tmp_path + '/frame' + str(i) + '.jpg')


bg_photo_name_gen(tmp_path)
