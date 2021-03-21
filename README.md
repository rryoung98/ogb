## Differential Group Normalization for GraphCONV and GCN

This experiment is based on stanford OGB (1.2.1) benchmark. The description of 《Towards Deeper Graph Neural Networks with Differentiable Group Normalization》 is [avaiable here](https://arxiv.org/abs/2006.06972). The steps are:

### Note!
We propose **DGN GraphCONV** and **DGN GCN** , where we extend our base model's width by implementing DGN, which allows for models to be deeper by incorporating soft clustering to the normalization. 

### Environment:
We recommend importing the given ipython notebook into Google Colab, which provides free GPUs and most of the packages needed to run this code already installed.

### Baseline:
Search for occurences of the code `self.bn` in the `GNN` class and comment that out (should be in two places) in order to run the baseline model without DGN. If you want to change between GCN and GraphConv, simply replace occurence of `GraphConv()` in `__init__()` with `GCNConv()` and vice-versa.

### Running the Code
Running the code is simple, just run all the cells in the notebook. In particular, running the last cell will perform one run of an experiment with the given random seed appiled to the `main()` function at the bottom of the last cell. In order to change the random seed for another run, simply change the value passed in to main.
  
### The **detailed hyperparameter** is:

```
num_layers          3
hidden_channels     256
num_batch_groups    2
dropout             0.0
batch_size          64 * 1024
lr                  1e-3
epochs              400
```

### Reference performance for OGBL-collab:

| Model                 |Valid Accuracy   | Parameters    | Hardware |
| --------------------  | --------------- | ------------- |----------|
| GCN                   | 0.5263  ± 0.150 | 296,449  | Tesla K80 |
| GCN+DGN               | 0.5778  ± 0.636 | 429,571 | Tesla K80 |
| GraphCONV             | 0.5378  ± 0.777 | 460,289 | Tesla K80 |
| GraphCONV+DGN         | 0.5527  ± 0.311 | 593,411  | Tesla K80 |
