import importlib


# find the dataset definition by name, for example ScanNetDataset (scannet.py)
def find_dataset_def(dataset_name):
    module_name = 'datasets.{}'.format(dataset_name)
    module = importlib.import_module(module_name)  #先获取文件  之后再返回文件当中的类
    if dataset_name == 'scannet':
        return getattr(module, "ScanNetDataset")   #返回ScanNetDataset类
    elif dataset_name == 'demo':
        return getattr(module, "DemoDataset")  #返回DemoDataset类
