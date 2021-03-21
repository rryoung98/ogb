<p align='center'>
  <img width='40%' src='https://snap-stanford.github.io/ogb-web/assets/img/OGB_rectangle.png' />
</p>

--------------------------------------------------------------------------------


[![PyPi Latest Release](https://img.shields.io/pypi/v/pgl.svg)](https://pypi.org/project/pgl/)
[![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](./LICENSE)
## Differential Group Normalization for GraphCONV and GCN

This experiment is based on stanford OGB (1.2.1) benchmark. The description of 《Towards Deeper Graph Neural Networks with Differentiable Group Normalization》 is [avaiable here](https://arxiv.org/abs/2006.06972). The steps are:

### Note!
We propose **DGN GraphCONV** and **DGN GCN* , where we extend our base model's width by implementing DGN, which allows for models to be deeper by incorporating soft clustering to the normalization. 

### Install environment:
``` 
    git clone https://github.com/rryoung98/ogb/
    cd ogb
    pip install -e .
    
```
### Arxiv dataset:
  1. ```python main_arxiv.py --place 0 --log_file arxiv_baseline.txt``` to get the baseline result of arxiv dataset.
  2. ```python main_arxiv.py --place 0 --use_label_e --log_file arxiv_unimp.txt``` to get the UniMP result of arxiv dataset.
  3. ```python main_arxiv_large.py --place 0 --use_label_e --log_file arxiv_unimp_large.txt``` to get the UniMP_large result of arxiv dataset.
  
### The **detailed hyperparameter** is:

```
Collab_dataset:          
--num_layers        3                    
--hidden_size       128           
--num_heads         2            
--dropout           0.3           
--lr                0.001            
```

### Reference performance for OGBL-collab:

| Model                 |Valid Accuracy   | Parameters    | Hardware |
| ------------------  | --------------- | -------------- |----------|
| GCN                 | 0.7367  ± 0.0012 | 468,369  | Tesla V100 (32GB) |
| GCN+DGN             | 0.7450  ± 0.0005 | 473,489 | Tesla V100 (32GB) |
| GraphCONV           | 0.7475  ± 0.0008 | 1,162,515 | Tesla V100 (32GB) |
| GraphCONV+DGN       | 0.9286  ± 0.0017 | 1,470,905  | Tesla V100 (32GB) |
   
## Citing OGB
```
@article{hu2020ogb,
  title={Open Graph Benchmark: Datasets for Machine Learning on Graphs},
  author={Weihua Hu, Matthias Fey, Marinka Zitnik, Yuxiao Dong, Hongyu Ren, Bowen Liu, Michele Catasta, Jure Leskovec},
  journal={arXiv preprint arXiv:2005.00687},
  year={2020}
}
```
