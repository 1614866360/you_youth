# -*- coding: utf-8 -*-
# @File  : project_main.py
# @Author: Thomas_yx
# @Date  : 2020/8/20
# @Contact : yx20001210@163.com
# @Software : PyCharm

#导入paddlehub
import paddlehub as hub
#加载预训练模型
module = hub.Module(name="resnet_v2_50_imagenet")

#数据准备
#加载图片数据集
from paddlehub.dataset.base_cv_dataset import BaseCVDataset
class DemoDataset(BaseCVDataset):
    def __init__(self):
        # 数据集存放位置

        self.dataset_dir = "D:\\19001837\\python\\project"
        super(DemoDataset, self).__init__(
            base_path=self.dataset_dir,
            train_list_file="train_list.txt",   #训练列表（路径）
            validate_list_file="validate.txt",  #预测列表（路径）
            test_list_file="test_list.txt",     #检测列表（路径）

            label_list_file="label_list.txt",   #标签列表
        )
dataset = DemoDataset()


#生成数据读取器
#接着生成一个图像分类的reader，reader负责将dataset的数据进行预处理，接着以特定格式组织并输入给模型进行训练。
#当我们生成一个图像分类的reader时，需要指定输入图片的大小
data_reader = hub.reader.ImageClassificationReader(
    image_width=module.get_expected_image_width(),
    image_height=module.get_expected_image_height(),
    images_mean=module.get_pretrained_images_mean(),
    images_std=module.get_pretrained_images_std(),
    dataset=dataset)

#配置策略
config = hub.RunConfig(
    use_cuda=False,                              #是否使用GPU训练，默认为False；
    num_epoch=3,                                #Fine-tune的轮数；
    checkpoint_dir="cv_finetune_turtorial_demo",#模型checkpoint保存路径, 若用户没有指定，程序会自动生成；
    batch_size=30,                              #训练的批大小，如果使用GPU，请根据实际情况调整batch_size；
    eval_interval=15,                           #模型评估的间隔，默认每100个step评估一次验证集；
    strategy=hub.finetune.strategy.DefaultFinetuneStrategy())  #Fine-tune优化策略；

#组建Finetune Task
input_dict, output_dict, program = module.context(trainable=True)       #获取module的上下文环境，包括输入和输出的变量，以及Paddle Program；
img = input_dict["image"]
feature_map = output_dict["feature_map"]        #从输出变量中找到特征图提取层feature_map
feed_list = [img.name]

#在feature_map后面接入一个全连接层，生成Task
task = hub.ImageClassifierTask(
    data_reader=data_reader,
    feed_list=feed_list,
    feature=feature_map,
    num_classes=dataset.num_labels,
    config=config)

#我们选择finetune_and_eval接口来进行模型训练，这个接口在finetune的过程中，会周期性的进行模型效果的评估，以便我们了解整个训练过程的性能变化
# run_states = task.finetune_and_eval()









