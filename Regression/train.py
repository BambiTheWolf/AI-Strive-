from torch import nan_to_num

class MLP(nn.Module):
    def __init__(self, input_size, hidden_size, output_size):
        super(MLP, self).__init__()
        
        self.fc1 = nn.Linear(input_size, hidden_size[0])
        
        layers = []
        for i in range(hidden_size):
            self.layers.append(nn.Linear)
        
        self.fc2 = nn.Linear(hidden_size, output_size)
    
    def forward(self, x):
        
        x = self.fc1(x)
        x = nn.ReLU(x)
        return self.fc2(x)
