import torch
import torch.nn.functional as F

class batch_norm(torch.nn.Module):
    def __init__(self, hidden_features, type_norm, skip_connect=False, num_groups=2,
                 skip_weight=0.005):
        super(batch_norm, self).__init__()
        self.type_norm = type_norm
        self.skip_connect = skip_connect
        self.num_groups = num_groups
        self.skip_weight = skip_weight
        self.hidden_features= hidden_features
        if self.type_norm == 'batch':
            self.bn = torch.nn.BatchNorm1d(hidden_features, momentum=0.3)
        elif self.type_norm == 'group':
            self.bn = torch.nn.BatchNorm1d(hidden_features*self.num_groups, momentum=0.3)
            self.group_func = torch.nn.Linear(hidden_features, self.num_groups, bias=True)
        else:
            pass

    def forward(self, x):
        if self.type_norm == 'None':
            return x
        elif self.type_norm == 'batch':
            # print(self.bn.running_mean.size())
            return self.bn(x)
        elif self.type_norm == 'group':
            if self.num_groups == 1:
                x_temp = self.bn(x)
            else:
                score_cluster = F.softmax(self.group_func(x), dim=1)
                x_temp = torch.cat([score_cluster[:, group].unsqueeze(dim=1) * x for group in range(self.num_groups)], dim=1)
                x_temp = self.bn(x_temp).view(-1, self.num_groups, self.hidden_features).sum(dim=1)
            x = x + x_temp * self.skip_weight
            return x

        else:
            raise Exception(f'the normalization has not been implemented')
